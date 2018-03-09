import six
from google.cloud import bigquery

if False:
    from google.cloud import storage
    import pandas as pd
    from typing import *


def pd_to_gcs(dataframe, blob):  # type: (pd.DataFrame, storage.Blob) -> None
    extensions = blob.name.split('.')
    compression = None
    if extensions[-1] == "gz":
        compression = "gzip"
        extensions = extensions[:-1]

    buf = six.StringIO()
    ext = extensions[-1]
    if ext == "csv":
        dataframe.to_csv(buf, compression=compression, index=False)
    elif ext == "json":
        dataframe.to_json(buf, compression=compression)
    else:
        raise Exception("unsupported format: {}".format(ext))

    b = buf.getvalue()
    if six.PY3:
        b = b.encode("utf-8")
    blob.upload_from_file(six.BytesIO(b), rewind=True)


def generate_bq_schema(dataframe):  # type: (pd.DataFrame) -> [bigquery.SchemaField]
    type_mapping = {
        'i': 'INTEGER',
        'b': 'BOOLEAN',
        'f': 'FLOAT',
        'O': 'STRING',
        'S': 'STRING',
        'U': 'STRING',
        'M': 'TIMESTAMP',
    }
    dataframe.to_csv()
    return [
        bigquery.SchemaField(column_name, type_mapping.get(dtype.kind, 'STRING'))
        for column_name, dtype in dataframe.dtypes.items()
    ]
