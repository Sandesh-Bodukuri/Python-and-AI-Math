import numpy as np

# Student IDs and their final composite scores
student_ids = np.array(["ID_101", "ID_102", "ID_103", "ID_104", "ID_105"])
scores = np.array([72.5, 95.0, 61.0, 88.5, 91.0])

# 1. Full Ranking with np.argsort()

# Get indices in ascending order: [2, 0, 3, 4, 1]
sort_indices = np.argsort(scores)

# Reverse slice [::-1] to get descending order (highest score first)
rank_indices = sort_indices[::-1]

print("Leaderboard Ranking:")
for rank, idx in enumerate(rank_indices, start=1):
    print(f"Rank {rank}: {student_ids[idx]} with score {scores[idx]}")