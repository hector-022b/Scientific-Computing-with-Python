# Case Converter - CamelCase to Snake_Case 🐫➡️🐍  

**Description:**  
 In this project, I built a Python program that converts strings from CamelCase or PascalCase into snake_case. It started with a traditional for loop solution to understand the logic step-by-step, and then I refactored it using list comprehension for a cleaner, more Pythonic approach. I used this project to get more comfortable with list comprehensions, how they work, when to use them, and how they can simplify my code by replacing verbose loops and conditionals.

## 🔥 What I Learned  
Through this project, I gained hands-on experience with:  
- ✅ List comprehension – constructing new lists from strings in a single line 
- ✅ String manipulation – identifying uppercase letters and inserting underscores  
- ✅ Iterables and conditions – using concise logic to transform data  

## 🛠 How It Works  
The converter operates in two phases:

1️⃣ Phase 1 – Using a for loop
- Loop through each character in the input string
- If the character is uppercase, insert an underscore and convert it to lowercase
- Combine and print the final string

2️⃣ Phase 2 – Using list comprehension
- Use a single line to apply the same logic
- Join the results into a final snake_case string

## 📌 Example Usage  
### Example Input and Output

#### Conversion 1
```
Input: Enter a CamelCase or PascalCase string: ConvertThisToSnake

Output: snake_case: convert_this_to_snake
```

#### Conversion 2
```
Input: Enter a CamelCase or PascalCase string: ListComprehensionRocks

Output: snake_case: list_comprehension_rocks

```

## 🎓 Credits
This project is part of the "Learn Python List Comprehension by Building a Case Converter Program" course by freeCodeCamp. **[freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**.  
