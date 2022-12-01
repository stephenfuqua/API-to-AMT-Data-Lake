from dagster import repository

from dagster_data_lake.jobs.pipe_api import pipe_api_job
from dagster_data_lake.schedules.schedule import hourly_schedule
from .sensors.sensor import sensor

import os

@repository
def dagster_data_lake():
    jobs = [pipe_api_job]
    schedules = [hourly_schedule]
    sensors = [sensor]
    return jobs + schedules + sensors
