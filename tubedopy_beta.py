from pytube import YouTube as yt
from pytube.contrib.playlist import Playlist as pl
import pytube
import os

'''
    Autor: Mithzuka (Daniel Velazquez)
    Nombre: TubeDoPy
    Version: Beta 1.4.0.2127
    Fecha salida: 31/01/2021
    Para SO: Windows 10

    Actualmente el programa esta hecho para descargar unicamente audio en la mejor calidad
    posible y de YouTube solamente.
    Para poder usar bien este programa necesitas las 
    siguientes librerias:
                          - pip install pytube
                          - pip3 install --upgrade google-api-python-client
                            (En este link explica el uso y como conseguir la clave*: 
                            https://stackoverflow.com/questions/62345198/extract-individual-links-from-a-single-youtube-playlist-link-using-python)

    

    Cualquier duda o comentario favor de mandarlo a mi correo 'govetzka@gmail.com'.
    
    * La clave es necesaria para que el programa pueda funcionar correctamente.

    Recuerda: Si te gusta la app y quieres que siga mejorandola no olvides donar. 
              Si te gusta lo que descargas apoyalos comprando su contenido oficial.
'''




class tubedopy():

    '''
        Empieza ubicando la carpeta (C:/Users/NOMBREUSUARIO/Music/TubeDoPy)
        y la toma de base para guardar los archivos descargados.        
    '''

    def __init__(self):
        
        self.path = os.path.expanduser('~').replace('\\', '/')
        self.path += '/Music/TubeDoPy'

        while True:
            try:
                os.chdir(self.path)
                break
            except FileNotFoundError:
                os.mkdir(self.path)
        
    def comprobar_url(self, url=None):

        '''
            Verifica si la url de una playlist o un video independiente.
        '''

        self.url = url

        if '&list' in url:
            try:
                self.plist = pl(self.url)
                return True
            except:
                return 'Error: Url no valido'
        else:
            try:
                self.list = yt(self.url)
                return True
            except pytube.exceptions.RegexMatchError:
                return 'Error: URL no valido'
    
    def download_aud(self, ref_url=None):
        '''
            Escoge la mejor calidad de audio y la descarga.
        '''
        try:
            self.ref_url = ref_url
            stream = yt(self.ref_url)
            self.audio = stream.streams.order_by('abr').last()
            self.audio.download()
        except:
            return 'Error: URL no valido'

    def convert_aud(self, aud_ext=None):

        '''
            Cambia la extencion del archivo a mp3
        '''

        self.aud_ext = yt(aud_ext).title

        for a in '\\/<>"?|*:':
            self.aud_ext = self.aud_ext.replace(a, '')

        self.act_ext = ''
        self.new_ext = self.aud_ext
        self.new_ext += '.mp3'

        for entry in os.scandir():
            if not entry.name.startswith('.') and entry.is_file():
                if self.aud_ext in entry.name:
                    self.act_ext = entry.name
                    break

        os.replace(self.act_ext, self.new_ext)

    def get_linkpl(self, ref_purl=None):
        '''
            Extrae los links de una playlist y los retorna en una lista.
        '''
        pass

        

        
            
    def get_name(self, link_vid=None):

        '''
            Retorna el nombre del video.
        '''

        self.link_vid = link_vid
        title = yt(self.link_vid)
        return title.title 
