import numpy as np
a = np.array([1,2,3,4])
b = np.arange(4)
c = np.arange(1,9,3)
print(a)
print(b)
print(c)
#evenly spaced elements within a given range, ex: 5 evenly spaced ele from 0 to 100
d = np.linspace(1,100,5)
print(d)
d_int = np.linspace(1,100,5, dtype=int)# to get integers
print(d_int)
#character array
char_arr = np.array(['Welcome to Math for ML!'])
print(char_arr)