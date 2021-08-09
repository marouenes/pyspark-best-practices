# -*- coding: utf-8 -*-

import os
import sys

if os.path.exists('src.zip'):
    sys.path.insert(0, 'src.zip')
else:
    sys.path.insert(0, './src')

from utilities import app

if __name__ == '__main__':

    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .master("local") \
        .appName("Test") \
        .getOrCreate()

    app.say_hello('John')
    print(spark.range(10000).where("id > 1000").selectExpr("sum(id)").collect())
