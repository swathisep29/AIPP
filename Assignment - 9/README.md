# Python Programming Assignment: Student Class & Calculator Module

This project contains two Python programs demonstrating the use of:
- Classes and object-oriented programming
- Arithmetic functions with NumPy-style docstrings
- Comparison between manual and AI-generated comments/docstrings

---

## 📘 1️⃣ Student Class Program

### ✅ Features:
- Defines a `Student` class with:
  - `name`, `roll_no`, and `hostel_status` attributes
  - Fee assignment based on hostel status
  - `fee_update()` method to update the fee
  - `display_details()` method to print student information
- Manual comments and AI-generated comments included for comparison
- Interactive user input demonstration

### 🎯 Learning Outcome:
Shows how different styles of code comments affect clarity and usefulness for readers and developers.

---

## 🧮 2️⃣ Calculator Module Program

### ✅ Features:
- Includes four arithmetic functions:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
  - `divide(a, b)`
- Each function uses **NumPy-style docstrings**
- Manual and AI-generated docstrings are both included
- Comparison of manual vs. AI-generated documentation style
- Demo section using user input

### ✍️ Docstring Comparison Summary:
| Aspect | Manual Docstrings | AI Docstrings |
|--------|------------------|---------------|
| Examples Provided | ✅ | ❌ |
| Detailed Explanation | ✅ | ✅ (less detailed) |
| Educational Value | ✅✅✅ | ✅✅ |
| Clarity of Edge Cases | ✅ | ⚠️ sometimes |
| Brevity | ⚠️ | ✅✅✅ |

📌 *Conclusion:*  
Manual docstrings are more helpful for learning due to examples and clearer parameter descriptions. AI-generated ones are concise but sometimes lack context.

---

## 📂 Project Structure
```
├── student_program.py         # Student class with manual & AI comments
├── calculator_module.py       # Arithmetic module with two docstring styles
└── README.md                  # Project documentation (this file)
```

---

## 🚀 How to Run

1. Make sure Python 3.x is installed.
2. Save the programs in the same folder.
3. Run individually in the terminal or IDE:

```bash
python student_program.py
python calculator_module.py
```

---

## ✅ Final Notes

This assignment demonstrates:
- Importance of comments and documentation in software development
- Difference in detail and clarity between human-written and AI-generated documentation
- Practical implementation using Python functions and classes

If needed, further improvements can include:
- Type hints for all functions and parameters
- Automated unit testing (`pytest` / `unittest`)

---

📌 *Prepared for academic submission: includes explanation, demonstration, and comparison.*

