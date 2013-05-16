movie_1 = ('Iron Man 3', 78)
movie_2 = ('The Great Gatsby', 48)
movie_3 = ('Star Trek Into Darkness', 90)
movie_4 = ('Oblivion', 56)

movies = [movie_1, movie_2, movie_3, movie_4]





for scores in movies:
    movie_sentence = "{} is rated {} out of 100".format(scores[0],scores[1])
    print movie_sentence