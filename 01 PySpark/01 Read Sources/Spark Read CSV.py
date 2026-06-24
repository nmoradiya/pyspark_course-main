# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "2"
# ///
df=spark.read.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales.csv")

display(df)

# COMMAND ----------

df=spark.read.option("header","true").\
csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales.csv")

display(df)

# COMMAND ----------

df=spark.read.\
option("header","true")\
.option("inferSchema","true")\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales.csv")

display(df)

# COMMAND ----------

schema_str = "id INT, customer_name STRING, product STRING, quantity INT, price DOUBLE, remarks STRING"

df=spark.read.\
schema(schema_str)\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_no_header.csv")

display(df)

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

schema = StructType([
    StructField("id", StringType(), True),
    StructField("customer_name", StringType(), True),
    StructField("my_product", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("remarks", StringType(), True)
])

df=spark.read.\
schema(schema)\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_no_header.csv")

display(df)

# COMMAND ----------

df=spark.read.\
option("header","true")\
.option("inferSchema","true")\
.option("delimiter","|")\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_pipe.csv")

display(df)

# COMMAND ----------

df=spark.read.\
option("header","true")\
.option("inferSchema","true")\
.option("delimiter","|")\
.option("quote","'")\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_pipe_single_quote.csv")

display(df)

# COMMAND ----------

df=spark.read.\
option("header","true")\
.option("inferSchema","true")\
.option("delimiter","|")\
.option("quote","'")\
.option("escape","#")\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_pipe_single_quote_escape.csv")

display(df)

# COMMAND ----------

df=spark.read.\
option("header","true")\
.option("inferSchema","true")\
.option("delimiter","|")\
.option("quote","'")\
.option("escape","#")\
.option("multiline","true")\
.csv("/Volumes/dblearn_nk/raw_datafiles/sourcefiles/csv_files/sales_pipe_single_quote_escape_multiline.csv")

display(df)
