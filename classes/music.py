import eyed3
import os
# audiofile = eyed3.load("song.mp3")
# audiofile.tag.artist = "Token Entry"
# audiofile.tag.album = "Free For All Comp LP"
# audiofile.tag.album_artist = "Various Artists"
# audiofile.tag.title = "The Edge"
# audiofile.tag.track_num = 3


class Music:
    def __init__(self, adress):
        self.music = eyed3.load(adress)
        self.title = self.music.tag.title
        self.artist = self.music.tag.artist
        self.album = self.music.tag.album
        self.covers = self.music.tag.images

    def save_cover(self, adress=""):
        if adress:
            tmp_address = os.getcwd()
            os.chdir(adress)
        try:
            for image in self.music.tag.images:
                if self.album is not None:
                    image_file = open("{0} - {1}({2}).jpg".format(self.artist, self.album, image.picture_type),"wb")
                else:
                    image_file = open("{0}({1}).jpg".format(self.artist, image.picture_type),"wb")

                image_file.write(image.image_data)
                image_file.close()
        except:
            print('Error in save cover')
        os.chdir(tmp_address)
    def __len__(self):
        return int(self.music.info.time_secs)

    def min_timing(self):
        x = self.music.info.time_secs
        min = int(x // 60)
        sec = int(x - (min * 60))
        return f'{min}:{sec}'

