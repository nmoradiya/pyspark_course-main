# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
df=spark.read.text("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/log_files/")
display(df)

# COMMAND ----------

df=spark.read.text("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/log_files/",wholetext=True)
display(df)

# COMMAND ----------

df = spark.read.format("binaryFile").load("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/log_files/")
display(df)

# COMMAND ----------

df=spark.read.text("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/log_files/",wholetext=True)
df2=df.selectExpr("value", "_metadata.file_path", "_metadata.file_name", "_metadata.file_size", "_metadata.file_modification_time")
display(df2)


# COMMAND ----------

df=spark.read.parquet("/Volumes/dblearn_nk/raw_datafiles/output_files/parquet_files_sample/")
display(df)

# COMMAND ----------

df2=df.selectExpr("customer_name",'id','price','product','quantity','remarks', "_metadata.file_path", "_metadata.file_name", "_metadata.file_size", "_metadata.file_modification_time")
display(df2)
