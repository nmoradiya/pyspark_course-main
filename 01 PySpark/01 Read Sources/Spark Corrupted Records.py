# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
# MAGIC %md
# MAGIC This lesson is about the how to handle corrupted data file.
# MAGIC

# COMMAND ----------

# PERMISSIVE mode - include corrupted data rows with additional columns named as _corrupt_record
#- DROPMALFORMED mode - drop corrupted data rows
#- FAILFAST mode - throw an exception if any corrupted data rows are found
# DBTITLE 1,PERMISSIVE mode - include corrupted data rows with additional columns named as _corrupt_record
df=spark.read.format("json").\
    option("mode","PERMISSIVE").\
    load("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/json_files/sales_corrupted.json")
display(df)

# COMMAND ----------

# defult PERMISSIVE mode has included corrupted data where column _c3 display value as xx.

df=spark.read.format("csv").load("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_corrupted.csv")
display(df)

# COMMAND ----------

schema_str = "id INT, customer_name STRING, product STRING, quantity INT, price DOUBLE, remarks STRING, _corrupt_record STRING"

df=spark.read.\
schema(schema_str)\
.format("csv")\
.option("mode","DROPMALFORMED")\
.load("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_corrupted.csv")

display(df)

# COMMAND ----------

schema_str = "id INT, customer_name STRING, product STRING, quantity INT, price DOUBLE, remarks STRING"

df=spark.read.\
schema(schema_str)\
.format("csv")\
.option("badRecordsPath","/Volumes/dblearn_nk/raw_datafiles/output_files/badRecordsPath")\
.load("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_corrupted.csv")

display(df)

# COMMAND ----------

df2=spark.read.format("json").option("recursiveFileLookup", "true").load("/Volumes/dblearn_nk/raw_datafiles/output_files/badRecordsPath")
display(df2)
