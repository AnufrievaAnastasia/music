from main import *
print('Программа позволяет получить информацию о музыкальном альбоме \n'
      'Если вы хотите остановить запись, введите:  "EXIT" \n'
      'Вводите данные по образцу:\n'
      'Название альбома, год релиза')

key = True
while key:
    try:
        name, release_year = input('Введите данные о музыкальном альбоме  \n').split(',')
        info = Album(name, release_year)
        while key:
            try:
                name, duration, artist, release_year = input('Введите данные о песне  \n').split(',')
                info.add_song(name, duration, artist, release_year)
                my_file = open("information.txt", "a")
                my_file.write(str(info.songs))
            except ValueError:
                print('Запись завершена.')
                key = False

    except ValueError:
        print('Запись завершена.')
        key = False

