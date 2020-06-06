class Song:
    ''' Класс, содержащий информацию о треках'''
    def __init__(self, name, duration, artist, album, release_year, song_number, action=' Не воспроизводится'):
        self.name = name
        self.duration = duration
        self.artist = artist
        self.album = album
        self.release_year = release_year
        self.action = action
        self.song_number = song_number


    def action_song(self):
        if self.action == 'Не воспроизводится':
            self.action = 'Воспроизводится'
            return self.action
        elif self.action == 'Воспроизводится':
            self.action = 'Не воспроизводится'
            return self.action

    def pause(self):
        if self.action == 'Не Воспроизводится':
            self.action = 'Не Воспроизводится'
            return self.action
        elif self.action == 'Воспроизводится':
            self.action = 'Пауза'
            return self.action
        elif self.action == 'Пауза':
            self.action = 'Воспроизводится'
            return self.action

    def __str__(self):
        s = '#' + str(self.song_number) + '\n'
        s += 'Название альбома: ' + Album.__str__(self.album) + '\n'
        s += 'Название трека: ' + self.name + '\n'
        s += 'Длительность трека: ' + self.duration + '\n'
        s += 'Исполнитель: ' + self.artist + '\n'
        s += 'Год выпуска: ' + self.release_year + '\n'

        return s

    def __repr__(self):
        return self.__str__()



class Album:
    '''Класс, содержащий информацию об альбомах'''
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year
        self.songs = []


    def add_song(self, name, duration, artist, release_year):
        song_number = len(self.songs)
        song = Song(name, duration, artist, self, release_year, song_number)
        self.songs.append(song)

    def __str__(self):
        return self.name + ' ' + self.release_year

