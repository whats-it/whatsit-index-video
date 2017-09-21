import imageio

imageio.plugins.ffmpeg.download()

import os
from util.Extract import Extract
from util.Comm import delete_pod

print(os.environ)
__data_set_id = None

try:
    __data_set_id = os.environ['DATA_SET_ID'].replace('"', '')
    print('data_setID::' + __data_set_id)
except Exception as ex:
    print('Not defined dataset ID value::')
    print(ex)

if __data_set_id is not None:
    extract = Extract(os.path.join(os.path.dirname(__file__), 'tmp'), __data_set_id)
    extract.execute()

# Delete pod
delete_pod()
