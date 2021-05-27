# TubeDoPy 🎧🎵
Music Downloader from Youtube based in pytube library.

**PIP Packages**
```bash
  pip install pytube
  pip install requests
```

Tested in W10 and Ubuntu 20.04

Versions:
  - Python 3.9.0 
  - pytube 10.8.1
  - requests 2.25.1

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

Playlist doesn't work with playlist's made by youtube.
