FROM apache/hive:3.1.3

ARG POSTGRES_DRIVER_VERSION="42.6.0"

USER root
RUN apt-get update && apt-get install -y curl
RUN curl --output $HIVE_HOME/lib/postgresql-$POSTGRES_DRIVER_VERSION.jar https://jdbc.postgresql.org/download/postgresql-$POSTGRES_DRIVER_VERSION.jar
RUN cp /opt/hadoop/share/hadoop/tools/lib/hadoop-aws-*.jar $HIVE_HOME/lib
RUN cp /opt/hadoop/share/hadoop/tools/lib/aws-java-sdk-bundle-*.jar $HIVE_HOME/lib

USER hive
COPY ./entrypoint.sh /entrypoint.sh
ADD conf/hive-site.xml /opt/hive/conf

ENTRYPOINT  [ "/entrypoint.sh" ]
