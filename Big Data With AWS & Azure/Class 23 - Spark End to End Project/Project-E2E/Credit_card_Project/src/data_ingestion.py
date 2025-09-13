
import yaml
from pyspark.sql import SparkSession
from src.logger import get_logger

logging = get_logger()

def load_config(config_path):
    with open(config_path) as file:
        config = yaml.safe_load(file)
        print(config)
    return config

def spark_session(config):


    spark = SparkSession.builder \
        .appName(config['spark']['app_name']) \
        .config('shuffle.partitions', config['spark']['shuffle_partitions']) \
        .getOrCreate()
    logging.info('Spark session created')
    return spark

def run_data_ingestion(config_path='configs/config_local.yaml'):
    config = load_config(config_path)
    spark = spark_session(config)
    
    if(config['env']=='local'):
        application = spark.read.csv(config['data_path'], header=True, inferSchema=True)
        credit = spark.read.csv(config['credit_data_path'], header=True, inferSchema=True)
        logging.info("Data loaded successfully")
        print(application.show())

    return application

# config = load_config('configs/config_local.yaml')
# spark = spark_session(config)

run_data_ingestion('configs/config_local.yaml')