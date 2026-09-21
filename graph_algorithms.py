from google.cloud import storage

BUCKET_NAME = "cloud-computing-homework-2-bucket"
DIRECTORY = "pages/"

# Grab the contents of every html file in my bucket as a string
def get_file_contents_from_GCS(bucket_name: str = BUCKET_NAME, directory: str = DIRECTORY) -> dict[str, str]:
    client = storage.Client()

    # Client.list_blobs returns an iterator of all my blobs in my bucket
    # A blob is just a reference to a file in GCS, not a file itself
    blob_iterator = client.list_blobs(bucket_name)

    # Consume my iterator into a list 
    blobs = list(blob_iterator)

    # Download the contents of every blob into local memory
    html_pages = {}
    for blob in blobs:
        html_pages[blob.name.removeprefix(directory)] = blob.download_as_text()

        # uncomment this if you don't want it to take forever.
        # and comment the above line
        # if blob.name == "pages/1001.html": 
        #     html_pages[blob.name.removeprefix(directory)] = blob.download_as_text()

    return html_pages


# TODO write a test module for this
# TODO make a dummy function for tests that just gets the files from the local dir
if __name__ == "__main__":
    output = get_file_contents_from_GCS()
    print(output["1001.html"])