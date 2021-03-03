# Databricks notebook source
dbutils.library.installPyPI("koalas")
dbutils.library.installPyPI('numpy','1.16.3')
dbutils.library.installPyPI('pandas','0.24.2')
dbutils.library.restartPython()

# COMMAND ----------

from pyspark.sql.types import StructType,StructField,StringType, DecimalType
from decimal import Decimal
from pyspark.sql import Row
data1 = [Row("1","12", Decimal(1.0),"In Progress"),
         Row("2","13", Decimal(2.0),"In Progress"),
         Row("3","14", Decimal(3.0),"End"),
         Row("4","15", Decimal(4.0),"End")
  ]

schema = StructType([ \
    StructField("row_id",StringType(),True), \
    StructField("order_num",StringType(),True), \
    StructField("recv_num",DecimalType(15, 7),True), \
    StructField("status_cd", StringType(), True)
  ])
 
df1 = spark.createDataFrame(data=data1,schema=schema)


data2 = [Row("5","15", Decimal(1.0),"In Progress"),
         Row("6","16", Decimal(2.0),"In Progress"),
         Row("7","17", Decimal(3.0),"End"),
         Row("8","18", Decimal(4.0),"End")
  ]

df2 = spark.createDataFrame(data=data2,schema=schema)

data3 = [Row("9","19", Decimal(1.0),"In Progress"),
         Row("10","110", Decimal(2.0),"In Progress"),
         Row("11","111", Decimal(3.0),"End"),
         Row("12","112", Decimal(4.0),"End")
  ]

df3 = spark.createDataFrame(data=data3,schema=schema)

# COMMAND ----------

x = spark.conf.set("spark.rpc.message.maxSize")
print(x)

# COMMAND ----------

spark.conf.set("spark.rpc.message.maxSize", 512)

# COMMAND ----------

