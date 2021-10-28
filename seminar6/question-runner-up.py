l = [12, 23, 32, 12, 23, 56, 32, 56, 22, 87]

uniques = list(set(l))

# sort in desending order and get second element
# uniques.sort(reverse=True)
# print(uniques[1])

# sort in ascending element and get second to last element
uniques.sort()
print(uniques[-2])