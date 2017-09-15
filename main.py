import os

from util.Extract import Extract

# imageio.plugins.ffmpeg.download()

extract = Extract(os.path.join(os.path.dirname(__file__), 'tmp'), '59b24dc8c3113c00135c2ed2')
extract.execute()
