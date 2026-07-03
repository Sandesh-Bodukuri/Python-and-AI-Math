gradebook = {
    "STU01": {"name": "Ananya", "scores": [85, 92, 88]},
    "STU02": {"name": "Rohan", "scores": [70, 78, 65]}
}

#adding  a dict using variable
new_std = {"name": "Aditi", "scores": [95, 97, 99]}
gradebook["STU03"] = new_std

#adding a dict using .update
gradebook.update({"STU04": {"name": "Reyansh", "scores": [80,78,91]}})

# updating list inside dictionary
gradebook["STU01"]["scores"].append(95)
First_student = gradebook.get("STU01")

# step 4: safe lookup with .get()
student = gradebook.get("STU99")
if student is None:
    print("Student STU99 not found.")
else:
    print(f"Found student: {student['name']}")

# step 5: calculate averages and print dashboard
for student_id, profile in gradebook.items():
    scores = profile["scores"]
    average = sum(scores) / len(scores)
    print(
        f"ID: {student_id} | Name: {profile['name']} | "
        f"Scores: {scores} | Average: {average:.2f}"
    )