import imageio

imageio.plugins.ffmpeg.download()

import os
from util.Extract import Extract

print(os.environ)

__data_set_id = None

try:
    __data_set_id = os.environ['DATA_SET_ID']
except Exception as ex:
    print('Not defined dataset ID value::')
    print(ex)

if __data_set_id is not None:
    extract = Extract(os.path.join(os.path.dirname(__file__), 'tmp'), __data_set_id)
    extract.execute()
