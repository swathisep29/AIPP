"""
Interactive Python demo that exercises core constructs:
- Class definition and methods
- Loops (for/while)
- Conditionals

Run: python main.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Person:
    name: str
    age: int

    def greet(self) -> str:
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

    def is_adult(self) -> bool:
        return self.age >= 18


def parse_numbers(csv: str) -> List[float]:
    parts = [p.strip() for p in csv.split(",") if p.strip()]
    numbers: List[float] = []
    for part in parts:
        try:
            numbers.append(float(part))
        except ValueError:
            # Skip invalid entries
            continue
    return numbers


def compute_statistics(numbers: List[float]) -> Dict[str, float]:
    if not numbers:
        return {
            "count": 0,
            "sum": 0.0,
            "mean": 0.0,
            "min": 0.0,
            "max": 0.0,
            "num_positive": 0,
            "num_negative": 0,
        }

    total = 0.0
    mn = numbers[0]
    mx = numbers[0]
    num_positive = 0
    num_negative = 0

    # for-loop with conditionals
    for value in numbers:
        total += value
        if value < mn:
            mn = value
        if value > mx:
            mx = value
        if value > 0:
            num_positive += 1
        elif value < 0:
            num_negative += 1

    mean = total / len(numbers)
    return {
        "count": len(numbers),
        "sum": total,
        "mean": mean,
        "min": mn,
        "max": mx,
        "num_positive": num_positive,
        "num_negative": num_negative,
    }


def countdown(start: int) -> List[int]:
    # while-loop example
    n = start
    seq: List[int] = []
    while n >= 0:
        seq.append(n)
        n -= 1
    return seq


def main() -> None:
    print("=== AI Autocomplete Exploration: Python Constructs ===")
    name = input("Enter your name: ").strip() or "Guest"

    age_str = input("Enter your age (integer): ").strip() or "0"
    try:
        age = int(age_str)
    except ValueError:
        age = 0

    user = Person(name=name, age=age)
    print(user.greet())
    print("Adult? ", "Yes" if user.is_adult() else "No")

    csv = input("Enter numbers (comma-separated): ")
    numbers = parse_numbers(csv)
    stats = compute_statistics(numbers)
    print("Numbers:", numbers)
    print("Stats:", stats)

    start_str = input("Countdown start (integer): ").strip() or "5"
    try:
        start = int(start_str)
    except ValueError:
        start = 5
    print("Countdown:", countdown(start))

    # Simple branching based on stats
    if stats["count"] == 0:
        print("No numbers provided. Try again with some input.")
    elif stats["mean"] > 100:
        print("High average detected.")
    else:
        print("Average is within a typical range.")


if __name__ == "__main__":
    main()


