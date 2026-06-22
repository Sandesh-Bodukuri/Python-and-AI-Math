#create a list from 0 to 10 which stores the cube values of each num in that list, using list comprehension.
cubes = [num**3 for num in range(0,11)]
print(cubes)

#list comprehension using condition
even_cubes = [num**3 for num in range(0,11) if num % 2 ==0]
print("The list of odd cubes from 0 to 10 :",even_cubes)
odd_cubes = [num**3 for num in range(0,11) if num % 2 == 1]
print("The list of odd cubes from 0 to 10 :",odd_cubes)

#using function in list comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    grid = [ [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n ]
    print(grid)
    