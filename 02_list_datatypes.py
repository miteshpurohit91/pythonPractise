#List is Datatype allow multiple values with different Data type
values = [1,"Mitesh",3.5,4,5]
print(values)

# print values with index of list
print(values[3])

#Print last value of index
print(values[-1])

#insert value in list in between
values.insert(2,"Purohit")

# Append value at lat of list with append keyword
values.append(5)

# Update value at given index in List
values[2] = "PUROHIT"
print(values)

# TO remove value from List
del values[5]
print(values)
