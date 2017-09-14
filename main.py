from util import Trans

# imageio.plugins.ffmpeg.download()

# extract = Extract(os.path.join(os.path.dirname(__file__), 'tmp'), 'dataset_id')
# extract.execute()

print(Trans.request_service('http://api.whatsit.net/datasets/59b24dc8c3113c00135c2ed2'))
