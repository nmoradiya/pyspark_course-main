# Databricks notebook source
df=spark.read.json("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/json_files/sales_single_line.json")
display(df)

# COMMAND ----------

df=spark.read.option("multiline","true").json("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/json_files/sales_multi_line.json")
display(df)

# COMMAND ----------

df.write.format("csv").save("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_out_files/")
df.write.format("json").save("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/json_out_files/")
