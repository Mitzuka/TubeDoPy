from pytube import YouTube as yt
from dependencies import directory_control as dc
from dependencies import yt_playlist as pl
import concurrent.futures
import pytube
import sys
import os

class tubedopy():
    
    
    def __init__(self):
        dc().change_path()


    def check_url(self, url=None):
        return yt(url).check_availability()


    def download_aud(self, url=None):
        
        stream = yt(url)
        audio = stream.streams.order_by('abr').last()
        audio.download()


    def aud_convert(self, url=None, ext=None):

        file_name = yt(url).title
        ext = '.mp3' if ext == None else ext

        for a in '\\/<>"?|*:':
            file_name = file_name.replace(a , '')
       
        for entry in os.scandir():
            if not entry.name.startswith('.') and entry.is_file():
                if file_name in entry.name:
                    os.system(f'ffmpeg -i "{entry.name}" -vn -y "{file_name+ext}" -loglevel error')
                    break


    def get_purls(self, purl=None):
        return pl(purl).get_urls()


    def get_title(self, url=None):
        return yt(url).title


if __name__ == '__main__':

    import logging
    import argparse

    tdp = tubedopy()

    def __check_command():
        parser = argparse.ArgumentParser(prog='TubeDoPy')
        parser.add_argument("-pl", "--playlist", default=None, help="To download the playlist from the link")
        parser.add_argument("-l", "--link", default=None, help="Download the link's song")
        args = parser.parse_args()
    
        if args.playlist:
            __multi_download(args.playlist)
        if args.link:
            try:
                tdp.download_aud(args.link)
            except:
                print(f'Failed to download')
                os._exit()
            print('Download Complete\nStarting convertion...')
            tdp.aud_convert(args.link)
            print('Downloaded succesfully!')


    def __multi_download(purl=None):
        
        urls_list = tdp.get_purls(purl)

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_download = {executor.submit(__down_convert, url): url for url in urls_list}


    def __down_convert(url=None):
        try:
            tdp.download_aud(url)
        except:
            print(f'Failed to download -> {tdp.get_name(url)}')
            return
        print('Download Complete\nStarting convertion...')
        tdp.aud_convert(url)
        print(f'{tdp.get_name(url)} Downloaded succesfully!')


    __check_command()
