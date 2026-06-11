U_name = (str(input("Enter the User name with a space between first name and last name only, use single space:")))
S_Id = (str(input("Enter the Student ID along with birth year with a space(eg: 3816 2005) :")))


U_name = U_name.strip().lower().split()

S_Id = S_Id.strip().split()

first_name = U_name[0]  
last_name =  U_name[1]
birth_year = S_Id[1]
first_initial = first_name[0] 

UserName = first_initial + last_name + birth_year
Password = last_name[::-1] + "@123"

print("     ACCOUNT REGISTRATION SUMMARY     ")
print(f"Sanitized First Name : {first_name.capitalize()}")
print(f"Sanitized Last Name  : {last_name.capitalize()}")
print(f"Extracted Year       : {birth_year}")
print(f"Generated Username   : {UserName}")
print(f"Temporary Password   : {Password}")
