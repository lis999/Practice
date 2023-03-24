# Extract duplicate words from the given list

lst = "My name is Anton I am living in San Jose My name is Anton"
new_lst = lst.split()
duplicates = []
for word in new_lst:
    if new_lst.count(word) > 1:
        if word not in duplicates:
            duplicates.append(word)
print(duplicates)