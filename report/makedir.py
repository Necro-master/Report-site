import os

def makedir(path):
    """
    create directory and if it exists don't do anything
    """

    try:
        os.mkdir(path)
    except:
        pass
