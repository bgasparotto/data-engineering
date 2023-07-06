#!/bin/bash

echo "Initialising database schema"
if ! schematool -initSchema -dbType postgres 2>/dev/null ; then
  echo "Schema initialisation failed as it has already been initialised. Upgrading it instead"
  schematool -upgradeSchema -dbType postgres 2>/dev/null
fi

export METASTORE_PORT=${METASTORE_PORT:-9083}
hive --skiphadoopversion --skiphbasecp --service metastore
