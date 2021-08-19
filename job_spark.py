from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName('Csv_to_Spark')
    .getOrCreate()
)

enem = (
    spark
    .read
    .format('csv')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', ';')
    .load('s3://datalake-barbara/raw-data/MICRODADOS_ENEM_2019.csv')
)

(
    enem
    .write
    .mode('overwrite')
    .format('parquet')
    .partitionBy("NU_ANO")
    .save('s3://datalake-barbara/consumer-zone')
)