import os

class directory_control():

    def __init__(self):
        self.windows = self.detect_os()


    def detect_os(self):
        return os.name == 'nt'
    

    def change_path(self):
        if self.windows:
            self.path = os.path.expanduser('~').replace('\\', '/')
            self.path += '/Music/TubeDoPy'

            while True:
                try:
                    os.chdir(self.path)
                    break
                except FileNotFoundError:
                    os.mkdir(self.path)
        else:
            self.path = os.path.expanduser('~')
            self.path += '/Music/TubeDoPy'

            while True:
                try:
                    os.chdir(self.path)
                    break
                except FileNotFoundError:
                    os.system(f'mkdir {self.path}')
