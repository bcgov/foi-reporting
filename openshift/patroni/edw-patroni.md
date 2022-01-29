Basic Reference Doc : https://github.com/BCDevOps/platform-services/tree/master/apps/pgsql/patroni

### First step is to pull ImageStream for POSTGRES AND PATRONI, then build it on tools project . In this case its  c84b95-tools

        oc process -f openshift/build.yaml \
            -p "GIT_URI=$(git config --get remote.origin.url)" \
            -p "GIT_REF=$(git rev-parse --abbrev-ref HEAD)" \
            -p SUFFIX=-pg11 \
            -p OUT_VERSION=v11-latest \
            -p PG_VERSION=11 | oc create -f -

#### Please delay the build cmd till both the imagestream are successfully pulled

        # Trigger a build
        oc start-build patroni-pg11
        
#### Note : Please make sure tagging on the patroni is missing or not, if missing try adding using the below command. As per above commands , expecting a tag "v11-latest"

   
        oc tag patroni patroni:v11-latest

###### Make sure builds are succesfull and shows "complete" without any errors or warning

### Second part is to switch to DEV/TEST/PROD OC project
        oc project c84b95-dev
        
##### first step is set up the service account permission on the project
        #need to make service account refered is not "default". Earlier, we were having an "ImagePullBackup" due to using a wrong service account. *** 
        oc policy add-role-to-user
        system:image-puller system:serviceaccount:c84b95-dev:patroni-001


##### second to this we can  run pre-req & deployment yaml on the oc project

        oc process -f openshift/deployment-prereq.yaml \
                -p NAME=patroni \
                -p SUFFIX=-001 | oc create -f -

        oc process -f openshift/deployment.yaml \
         -p NAME=patroni \
         -p "IMAGE_STREAM_NAMESPACE=$(oc project -q)" \
         -p "IMAGE_STREAM_TAG=patroni:v11-latest" \
         -p REPLICAS=3 \
         -p SUFFIX=-001 | oc apply -f -





Rocket chat Reference for the error caused : https://chat.developer.gov.bc.ca/channel/devops-how-to/thread/Bi8KC4W6LwgmMgkDk
