# 1. Input Collection
coding_score = float(input("Enter applicant's Coding Score (0-100): "))
experience = int(input("Enter Years of Professional Experience: "))
knows_python_input = input("Whether you have python knowledge or not? (yes/no): ").strip().lower()

# Correct Boolean Mapping
knows_python = knows_python_input in ["yes", "y", "true"]

# 2. Boundary Validation
if coding_score < 0 or coding_score > 100 or experience < 0:
    print("\n[ERROR]: Invalid input metrics.")
    exit()

# 3. Tiered Evaluation Logic
status = ""

if coding_score >= 90 and experience >= 3:
    status = "DIRECT INTERVIEW: ELITE TRACK"

elif coding_score >= 75 or (experience >= 5 and coding_score >= 60):
    if knows_python:
        status = "TECHNICAL INTERVIEW REQUIRED (PYTHON)"
    else:
        status = "HOLD: Requires Python Foundations Check"

elif coding_score >= 50:
    # If knows_python is False, 'not knows_python' is True -> triggers the correct status string
    status = "python course required" if not knows_python else "HOLD: Technical Review Queue"

else:
    status = "APPLICATION UNSUCCESSFUL"

# 4. Print Dashboard Panel
print("\n" + "=" * 50)
print(f" SYSTEM DECISION       : {status}")
print("=" * 50 + "\n")
print("             EVALUATION REPORT              ")

print(f" Applicant Coding Score : {coding_score:.1f}/100")
print(f" Industry Experience   : {experience} Years")
print(f" Core Python Stack     : {'PASSED' if knows_python_input else 'FAILED'}")

print(f" SYSTEM DECISION       : {status}")






        
        