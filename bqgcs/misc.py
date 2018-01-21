if False:
    from google.cloud import storage


def gcs_path(blob):  # type: (storage.Blob) -> str
    return "gs://{}/{}".format(blob.bucket.name, blob.name)
