from google.cloud import storage

BUCKET_NAME = "cloud-computing-homework-2-bucket"
DIRECTORY = "pages/"

# # Grab every html file from the "pages" directory in my bucket
# def list_pages(bucket_name=BUCKET_NAME, directory=DIRECTORY):
#     client = storage.Client()

#     return [
#         # Google cloud doesn't actually have directories (in a normal bucket)
#         # So I need to remove the 
#         blob.name.removeprefix(directory)
#         for blob in client.list_blobs(bucket_name, prefix=directory)
#         if blob.name.endswith(".html")
#     ]


if __name__ == "__main__":
    client = storage.Client()

    # This returns an iterator
    output = client.list_blobs(BUCKET_NAME)
    # This gives me all the names in my blob iterator
    names = [blob.name for blob in output]

    # Found 10000 objects
    print(f"Found {len(names)} objects")
    # ['pages/0.html', 'pages/1.html', 'pages/10.html', 'pages/100.html', 'pages/1000.html']
    print(names[:5])