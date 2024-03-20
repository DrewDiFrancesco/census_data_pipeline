import pandas as pd
import threading
import os
import json
import etl_helpers as etl_helpers
import config as config
from conf_variables import default_args
from spark_session import SparkManager
import importlib
import configparser
from functools import reduce


root_path = os.path.dirname(os.path.abspath(__file__))

# Main function
def main(override_args=None, spark=None):
    print(f"HERE is the override args: {override_args}")

    if override_args:
        default_args.update(override_args)

    print(f"HERE is the new default args: {default_args}")
    config_manager = config.Config(default_args)
    
    running_locally = config_manager.args['running_locally']

    if spark is None:
        print(f"Getting Spark")
        spark = SparkManager(config_manager.args).get_spark()
        print("Done getting spark")

    if config_manager.args['s3_bucket'] != '':
        print(f"Updating data_path because s3_bucket is not an empty string...")
        config_manager.args['data_path'] = config_manager.args['s3_bucket']+'/data'

    api_key = read_data()





if __name__ == '__main__':
    drews_conf = {'data_path': '/Users/drewdifrancesco/Desktop/data',
                  'root_path': root_path,
                  's3_bucket': ''}

    main(override_args=drews_conf)
    # main(None,override_args={})