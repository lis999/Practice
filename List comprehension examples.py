movies = ['Star Wars', 'Bob', 'Casandra', '911', 'Toy Story', 'Gatsby', 'Green Mile', 'Kill Bill']

g_movies = [title for title in movies if title.startswith('G')]
print(g_movies)
print('-'*100)
#

movies = [('Star Wars', 2002), ('Bob', 1999), ('Casandra', 1984), ('911', 2001), ('Toy Story', 2000), ('Gatsby', 2003),
          ('Green Mile', 1984), ('Kill Bill', 2000)]

movies_before_2000 = [title for (title, year) in movies if year < 2000]
print(movies_before_2000)
print('-'*100)
#

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)
