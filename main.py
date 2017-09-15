import os

from util.Extract import Extract

# imageio.plugins.ffmpeg.download()

extract = Extract(os.path.join(os.path.dirname(__file__), 'tmp'), '59bb813cc8729c0010ab8929')
extract.execute()

