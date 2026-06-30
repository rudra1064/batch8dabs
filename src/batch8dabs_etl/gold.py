# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg,count

spark = SparkSession.builder.getOrCreate()

silver = spark.table("dbx_training.silver.iris_clean")

gold = (
    silver.groupBy("species")
          .agg(
              count("*").alias("total_flowers"),
              avg("sepal_length").alias("avg_sepal_length"),
              avg("petal_length").alias("avg_petal_length")
          )
)

gold.write.mode("overwrite").saveAsTable("dbx_training.gold.iris_summary")

print("Gold Completed")

display(gold)