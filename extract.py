import os
import shutil
import zipfile

from moviepy.editor import VideoFileClip

from util import Comm, Trans, Config

CONFIG_TEMP_PATH = Config.getValue('FILE', 'TEMP_PATH')
CONFIG_TEMP_ZIP_FILE_NAME = Config.getValue('FILE', 'TEMP_ZIP_FILE_NAME')

TEMP_PATH = os.path.join(CONFIG_TEMP_PATH, 'img')

TIME = [(0, 4), (8, 12), (15, 20), (40, 50), (50, 60)]

Comm.checkAndCreateDirectory(CONFIG_TEMP_PATH)
Comm.checkAndCreateDirectory(TEMP_PATH)

video_path = Trans.downloadFile(os.path.join(CONFIG_TEMP_PATH, 'temp.mp4')
                                ,
                                'http://0.s3.envato.com/h264-video-previews/80fad324-9db4-11e3-bf3d-0050569255a8/490527.mp4')

video = VideoFileClip(filename=video_path, audio=False, verbose=True)
zip = zipfile.ZipFile(os.path.join(CONFIG_TEMP_PATH, CONFIG_TEMP_ZIP_FILE_NAME), 'w')

for i in TIME:
    for k in range(i[0], i[1] + 1):
        filePath = os.path.join(TEMP_PATH, str(k) + '.jpg')
        video.save_frame(filename=filePath, t=k)
        zip.write(filePath, os.path.relpath(filePath, TEMP_PATH), compress_type=zipfile.ZIP_DEFLATED)
        print(filePath)

zip.close()
print(zip.filename)
Trans.uploadFileToBucket('whatsit-dataset-video', zip.filename, key='test.zip')
print(shutil.rmtree(CONFIG_TEMP_PATH))
