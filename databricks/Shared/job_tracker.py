# src/utils/job_tracker.py

import uuid
from datetime import datetime, timedelta
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, max
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

DEFAULT_START_DATE = datetime(2025, 7, 17).date()

def _ensure_job_tracker_table_exists(spark: SparkSession, job_tracker_table_path: str):
    create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS delta.`{job_tracker_table_path}` (
            job_name STRING NOT NULL,
            run_id STRING NOT NULL,
            start_time TIMESTAMP NOT NULL,
            end_time TIMESTAMP,
            status STRING NOT NULL,
            message STRING
        ) USING DELTA
        LOCATION '{job_tracker_table_path}'
    """
    try:
        spark.sql(create_table_sql)
        print(f"Ensured job tracker table exists at: {job_tracker_table_path}")
    except Exception as e:
        print(f"Error ensuring job tracker table exists: {e}")
        raise # Re-raise to prevent job from proceeding without tracker


def get_last_successful_run_time(spark: SparkSession, job_tracker_table_path: str, job_name: str) -> datetime | None:
    try:
        _ensure_job_tracker_table_exists(spark, job_tracker_table_path)
        tracker_df = spark.read.format("delta").load(job_tracker_table_path)

        last_run_df = tracker_df.filter(
            (col("job_name") == job_name) & (col("status") == "SUCCEEDED")
        ).orderBy(col("start_time").desc())

        if last_run_df.count() > 0:
            last_successful_time = last_run_df.first()["start_time"]
            print(f"Found last successful run for '{job_name}' at: {last_successful_time}")
            return last_successful_time
        else:
            print(f"No previous successful run found for '{job_name}'.")
            return None
    except Exception as e:
        print(f"Error reading job tracker for last successful run for '{job_name}': {e}")
        return None


def record_job_status(spark: SparkSession, job_tracker_table_path: str, job_name: str, run_id: str, status: str,
                      start_time: datetime, end_time: datetime = None,
                      message: str = None):
    _ensure_job_tracker_table_exists(spark, job_tracker_table_path) # Ensure table before writing

    schema = StructType([
        StructField("job_name", StringType(), False),
        StructField("run_id", StringType(), False),
        StructField("start_time", TimestampType(), False),
        StructField("end_time", TimestampType(), True),
        StructField("status", StringType(), False),
        StructField("message", StringType(), True)
    ])

    data = [(job_name, run_id, start_time, end_time, status, message)]

    new_status_df = spark.createDataFrame(data, schema=schema)
    new_status_df.createOrReplaceTempView("new_status_df_temp_view") # Create a temp view for MERGE

    try:
        merge_sql = f"""
            MERGE INTO delta.`{job_tracker_table_path}` AS target
            USING new_status_df_temp_view AS source
            ON target.job_name = source.job_name AND target.run_id = source.run_id
            WHEN MATCHED THEN
                UPDATE SET
                    end_time = source.end_time,
                    status = source.status,
                    message = source.message
            WHEN NOT MATCHED THEN
                INSERT (job_name, run_id, start_time, end_time, status, message)
                VALUES (source.job_name, source.run_id, source.start_time, source.end_time, source.status, source.message)
        """
        spark.sql(merge_sql)
        print(f"Job status for '{job_name}' (run_id: {run_id}) recorded as: {status}")
    except Exception as e:
        print(f"ERROR: Failed to record job status for '{job_name}' (run_id: {run_id}): {e}")
        raise # Re-raise to ensure the job failure is propagated

def get_current_run_id(spark: SparkSession) -> str:
    """
    Get the Databricks run ID from Spark conf, otherwise generates a UUID.
    """
    try:
        return spark.conf.get("spark.databricks.driver.runId")
    except Exception:
        run_id = str(uuid.uuid4())
        print(f"Warning: spark.databricks.driver.runId not found. Using generated UUID: {run_id}")
        return run_id

def generate_date_range_json(last_successful_run_date: datetime | None, current_job_date: datetime) -> list[str]:
    """
    Generates a JSON array of dates (YYYY-MM-DD) between the last successful run date and the current job date.
    """
    date_list = []
    
    # Ensure it's date only, not time
    end_date = current_job_date.date()

    if last_successful_run_date:
        start_date = last_successful_run_date.date()
        # Ensure start_date is not after end_date
        if start_date > end_date:
            start_date = end_date
    else:
        # If no last successful run, start from DEFAULT_START_DATE.
        start_date = DEFAULT_START_DATE

    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    return date_list