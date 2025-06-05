# Arithmetic Formatter 🧮✨

**Description:**  
In this project, I built an Arithmetic Formatter in Python that arranges
basic arithmetic problems (addition and subtraction) vertically and side-by-side, 
mimicking the way students traditionally write them by hand. This project helped me 
sharpen my skills in string manipulation, input validation, and formatting logic. It gave 
me valuable experience in structuring clean, readable output while ensuring the program handles 
errors gracefully when given incorrectly formatted input.

## 🔥 What I Learned  
While working on this project, I strengthened my skills in:  
- ✅ **String formatting** and padding with `.rjust()`  
- ✅ **Input validation** with conditionals and `.isdigit()`  
- ✅ **Dynamic output layout** using Python lists and `.join()`  
- ✅ **Error handling** with descriptive return messages  
- ✅ **Optional parameters** with the `show_answers` flag  

## 🛠 How It Works  
The `arithmetic_arranger()` function takes two inputs:  
- A list of arithmetic problems (max 5)  
- An optional boolean `show_answers` to display the results

### It processes each problem by:  
1. Splitting into operands and operators  
2. Validating for:
   - Too many problems  
   - Unsupported operators (only `+` and `-` allowed)  
   - Non-digit characters in operands  
   - Operands longer than four digits  
3. Right-aligning operands and operators for vertical display  
4. Generating answer lines if `show_answers=True`  
5. Joining all parts with consistent spacing for a clean layout  

## 📌 Example Usage  

### Input:  
```python
arithmetic_arranger(["3801 - 2", "123 + 49"])
```
### Output:
```python
  3801      123
-    2    +  49
------    -----
```
### Input:  
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
### Output:
```python
   32         1      9999      523
+   8    - 3801    + 9999    -  49
-----    ------    ------    -----
   40     -3800     19998      474
```
## ⚠️ Error Handling
The function returns specific error messages for invalid inputs:
- Too many problems: 'Error: Too many problems.'
- Invalid operator: 'Error: Operator must be \'+\' or \'-\'.'
- Non-digit operand: 'Error: Numbers must only contain digits.'
- Operand too long: 'Error: Numbers cannot be more than four digits.'

## 🎓 Credits
This project is part of the "Build an Arithmetic Formatter Project" course by 
**[freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**.  
