from pyspark.sql import SparkSession, DataFrame, functions as F
from pyspark.sql.window import Window
import uuid
from pyspark.sql.functions import lit, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from delta.tables import DeltaTable



def append_with_incrementing_id(
    new_df: DataFrame,
    table_name: str,
    id_column: str = "id",
    order_by_column: str = None,
    database: str = "default"
):
    """
    Appends new_df to a Delta table with string auto-increment IDs like '1', '2', '3', ...

    Parameters:
    - new_df: The new data to insert.
    - table_name: Target Delta table name (must exist).
    - id_column: Name of the ID column (default: 'id').
    - order_by_column: Optional: Column to use for ordering (for deterministic IDs).
    - database: Databricks database containing the table.
    """
    spark = SparkSession.getActiveSession()
    full_table_name = f"{database}.{table_name}"

    if not spark._jsparkSession.catalog().tableExists(full_table_name):
        raise Exception(f"Table {full_table_name} does not exist. Please create it first.")

    existing_df = spark.table(full_table_name)

    if id_column in existing_df.columns:
        numeric_part_expr = F.regexp_extract(F.col(id_column), r"(\d+)$", 1).cast("long")
        max_id_row = existing_df.select(F.max(numeric_part_expr)).collect()[0][0]
        max_id = max_id_row if max_id_row is not None else 0
    else:
        max_id = 0

    if order_by_column and order_by_column in new_df.columns:
        windowSpec = Window.orderBy(F.col(order_by_column))
    else:
        windowSpec = Window.orderBy(F.lit(1))

    new_df_with_number = new_df.withColumn(
        "__rownum", F.row_number().over(windowSpec) + max_id
    )

    new_df_with_id = new_df_with_number.withColumn(
        id_column, F.col("__rownum")
    ).drop("__rownum")

    cols = new_df_with_id.columns
    ordered_cols = [id_column] + [c for c in cols if c != id_column]
    new_df_with_id = new_df_with_id.select(ordered_cols)

    # new_df_with_id.write.mode("append").saveAsTable(full_table_name)

    new_df_with_id.printSchema()
    
    new_df_with_id.write.format("delta").mode("append").option("mergeSchema", "false").insertInto(full_table_name)  

    print(f"✅ Appended {new_df_with_id.count()} rows to {full_table_name} with IDs like '1', '2', '3', ...")


def start_run_cycle(
    packagename: str,
):
    """
    Inserts a new row into the run cycle table to mark the start of a cycle.

    Parameters:
    - table_name: name of the target Delta table
    - description: description of this run cycle (string)
    - packageid: package identifier (string)
    - packagename: package name (string)
    - database: optional database name (default: 'default')
    """
    spark = SparkSession.getActiveSession()
    df_existing = spark.sql("SELECT max(cast(runcycleid as int)) as runcycleid FROM dimruncycle")
    runcycleid = df_existing.first().runcycleid + 1
    full_table = f"default.dimruncycle"

    description = "package: " + packagename + " started"

    # Generate a UUID object
    uuid_obj = uuid.uuid4()

    # Convert the UUID object to a string and make it uppercase
    packageid = str(uuid_obj).upper()

    # Build single-row DataFrame
    data = spark.createDataFrame(
        [
            (
                runcycleid,
                None,  # runcyclestartat (will be filled below)
                description,
                packageid,
                packagename,
                None,  # runcycleendat
                "NULL"  # success
            )
        ],
        schema = StructType([
                StructField("runcycleid", IntegerType(), False),         # int
                StructField("runcyclestartat", TimestampType(), True),   # timestamp
                StructField("description", StringType(), True),          # string
                StructField("packageid", StringType(), True),            # string
                StructField("packagename", StringType(), True),          # string
                StructField("runcycleendat", StringType(), True),        # string (you may want to make this a TimestampType too)
                StructField("success", StringType(), True),              # string
        ])
    )

    # Set current timestamp as runcyclestartat
    df_with_timestamp = data.withColumn("runcyclestartat", current_timestamp())

    # Append to table
    df_with_timestamp.write.mode("append").saveAsTable(full_table)

    print(f"✅ Run cycle '{runcycleid}' inserted into {full_table}.")
    return runcycleid

def end_run_cycle(
    runcycleid: str,
    success: str,
    packagename: str,
    error: str = None,
):
    """
    Updates the run cycle row to mark the end of the run.

    Parameters:
    - table_name: name of the target Delta table
    - runcycleid: ID of the run cycle to update
    - success: True or False indicating run success
    - database: optional database name (default: 'default')
    """
    spark = SparkSession.getActiveSession()
    full_table = f"default.dimruncycle"

    delta_table = DeltaTable.forName(spark, full_table)

    if success == 't':
        description = "package: " + packagename + " complete"
    else:        
        description = "package: " + packagename + " error " + error

    

    # Perform update
    delta_table.update(
        condition=f"runcycleid = '{runcycleid}'",
        set={
            "description": lit(str(description)),
            "runcycleendat": current_timestamp().cast("string"),
            "success": lit(str(success).lower()),
        }
    )

    print(f"✅ Run cycle '{runcycleid}' marked as ended with success={success}.")