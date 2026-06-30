# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Read Bronze table
df = spark.table("dbx_training.bronze.iris")

print("Bronze Count :", df.count())

display(df)