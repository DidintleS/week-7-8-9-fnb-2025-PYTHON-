
fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)# Change the second element to "orange"
# This code prints the first element of the fruits list
fruits.insert(1, "orange")
print(fruits)

fruits.remove("kiwi")
print(fruits)  # This code prints the modified fruits list

fruits.sort(reverse=True)
print(fruits)  # This code prints the sorted fruits list