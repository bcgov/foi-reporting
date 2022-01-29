Basic Reference Doc : https://github.com/BCDevOps/platform-services/tree/master/apps/pgsql/patroni

### First step is to pull ImageStream for POSTGRES AND PATRONI, then build it on tools project . In this case its  c84b95-tools
    ``` bash

        oc process -f openshift/build.yaml \
            -p "GIT_URI=$(git config --get remote.origin.url)" \
            -p "GIT_REF=$(git rev-parse --abbrev-ref HEAD)" \
            -p SUFFIX=-pg11 \
            -p OUT_VERSION=v11-latest \
            -p PG_VERSION=11 | oc create -f -

    ```













https://chat.developer.gov.bc.ca/channel/devops-how-to/thread/Bi8KC4W6LwgmMgkDk
