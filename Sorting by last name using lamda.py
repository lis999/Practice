scifi_authors = ['Ray Bradbury', 'H. G. Wells', 'Robert Heinlein', 'Isaac Asimov', 'Arthur C. Clarke']
print(scifi_authors)

scifi_authors.sort(key = lambda name: name.split(' ')[-1].lower())

print(scifi_authors)