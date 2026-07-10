# =====================================================================
# Assignment: Automated Text Sanitizer & Keyword Analyzer
# =====================================================================

# 1. Define a Target Keyword Set
# Hardcoded reference set of key industry tech terms
target_keywords = {"python", "ai", "robotics", "data", "automation", "learning"}

# 2. Input Text Processing
raw_text = input("Enter a paragraph or sentence to analyze:\n")

# Convert to lowercase and replace basic punctuation with spaces to avoid joining words
cleaned_text = raw_text.lower()
for punctuation in [".", ",", "!", "?", ";", ":", "-", "_"]:
    cleaned_text = cleaned_text.replace(punctuation, " ")

# 3. Deduplication via Sets
# Split into individual words, then cast to a set to instantly wipe out duplicates
word_list = cleaned_text.split()
unique_words = set(word_list)

# 4. Perform Collection Math (Set Operations)
# Find target keywords that the user actually mentioned
mentioned_keywords = target_keywords.intersection(unique_words)

# Find target keywords that were completely missing from the user's text
missing_keywords = target_keywords.difference(unique_words)

# 5. Output Summary Panel
dashboard = f"""
==================================================
           TEXT ANALYSIS DASHBOARD
==================================================
[Metrics Overview]
Total Raw Words Processed : {len(word_list)}
Total Unique Words Found  : {len(unique_words)}

[Keyword Matching Analytics]
Target Reference Keywords : {list(target_keywords)}
Matched Keywords (&)     : {list(mentioned_keywords) if mentioned_keywords else "None"}
Missing Keywords (-)     : {list(missing_keywords) if missing_keywords else "None"}
==================================================
"""

print(dashboard)