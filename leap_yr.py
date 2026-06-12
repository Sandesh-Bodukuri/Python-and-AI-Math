def is_leap(year):
    leap = True
    not_leap = False
    
    if year % 4 == 0 :
        if year % 100 == 0 and not year % 400 == 0:
            return not_leap
        else :
               return leap    
    else :
        return not_leap
    
year = int(input())
print(is_leap(year))