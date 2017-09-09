import os

from moviepy.editor import VideoFileClip

TEMP_URL = '/Users/bluehack/bluehack/tmp'
TIME = [(0, 4), (8, 12), (15, 20), (40, 50), (50, 60)]

video = VideoFileClip(filename='/Users/bluehack/Downloads/toyota.mp4', audio=False, verbose=True)

for i in TIME:
    for k in range(i[0], i[1] + 1):
        filePath = os.path.join(TEMP_URL, str(k) + '.jpg')
        video.save_frame(filename=filePath, t=k)
        print(filePath)
