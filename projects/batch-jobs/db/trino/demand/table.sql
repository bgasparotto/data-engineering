CREATE TABLE IF NOT EXISTS hive.datalake.demand
(
    settlement_date            DATE,
    settlement_period          INT,
    national_demand            INT,
    transmission_system_demand INT,
    england_wales_demand       INT,
    embedded_wind_capacity     INT,
    embedded_wind_generation   INT,
    embedded_solar_capacity    INT,
    embedded_solar_generation  INT,
    dt                         VARCHAR
) WITH (
      external_location = 's3a://datalake/demand/',
      format = 'PARQUET',
      partitioned_by = ARRAY ['dt']);
