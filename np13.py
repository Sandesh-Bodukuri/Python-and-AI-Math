import numpy as np

# 1. Counting Non-Zero Elements
sparse_vector = np.array([0, 5, 0, 12, 0, 0, 99, 3])

# Count elements that are not 0
non_zeros = np.count_nonzero(sparse_vector)
print(f"Total non-zero entries: {non_zeros}")

# 2. Counting Elements Matching a Condition
scores = np.array([45, 88, 72, 91, 55, 60, 38, 95])

# Pass a boolean condition directly into count_nonzero
passed_count = np.count_nonzero(scores >= 60)
print(f"Students with passing scores (>= 60): {passed_count}")

# 3. 2D Row/Column Counts (Using Axis)
# 3 students (rows) across 4 assignments (columns) where 0 = missing submission
submissions = np.array([
    [1, 1, 0, 1],  # Student 0 completed 3
    [1, 1, 1, 1],  # Student 1 completed 4
    [0, 1, 0, 0]   # Student 2 completed 1
])

# axis=1 counts non-zeros per student (across columns)
completed_per_student = np.count_nonzero(submissions, axis=1)

print("\nAssignments completed per student:", completed_per_student)