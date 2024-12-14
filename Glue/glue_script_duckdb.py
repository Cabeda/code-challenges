import duckdb

duckdb.sql("SET home_directory='/tmp';")

con = duckdb.connect()

duckdb.sql("""CREATE SECRET (
    TYPE S3,
    PROVIDER CREDENTIAL_CHAIN
);""")

main = con.sql("SELECT * FROM 'data.parquet' limit 100").df()

print(main.head())
