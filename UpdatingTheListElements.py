Updating = ['Mahadi', 'John', 'Ton', 3.1416, 22]
# set OR Updating the Elements
Updating[0] = 'Sagor'
print(Updating)
Updating[1] = 'Hasan'
print(Updating)

# Inserting the Elements
#  1. Use of append()
# append () is  add elements of the list for last item

Inserting = [50, 40, 30, 'Abir', 'Mahbub']
Inserting.append('Tonny')
print(Inserting)
# Output is
# [50, 40, 30, 'Abir', 'Mahbub', 'Tonny']


#  2. use of insert ()
# insert () is add elements of list where u set

Inserting.insert(2, 'Tahsin')
print(Inserting)

# Output is
# [50, 40, 'Tahsin', 30, 'Abir', 'Mahbub', 'Tonny']

Inserting.extend('Sumaiya''Sadia''Akbor')
print(Inserting)
# output is
# [50, 40, 'Tahsin', 30, 'Abir', 'Mahbub', 'Tonny', 'S', 'u', 'm', 'a', 'i', 'y', 'a', 'S', 'a', 'd', 'i', 'a', 'A', 'k', 'b', 'o', 'r']
