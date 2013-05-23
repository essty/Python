recent_movies = [('Iron Man 3', 78),
                 ('The Great Gatsby', 48),
                 ('Star Trek Into Darkness', 90),
                 ('Oblivion', 56)]
print "\n"

for movie, rating in recent_movies:
    if rating > int('75'):
        print "I watched {} the other day.".format(movie)
        print "It was awesome!!"
        print "\n"
    elif rating < int('50'):
        print "I watched {} the other day.".format(movie)
        print "This movie sucked!".format(movie)
        print "\n"
    else:
        print "I watched {} the other day.".format(movie)
        print "It was okay."
        print "\n"
