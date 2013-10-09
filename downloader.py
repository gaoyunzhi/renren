# -*- coding: utf8 -*-
import sys, time, os, re
sys.path.append('../')
from douban.util import download_items, create_folder #@UnresolvedImport
from douban.downloader import Downloader as Down #@UnresolvedImport
from constant import INPUT_DIR, ALBUM_DIR, ALBUM_FILE, PHOTO_REG

class Downloader(Down):
    ''' renren downloader for albums saved in INPUT_DIR '''
    
    def __init__(self):
        self.albums_list = []
        self.filter = [] # empty filter matches all albums
    
    def auto(self):
        ''' automatically download all that matches filter '''
        self.__albums()
        for filename, album_name in self.albums_list:  
            album_name = album_name.decode('gb2312')    
            if not self.__match_filter('', album_name):
                continue
            print 'starting', album_name   
            album_folder = create_folder(ALBUM_DIR, album_name)
            self.__download(filename, album_folder)
        
    def __albums(self):
        ''' find all albums saved in INPUT_DIR '''
        self.albums_list = []
        for f in os.listdir(INPUT_DIR):
            match = re.match(ALBUM_FILE, f)
            if match:
                self.albums_list.append([os.path.join(INPUT_DIR, match.group(0)),
                                        match.group(1)])

    def __download(self, filename, album_folder):
        ''' download album in url to album_folder '''
        with open(filename) as f:
            content = f.read()
            photo_list = re.findall(PHOTO_REG, content)
        photo_list = [(match[2], match[0]) for match in photo_list]
        download_items(photo_list, album_folder)

if __name__ == "__main__":
    D = Downloader()
    # D.add_filter([u'汉族几千年或将被遗忘的古老习俗汇整'])
    D.auto()
    time.sleep(10) # give time to copy error message from terminal