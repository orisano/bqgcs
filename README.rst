BQGCS
===================================
| Google Cloud Storage Connector for Google BigQuery.

Getting Started
--------
.. code:: bash

    pip install bqgcs

How to Use
--------
.. code:: python

    import bqgcs
    from google.cloud import bigquery, storage

    gcs = storage.Client()
    blob = gcs.bucket("<<bucket_name>>").blob("<<blob_name>>")
    bqgcs.query_to_gcs("SELECT * FROM 'project.dataset.table'", blob)

    bq = bigquery.Client()
    table = bq.dataset("<<dataset>>").table("<<table>>")
    bqgcs.gcs_to_bq(blob, table)


License
--------
MIT
