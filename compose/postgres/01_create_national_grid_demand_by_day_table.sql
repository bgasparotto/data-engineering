create table national_grid_demand_by_day
(
    "date"                         date   not null unique,
    max_national_demand            bigint not null,
    min_national_demand            bigint not null,
    avg_national_demand            bigint not null,
    max_transmission_system_demand bigint not null,
    min_transmission_system_demand bigint not null,
    avg_transmission_system_demand bigint not null
);

create index idx_national_grid_demand_by_day_date
    ON national_grid_demand_by_day ("date");
