# Square Root Finder - Bisection Method ➗📐  

**Description:**  
In this project, I implemented the Bisection Method to approximate the square root 
of a number using Python. This classic numerical technique narrows down a 
range of possible values by repeatedly halving the interval until the solution is accurate enough.
It helped me understand how numerical methods can be applied to solve mathematical problems that don’t always have neat analytical solutions.  

## 🔥 What I Learned  
Through this project, I gained hands-on experience with:  
- ✅ **Numerical approximation** – using iteration to find precise values
- ✅ **The Bisection Method** – narrowing down intervals to converge on a result
- ✅ **Tolerance and precision** – defining acceptable error margins for floating-point math
- ✅ **Error handling** – managing invalid inputs like negative numbers

## 🛠 How It Works  
The program follows these steps:  
1️⃣ Ask for a number to find the square root of  
2️⃣ Set the initial search interval between 0 and the number (or 1 if it's < 1)  
3️⃣ Repeatedly check the midpoint of the interval  
4️⃣ If the square of the midpoint is close enough (within a small ```tolerance```), return the result  
5️⃣ Otherwise, adjust the interval and repeat  
6️⃣ If it doesn't converge within ```max_iterations```, notify the user  

## 🔢 Code Sample  
### Finding the Square Root of a Perfect Square

#### Input:
```
Enter a number to find the square root: 25
```
#### Output:
```
The square root of 25 is approximately 5.0
```

## 🎓 Credits
This project is part of the "Learn the Bisection Method by Finding the Square Root of a Number" course by freeCodeCamp. **[freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**.  
