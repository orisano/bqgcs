from google.cloud import bigquery

from .misc import gcs_path

if False:
    from google.cloud import storage


def gcs_to_bq(blob, table):  # type: (storage.Blob, bigquery.TableReference) -> None
    bq = bigquery.Client()

    job = bq.load_table_from_uri(gcs_path(blob), table)
    job.result()
