from pytube import YouTube as yt
from dependencies import directory_control as dc
from dependencies import yt_playlist as pl
import concurrent.futures
import pytube
import sys
import os

class tubedopy():
    
    
    def __init__(self):

        # This line creates the directory "TubeDoPy" in C:/Users/%USERNAME%/Music
        # After that, change the path to download in that directory.

        dc().change_path()


    def check_url(self, url=None):

        return yt(url).check_availability()



    def download_aud(self, url=None):
        
        stream = yt(url)
        audio = stream.streams.order_by('abr').last()
        audio.download()



    def aud_convert(self, name=None, ext=None, rem_file=False):

        # Start a search in the current path to seek the recently download
        # then calls the framework from console to convert the ".webm" file.

        file_name = name
        ext = '.mp3' if ext == None else ext

        for a in '\\/<>"?|*:;.\'':
            file_name = file_name.replace(a , '')
       
        for entry in os.scandir():
            if not entry.name.startswith('.') and entry.is_file():
                print(f"file_name={file_name} entry_name={entry.name}")
                if file_name in entry.name:
                    os.system(f'ffmpeg -i "{entry.name}" -vn -y "{file_name+ext}" -loglevel error')
                    os.system('del /A:- "*.webm" "*.mp4"') if rem_file else None
                    break



    def get_purls(self, purl=None):

        # Obtains the url's and create an file to 
        # save them temporaly.

        return pl(purl).get_urls()


    def get_title(self, url=None):
        return yt(url).title


if __name__ == '__main__':

    import logging
    import argparse


    tdp = tubedopy()
    remove_bool = False


    def __check_command():

        # Read the command line if the script was called in a command shell.


        parser = argparse.ArgumentParser(prog='TubeDoPy')
        parser.add_argument("-pl", "--playlist", default=None, help="To download the playlist from the link")
        parser.add_argument("-l", "--link", default=None, help="Download the link's song")
        parser.add_argument("-r", "--replace", action=argparse.BooleanOptionalAction, help="Removes the video format when the convertion is done")
        args = parser.parse_args()
    
        if args.replace:
            remove_bool = True

        if args.playlist:
            __multi_download(args.playlist)

        if args.link:
            
            song_name = tdp.get_title(args.link)

            try:
                tdp.download_aud(args.link)
            except:
                print(f'Failed to download')
                os._exit()
            print('Download Complete\nStarting convertion...')
            tdp.aud_convert( name=song_name, rem_file=remove_bool )
            print('Downloaded succesfully!')


    def __multi_download(purl=None):

        # Starts a download of a playlist with 5 threads.
        
        urls_list = tdp.get_purls(purl)

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_download = {executor.submit(__down_convert, url): url for url in urls_list}


    def __down_convert(url=None):

        song_name = tdp.get_title(url)

        try:
            tdp.download_aud(url)
        except:
            print(f'Failed to download -> {song_name}')
            return
        print('Download Complete\nStarting convertion...')
        tdp.aud_convert( name=song_name, rem_file=remove_bool )
        print(f'{song_name} Downloaded succesfully!')


    __check_command()
