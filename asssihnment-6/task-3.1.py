
"""Utility function for classifying a person's age into a group."""


def classify_age(age: int) -> str:
    """Return the age group label for a supplied age value.

    Classification:
        - age < 0: "Invalid age"
        - 0 <= age <= 12: "Child"
        - 13 <= age <= 17: "Teenager"
        - 18 <= age <= 64: "Adult"
        - age >= 65: "Senior"
    """

    if age < 0:
        return "Invalid age"
    if age <= 12:
        return "Child"
    if age <= 17:
        return "Teenager"
    if age <= 64:
        return "Adult"
    return "Senior"

