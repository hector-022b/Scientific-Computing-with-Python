# python_LuhnAlgorithm

# Luhn Algorithm - Credit Card Validator 💳🚀

**Description:**  
This project implements the Luhn Algorithm, a widely used method for validating credit card numbers. It's a simple yet powerful error-checking technique used by banks and payment processors to detect typos and invalid card numbers.



## 🔥 What I Learned
Through this project, I gained hands-on experience with:
- ✅ String manipulation – slicing, reversing, and processing characters
- ✅ Numerical computations – summing digits and applying mathematical operations
- ✅ Algorithmic thinking – understanding real-world applications of validation algorithms  


## 🛠 How It Works
The Luhn Algorithm follows these steps:
- 1️⃣ Reverse the card number
- 2️⃣ Extract odd and even-positioned digits
- 3️⃣ Double every second digit and sum the digits if needed
- 4️⃣ Add all digits together
- 5️⃣ Check if the total is a multiple of 10 (valid card number)  

## 📌 Example Usage
```
card_number = "4111-1111-4555-1142"
is_valid = verify_card_number(card_number)
print(is_valid)  # Output: True or False
```

## 🎓 Credits
This project is part of the "Learn How to Work with Numbers and Strings" course by freeCodeCamp. **[freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**.  

