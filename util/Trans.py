import requests


def downloadFile(save_path, file_url):
    r = requests.get(file_url)  # create HTTP response object

    with open(save_path, 'wb') as f:
        f.write(r.content)

    return save_path
