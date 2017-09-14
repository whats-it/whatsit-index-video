import os
import shutil
import zipfile

from moviepy.editor import VideoFileClip

from util import Trans, Config, Comm

CONFIG_TEMP_ZIP_FILE_NAME = Config.getValue('FILE', 'TEMP_ZIP_FILE_NAME')


class Extract:
    def __init__(self, path, dataset_id):
        self.__path = path
        self.__img_path = os.path.join(path, 'img')
        self.__dataset_id = dataset_id
        Comm.check_and_create_directory([path, self.__img_path])
        print('Created temp folders')

    def execute(self):
        TIME = [(0, 4), (8, 12), (15, 20), (40, 50), (50, 60)]

        video_path = Trans.download_file(os.path.join(self.__path, 'temp.mp4')
                                         ,
                                         'http://0.s3.envato.com/h264-video-previews/80fad324-9db4-11e3-bf3d-0050569255a8/490527.mp4')

        video = VideoFileClip(filename=video_path, audio=False, verbose=True)
        zip = zipfile.ZipFile(os.path.join(self.__path, CONFIG_TEMP_ZIP_FILE_NAME), 'w')

        print('[Extracted image file from video]')
        for i in TIME:
            for k in range(i[0], i[1] + 1):
                filePath = os.path.join(self.__img_path, str(k) + '.jpg')
                video.save_frame(filename=filePath, t=k)
                zip.write(filePath, os.path.relpath(filePath, self.__img_path), compress_type=zipfile.ZIP_DEFLATED)
                print(filePath)

        zip.close()
        print('\n\nCreated zip file::' + zip.filename)
        Trans.upload_file_to_bucket('whatsit-dataset-video', zip.filename, key=self.__dataset_id + '/test.zip')
        print('Deleted temp directory::')
        shutil.rmtree(self.__path)
