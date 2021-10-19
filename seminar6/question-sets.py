n_plants = input("Please insert the number of plants: ")
n_plants = int(n_plants)

# input of n_plants height
heights = input(f"Please enter {n_plants} heights: ")

# convert input to a list of strings by spliting the string on " "
heights = heights.split(" ")

# convert each input into an integer by casting the value using int()
for i in range(0, n_plants):
    heights[i] = int(heights[i])

# remove duplicated values by turning the list into a set using set()
unique_heights = set(heights)

# compute the average height of the plants by summing the values in 
#   my set and dividing by the number of elements in the set
total_unique_height = 0 
for h in unique_heights:
    total_unique_height = total_unique_height + h # s += h
average_unique_height = total_unique_height / len(unique_heights)

print(f"Average unique height: {average_unique_height}")