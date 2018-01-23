from google.cloud import bigquery

from .misc import gcs_path

if False:
    from typing import *

    from google.cloud import storage


def gcs_to_bq(blob, table, job_config=None):
    # type: (storage.Blob, bigquery.TableReference, Optional[bigquery.LoadJobConfig]) -> None
    bq = bigquery.Client()

    job = bq.load_table_from_uri(gcs_path(blob), table, job_config=job_config)
    job.result()
