import requests
import os 

class yt_playlist():

    def __init__(self, playlist_url=None):
        self.playlist_url = playlist_url
        self._get_html()
        self._get_param()
     

    def get_urls(self):
        self.url_list = self._get_urls()
        new_url_list = []
        for i in self.url_list:
            new_url_list.append(f'https://www.youtube.com/watch?v={i}')
        return new_url_list


    def count_list(self):
        return len(self.url_list)


    def yt_url(self, playlist_url):
        self.playlist_url = playlist_url


    def _get_urls(self) -> list:
        init_ref = self.html_str[20].find(self.code_links)
        links = []
        
        for i in range(self.html_str[20].count(self.code_links)):
            links.append(self.html_str[20][init_ref - 24: init_ref - 13])
            init_ref = self.html_str[20].find(self.code_links, init_ref + 8)

        return links


    def _get_param(self):
        find_word = '],"params":"'
        with open('temp_file', 'r', encoding='utf-8') as f:
            self.html_str = f.readlines()
        
        init = self.html_str[20].find(find_word) + len(find_word)
        self.code_links = self.html_str[20][init:init+6]


    def _get_html(self):
        html = requests.get(self.playlist_url)
        with open('temp_file','w',encoding='utf-8') as f:
            for i in html.text:
                f.write(i)
    

    def __del__(self):
        os.remove('./temp_file')
        

if __name__ == '__main__':
    links = yt_playlist('https://www.youtube.com/playlist?list=PLuZo1HaJOTyz8LPb3X4AQHuku1qjoATZK')
    print(links.get_urls())
    print(links.count_list())