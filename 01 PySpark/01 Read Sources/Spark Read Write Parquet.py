# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
df=spark.read.json("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/json_files/sales_single_line.json")
display(df)

# COMMAND ----------

df.write.format("parquet").save("/Volumes/dblearn_nk/raw_datafiles/output_files/parquet_files_sample")

# COMMAND ----------

df2=spark.read.format("parquet").load("/Volumes/dblearn_nk/raw_datafiles/output_files/parquet_files_sample")

# COMMAND ----------

display(df2)
