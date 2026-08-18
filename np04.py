import numpy as np

# Student exam scores across 3 subjects (Rows: Students, Columns: Math, Science, English)
scores = np.array([
    [78, 85, 92],
    [45, 52, 60],
    [88, 91, 79],
    [30, 48, 55]
])

# ---------------------------------------------------------------------
# 1. Column-wise Normalization via Broadcasting
# Formula: (x - min) / (max - min)
# ---------------------------------------------------------------------
col_min = scores.min(axis=0)  # [30, 48, 55]
col_max = scores.max(axis=0)  # [88, 91, 92]

# Broadcasts (4, 3) with (3,) automatically without loops
normalized = (scores - col_min) / (col_max - col_min)

print("Normalized Scores (0.0 to 1.0):\n", np.round(normalized, 2))


# ---------------------------------------------------------------------
# 2. Vectorized Conditional Replacement (np.where)
# Flag passing grades (>= 60) vs failing grades (< 60)
# ---------------------------------------------------------------------
status = np.where(scores >= 60, "Pass", "Fail")

print("\nStudent Status Matrix:\n", status)


# ---------------------------------------------------------------------
# 3. Fast Boolean Aggregations (np.any / np.all)
# ---------------------------------------------------------------------
# Did any student fail all 3 subjects?
failed_all = np.all(scores < 60, axis=1)
print("\nStudents who failed all exams:", np.where(failed_all)[0])