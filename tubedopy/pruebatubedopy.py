from pytube import YouTube as yt
from dependencies import directory_control as dc
from dependencies import yt_playlist as pl
import pytube
import os

class tubedopy():
    
    
    def __init__(self):
        dc().change_path()


    def check_url(self, url=None):
        pass


    def download_aud(self, url=None):
        
        stream = yt(url)
        audio = stream.streams.order_by('abr').last()
        audio.download()


    def convert_aud(self, url=None, ext=None):
        
        ext = '.mp3' if ext == None else ext
        
        if not dc().detect_os():
            ext = '.mp4'
        
        print(yt(url).title)
        # file_name = yt(url).title.replace((a for a in '\\/<>"?|*:'), '')
        # print(file_name)

    def get_linkpl(self, purl=None):
        pass


    def get_name(self):
        pass

if __name__ == '__main__':
    yolo = tubedopy()
    url = 'https://www.youtube.com/watch?v=l9_-2oG4Cc0'
    yolo.convert_aud(url)


