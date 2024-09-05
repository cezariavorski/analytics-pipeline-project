import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark session (simulating Databricks)
spark = SparkSession.builder.appName("Data Ingestion").getOrCreate()


data = {
    'name': ['Carlos Silva', 'Ana Souza', 'Pedro Oliveira'],
    'age': [29, 35, 42],
    'city': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(data)


spark_df = spark.createDataFrame(df)

spark_df = spark_df.withColumn('age_in_months', spark_df['age'] * 12)
spark_df.show()


mock_snowflake_db = []


def insert_into_snowflake(name, age_in_months, city):
    mock_snowflake_db.append({
        'name': name,
        'age_in_months': age_in_months,
        'city': city
    })


for row in spark_df.collect():
    insert_into_snowflake(row['name'], row['age_in_months'], row['city'])


def query_snowflake():
    return mock_snowflake_db


result = query_snowflake()
print("Data in Mocked Snowflake DB:")
for row in result:
    print(row)
