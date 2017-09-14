import os
import shutil


# noinspection PyPep8Naming
def check_and_create_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
