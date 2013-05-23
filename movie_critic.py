recent_movies = [('Iron Man 3', 78),
                 ('The Great Gatsby', 48),
                 ('Star Trek Into Darkness', 90),
                 ('Oblivion', 56)]
movie_stars = [('Leonardo DiCaprio', 'The Great Gatsby'),
               ('Tom Cruise', 'Oblivion'),
               ('Robert Downey Jr.', 'Iron Man 3'),
               (None, 'Star Trek Into Darkness')]

print "\n"

for movie, rating in recent_movies:
    if rating > int('75'):
        print "I watched {} the other day.".format(movie)
        print "It was awesome!!"
        print "Rotten Tomatoes agrees: they gave {} a score of {} out of 100".format(movie, rating)
        print "\n"
    elif rating < int('50'):
        print "I watched {} the other day.".format(movie)
        print "This movie sucked!".format(movie)
        print "Rotten Tomatoes agrees: they gave {} a score of {} out of 100".format(movie, rating)
        print "\n"
    else:
        print "I watched {} the other day.".format(movie)
        print "It was okay."
        print "Rotten Tomatoes agrees: they gave {} a score of {} out of 100".format(movie, rating)
        print "\n"