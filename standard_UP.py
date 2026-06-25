#Data Packing
def pack(*nums):
    for x in nums:
        print(f'packing:{x}')
    print(f'Packed: {nums}')
pack(1,2,3)

#Unpacking
def unpack(a,b,c):
    print('Unpacking')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
num = [1,2,3]
unpack(*num)


#Dictionary issue
def packdict(**nums):
    print(f"nums = {nums}")
    for k in nums :
     print(f'Packed: {k} = {nums[k] }')

packdict(name= 'Seeta' , age=47, pet='Dog')

#Unpacking Dictionary
def unpackdict(name,age,pet) :
   print('Unpacked Dictionary')
   print(f'Name ={name}')
   print(f'Age = {age}')
   print(f'Pet = {pet}')

d = dict(name= 'Rama', age =46, pet='Dog')
unpackdict(**d)