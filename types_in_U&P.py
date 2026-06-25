# 1. Standard unpacking
record = ("Alice", 28, "Engineer")
name, age, role = record
print(f"name = {name}")
print(f"age = {age}")
print(f"role = {role}")

# 2. Extended Unpacking (Catch-all)
sensor_data = [98.6, 98.7, 99.1, 100.2, 101.5]
first_reading, *middle_readings, last_reading = sensor_data

print(f"first_reading = {first_reading}")
print(f"middle_readings = {middle_readings}")
print(f"last_reading = {last_reading}")

# 3. Nested Unpacking
matrix_shape = (256, (1080, 1920))
channels, (height, width) = matrix_shape

print(f"channels = {channels}")
print(f"height = {height}")
print(f"width = {width}")
