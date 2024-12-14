
from pyiceberg.catalog import load_catalog

catalog = load_catalog("default")

table = catalog.load_table("core_variant_mngmnt_staging.core_jobs_with_pms")

df = table.scan(limit=10).to_pandas()
print(df)