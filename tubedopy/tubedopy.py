from pytube import YouTube as yt
from dependencies import directory_control as dc
from dependencies import yt_playlist as pl
import pytube
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


    def convert_aud(self, url=None, ext=None):

        file_name = yt(url).title
        ext = '.mp4' if ext == None else ext

        for a in '\\/<>"?|*:':
            file_name = file_name.replace(a , '')
       
        for entry in os.scandir():
            if not entry.name.startswith('.') and entry.is_file():
                if file_name in entry.name:
                    os.replace(entry.name, f'{file_name}{ext}')
                    break


    def get_purls(self, purl=None):
        return pl(purl).get_urls()


    def get_name(self, url=None):
        return yt(url).title

if __name__ == '__main__':
    import time
    yolo = tubedopy()
    url = 'https://www.youtube.com/watch?v=DH4vLA-6AkI'
    purl = 'https://www.youtube.com/playlist?list=PLuZo1HaJOTyzjiYG0dq-RXA7fhTqd64j3'
    yolo.download_aud(url)
    yolo.convert_aud(url)
    # yolo.check_url(url)
    '''
    start = time.time()
    ars = yolo.get_purls(purl)[72:]
    for urls in ars:
        try:
            yolo.download_aud(urls)
        except:
            print(f'No se pudo descargar la cancion {yolo.get_name(urls)}.')
            continue
        print(f'La cancion {yolo.get_name(urls)} se descargo correctamente')
        yolo.convert_aud(urls)
        print(f'La cancion {yolo.get_name(urls)} se convirtio correctamente')
    
    end = time.time()
    print('Descarga completa')
    print(f'Tiempo de descarga -> {end - start}')
    '''
