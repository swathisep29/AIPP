def generate_assign_grade_test_cases():
    """
    Generate diverse test cases for assign_grade(score) covering:
    - All grade boundaries: F, D, C, B, A
    - Lower and upper edges of each range
    - Out-of-bound values
    - Invalid input types
    Returns a tuple: (valid_cases, invalid_cases)
    """
    valid_cases = [
        (100, "A"),             # upper boundary A
        (90, "A"),              # lower boundary A
        (95, "A"),              # mid A
        (89, "B"),              # upper boundary B
        (80, "B"),              # lower boundary B
        (85, "B"),              # mid B
        (79, "C"),              # upper boundary C
        (70, "C"),              # lower boundary C
        (75, "C"),              # mid C
        (69, "D"),              # upper boundary D
        (60, "D"),              # lower boundary D
        (65, "D"),              # mid D
        (59, "F"),              # upper boundary F
        (0, "F"),               # lower boundary F
        (30, "F"),              # mid F
    ]
    invalid_cases = [
        -1,                # negative number
        -5,                # further negative
        101,               # above upper bound
        105,               # well above valid
        "eighty",          # string input
        None,              # NoneType
        90.5,              # float input (if not allowed)
        [],                # empty list
        {},                # empty dict
    ]
    return valid_cases, invalid_cases


def print_assign_grade_test_cases():
    valid_cases, invalid_cases = generate_assign_grade_test_cases()
    print("Valid Test Cases (score, expected_grade):")
    for score, expected in valid_cases:
        print(f"  assign_grade({score}) => '{expected}'")
    print("\nInvalid Test Cases (score):")
    for score in invalid_cases:
        print(f"  assign_grade({repr(score)}) => Should raise error or return invalid/None")

# Example invocation
if __name__ == "__main__":
    print_assign_grade_test_cases()
