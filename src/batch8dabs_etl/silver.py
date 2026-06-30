# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

bronze = spark.table("dbx_training.bronze.iris")

silver = (
    bronze
    .dropDuplicates()
    .dropna()
    .withColumnRenamed("SepalLengthCm","sepal_length")
    .withColumnRenamed("SepalWidthCm","sepal_width")
    .withColumnRenamed("PetalLengthCm","petal_length")
    .withColumnRenamed("PetalWidthCm","petal_width")
    .withColumnRenamed("Species","species")
)

silver.write.mode("overwrite").saveAsTable("dbx_training.silver.iris_clean")

print("Silver Completed")

display(silver)