numbers = [42, 7, 19, 7, 88, 3]
print("Original list:", numbers)


# 1. Searching and Counting
# count() finds duplicates, index() finds the first position of a value
seven_count = numbers.count(7)
index_of_88 = numbers.index(88)

print(f"Number 7 appears {seven_count} times.")
print(f"The number 88 is at index {index_of_88}.")



# 2. Sorting a List
# sort() modifies the original list; sorted() returns a new list without changing the original
numbers.sort()  # Sorts in ascending order
print("Sorted (ascending):", numbers)

numbers.sort(reverse=True)  # Sorts in descending order
print("Sorted (descending):", numbers)


# 3. Reversing a List
# reverse() flips the order of the elements in place
numbers.reverse()
print("Reversed list:", numbers)


# 4. Combining Lists (Concatenation & Extension)
list_a = [1, 2]
list_b = [3, 4]

# Method A: Using the '+' operator (creates a new list)
combined = list_a + list_b 

# Method B: Using extend() (modifies list_a in place)
list_a.extend(list_b) 

print("Combined with '+':", combined)
print("Extended list_a:", list_a)


# 5. List Comprehension (A powerful way to create/modify lists)
# Example: Create a new list with the squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares via list comprehension:", squares)


# 6. Clearing a List
# clear() removes all elements, leaving the list empty
numbers.clear()
print("After clear():", numbers)