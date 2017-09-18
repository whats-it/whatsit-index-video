import os

from util.Extract import Extract

# imageio.plugins.ffmpeg.download()

# TODO Service로 부터 Dataset Id를 가져 온다
extract = Extract(os.path.join(os.path.dirname(__file__), 'tmp'), '59bb813cc8729c0010ab8929')
extract.execute()

