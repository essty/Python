recent_movies = [('Iron Man 3', 78),
                 ('The Great Gatsby', 48),
                 ('Star Trek Into Darkness', 90),
                 ('Oblivion', 56)]
movie_stars = [('Leonardo DiCaprio', 'The Great Gatsby'),
               ('Tom Cruise', 'Oblivion'),
               ('Robert Downey Jr.', 'Iron Man 3'),
               (None, 'Star Trek Into Darkness')]

print "\n"

for i in recent_movies:
    if i[1] > int('75'):
        print "I watched {0} the other day.\nThis movie was awesome!!\nRotten Tomatoes agrees: they gave {0} a score of {1} out of 100".format(i[0],i[1])
        for actor, movie_name in movie_stars:
            if i[0] in movie_name:
                print "{} was pretty good in it, though.".format(actor)
        print "\n"
    elif i[1] < int('50'):
        print "I watched {0} the other day.\nThis movie sucked!\nRotten Tomatoes agrees: they gave {0} a score of {1} out of 100".format(i[0],i[1])
        for actor, movie_name in movie_stars:
            if i[0] in movie_name:
                print "{} was pretty good in it, though.".format(actor)
        print "\n"
    else:
        print "I watched {0} the other day.\nIt was okay.\nRotten Tomatoes agrees: they gave {0} a score of {1} out of 100".format(i[0],i[1])
        for actor, movie_name in movie_stars:
            if i[0] in movie_name:
                print "{} was pretty good in it, though.".format(actor)
        print "\n"