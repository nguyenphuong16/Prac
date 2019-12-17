"""
Replace the contents of this module docstring with your own details
Name: Vu Le Nguyen Phuong
Date started: 15/8/2019
GitHub URL: https://github.com/nguyenphuong16/CP1404.git
"""

fp = open('movies.csv', 'r')
movies = []
count = 0
for line in fp.readlines():
    line = line.strip()
    movies.append(line.split(','))
    count += 1
print("Movies To Watch 1.0-by <Vu Le Nguyen Phuong>")
print(count, "movies loaded")
fp.close()
while True:
    print("Menu:")
    print("L - List movies")
    print("A - Add new movie")
    print("W - Watch a movie")
    print("Q - Quit")
    option = input(">>>")
    option = option.lower()  # To make case-insensitive

    if option == 'l':
        watched = 0
        remain = 0
        for index, movie in enumerate(movies):
            print(str(index) + '. ' + ' '.join([str(item) for item in movie]))
            if movie[0] == '':
                watched += 1
            else:
                remain += 1
        print(watched, 'movies watched,', remain, 'movies still to watch')

    elif option == 'w':
        remain = 0
        for movie in movies:
            if movie[0] == '*':
                remain += 1
        if remain == 0:
            print('No more movies to watch!')
            continue
        print("Enter the number of a movie to mark as watched")
        while True:
            number = input(">>>")
            try:
                number = int(number)
            except:
                print('Invalid input; enter a valid number')
                continue
            if number < 0:
                print("Number must be >= 0")

            elif number > len(movies):
                print('Invalid movie number')
            elif movies[number][0] == '':
                print('You have already watched', movies[number][1])
                break
            else:
                print(movies[number][1], 'from', movies[number][2], 'watched')
                movies[number][0] = ''
                break
    elif option == 'a':
        title = ''
        while True:
            title = input('Title:')
            if title != '':
                break
            print('Input can not be blank')
        old = ''
        while True:
            old = input('Year: ')
            try:
                old = int(old)
            except:
                print('Invalid input; enter a valid number')
                continue
            if old < 0:
                print('Number must be >= 0')
            else:
                break
        category = ''
        while True:
            category = input('Category:')
            if category != '':
                break
            print('Input can not be blank')
        newItem = ['*', title, old, '(' + category + ')']
        indexToAdd = 0
        for movie in movies:
            if movie[2] > old:
                break
            indexToAdd += 1
        movies = movies[:indexToAdd] + [newItem] + movies[indexToAdd:]
        print(title, '(', category, 'from', old, ')added to movie list')
    elif option == 'q':
        fp = open('movies.csv', 'w')
        for movie in movies:
            fp.write(','.join([str(item) for item in movie]) + '\n')
        print(len(movies), 'movies saved to movies.csv')
        print('Have a nice day :)')
        break
    else:
        print('Invalid menu choice')