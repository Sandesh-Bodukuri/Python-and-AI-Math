#create a list from 0 to 10 which stores the cube values of each num in that list, using list comprehension.
cubes = [num**3 for num in range(0,11)]
print(cubes)

#list comprehension using condition
even_cubes = [num**3 for num in range(0,11) if num % 2 ==0]
print(even_cubes)
odd_cubes = [num**3 for num in range(0,11) if num % 2 == 1]
print(odd_cubes)

#using function in list comprehension
