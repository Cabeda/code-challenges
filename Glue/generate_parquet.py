import duckdb
from faker import Faker

duckdb.sql("SET home_directory='/tmp';")

duckdb.sql("""CREATE SECRET (
    TYPE S3,
    PROVIDER CREDENTIAL_CHAIN
);""")

def random_date():
    fake = Faker()
    return fake.date_between()

# duckdb.create_function("random_date", random_date, [], DATE, type="native", side_effects=True)

duckdb.sql("""
Copy (SELECT hash(i * 10 + j) AS id, IF (j % 2, true, false)
                 FROM generate_series(1, 50) s(i)
                 CROSS JOIN generate_series(1, 5000000) t(j)
                 )
                 TO 'data.parquet'
                 """)
