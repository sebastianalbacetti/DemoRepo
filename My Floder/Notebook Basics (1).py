# Databricks notebook source
print ("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello World from SQL!"

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Title 1 
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC 
# MAGIC text with a **blod** and *italicized* in it.
# MAGIC 
# MAGIC Ordered list
# MAGIC 1. once
# MAGIC 2. two
# MAGIC 3. three
# MAGIC 
# MAGIC Unordered list
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC Images:
# MAGIC ![Associate-badge](https://www.databricks.com/wp-content/uploads/2022/04/associate-badge-eng.svg)
# MAGIC 
# MAGIC Amd of course, tables:
# MAGIC 
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC |    1    |    Adam   |
# MAGIC |    2    |    Sarah  | 
# MAGIC |    3    |    John   |
# MAGIC 
# MAGIC Links (or Embedded HTML): <a href="https://docs.databricks.com/notebook-manage.html" target="_blank"> managing
# MAGIC Notebooks documentation</a>

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


