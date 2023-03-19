# TubeDoPy 🎧🎵
<h1 align="center">
  <br>
  <a><img src="https://raw.githubusercontent.com/Mitzuka/Images/master/Tubedopy.png?token=GHSAT0AAAAAAB74BPW6WP44SB3KI2ZH2AQGZAQZHQQ" width="500"></a>
  <br>
</h1>
Music Downloader from Youtube based in pytube library.

**PIP Packages**
```bash
  pip install pytube
  pip install requests
```

The program also needs the framework "ffmpeg", you can download in the next link:
    https://ffmpeg.org/download.html

**IMPORTANT**

You need add the directory of the framework to the PATH system.
If you don't know how to do this, follow the next links:

Windows: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10
 <br>&emsp;&nbsp;&nbsp;&nbsp;Linux: https://phoenixnap.com/kb/linux-add-to-path</br>


Tested in W10 and Ubuntu 20.04


Versions:
  - Python 3.11.2 
  - pytube 12.1.2
  - requests 2.28.2


Quickstart

Only the basic use appears here.

```python
>>> from tubedopy import tubedopy
>>> tdp = tubedopy()
>>> link = 'https://www.youtube.com/watch?v=0BIaDVnYp2A'
>>> playlist = 'https://www.youtube.com/playlist?list=PL6k57M9aVcIIARkqPG06AapxZ99yqepds'
>>> tdp.download_aud(url=link)           # Get the audio and puts the files in $ ~/Music/tubedopy
>>> tdp.change_ext(url=link, ext='mp3')  # Changes the original ext(.webm) for the chosen ext
>>> play_list = get_purls(purl=playlist) # Returns a list with all the links of the playlist
>>>
>>> for urls in play_list:
...     tdp.download_aud(url=urls)
...     tdp.chang_ext(url=urls, ext='mp3')
```

Also you can give an url to the file "tubedopy.py" as parameter in the console to download the music.

    C:\"random_path">python tubedopy -pl https://www.youtube.com/playlist?list=PLuZo1HaJOTyxRuytW8jXJK78eXaug5fut

The file "tubedopy.py" receive the parameters -pl and -l for the playlist or single song, respectively.
