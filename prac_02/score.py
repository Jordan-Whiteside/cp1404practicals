"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
from random import randint

def main():
    """Get user score and display status. Then display result of random score."""
    score = int(input("Enter score: "))
    score_status = determine_score_result(score)
    print(score_status)
    random_score_status = determine_score_result((randint(0,100)))
    print(random_score_status)


def determine_score_result(score):
    """Determine score status."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    else:
        return "Bad"



