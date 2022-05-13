from classes.music import Music


def main():
    test = Music('music/test.mp3')
    test.save_cover('./cover')
    print(f'duration: {test.min_timing()}')
    print(f'artist: {test.artist}')
    print(f'title: {test.title}')


if __name__ == '__main__':
    main()

