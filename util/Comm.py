import os
import shutil


# noinspection PyPep8Naming
def checkAndCreateDirectory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
