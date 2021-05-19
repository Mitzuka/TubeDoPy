import os

class directory_control():

    def __init__(self):
        self.windows = self._detect_os()


    def _detect_os(self):
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
            self.path = '~/Music/TubeDoPy'
            while True:
                if os.system(f'cd {self.path}') != 512:
                    break
                os.system(f'mkdir {self.path}')
                    

if __name__ == '__main__':
    ref = directory_control()
    ref.change_path()
