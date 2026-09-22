from graph_algorithms import get_file_contents_from_disk

# A simple test to get my started with pytest
# Run by calling 'pytest' in the terminal
def test_get_local_pages():
    pages_dict = get_file_contents_from_disk()
    assert len(pages_dict) == 10000
