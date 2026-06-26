dictionary_01 = {"Seeta": "Raama", "Raadha":"Krishna", "Parvati":"Shiva"}
view = dictionary_01.keys()
view_1 = dictionary_01.values()
view_2 = dictionary_01.items()
print(view)
print(view_1)
print(view_2)

a = dictionary_01.get("Saraswati")
print(a)
b = dictionary_01.setdefault("Saraswati", None)
print(b)
print(f"Saraswati gets added as key with a default value 'none', due to the usage of .setdefault")
print(dictionary_01)

dictionary_01.update({"Saraswati": "Brahma"})
print(dictionary_01)

