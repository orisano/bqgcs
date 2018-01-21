from google.cloud import bigquery

from .misc import gcs_path

if False:
    from google.cloud import storage


def bq_to_gcs(table, blob):  # type: (bigquery.TableReference, storage.Blob) -> None
    bq = bigquery.Client()
    extract_job = bq.extract_table(table, gcs_path(blob))
    extract_job.result()


def query_to_table(query):  # type: (str) -> bigquery.TableReference
    bq = bigquery.Client()
    query_job = bq.query(query)
    query_job.result()

    return query_job.destination


def query_to_gcs(query, blob):  # type: (str, storage.Blob) -> None
    bq_to_gcs(query_to_table(query), blob)
