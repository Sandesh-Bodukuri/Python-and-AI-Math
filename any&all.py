scores = [88, 92, 79, 95, 84]

# Check 1: Did EVERY student pass (score >= 70)?
all_passed = all(score >= 70 for score in scores)

# Check 2: Did ANY student score an A+ (score >= 95)?
has_top_performer = any(score >= 95 for score in scores)


print(f"All Passed? {all_passed}")             
print(f"Has Top Performer? {has_top_performer}") 