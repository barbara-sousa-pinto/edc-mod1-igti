from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName('Csv_to_Parquet')
    .getOrCreate()
)

censo = (
    spark
    .read
    .format('csv')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', '|')
    .load('s3://datalake-barbara/raw-data/censo/')
)

(
    censo
    .write
    .mode('overwrite')
    .format('parquet')
    .partitionBy("NU_ANO")
    .save('s3://datalake-barbara/consumer-zone/censo')
)