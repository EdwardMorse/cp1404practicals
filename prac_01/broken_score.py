"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid. Your score must be between 0 and 100")
    score = float(input("Enter score: "))
if score >= 90:
    category = "Excellent"
elif score >= 50:
    category = "Passable"
else:
    category = "Bad"
print(f"Your score of {score:.2f} is {category}")
