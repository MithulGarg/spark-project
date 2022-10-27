import pyspark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

# Read JSON files into dataframes
gbrDf = spark.read.json("gbr.jsonl")
ofacDf = spark.read.json("ofac.jsonl")
# df.printSchema()
# df.show()

# df1.intersectAll(df2).show()

# normalize and clean data from both data sets
def normalizeData(x):
    id = x.id.toString()
    # write code to change reported_dates_of_birth and place_of_birth to common format for comparison

# create output dataframe to store result in
columns = ["ofac_id", "uk_id", "matching_data"] # matching_data can be a list of matching identifiers
outputDf = spark.createDataFrame(data=data, schema=columns)
