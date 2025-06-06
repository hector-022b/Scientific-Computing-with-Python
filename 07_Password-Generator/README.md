# 🔐 Password Generator - Regular Expressions

## Description

In this project, I built a **secure password generator** in Python
using modules from the standard library, such as `re`, `string`, and `secrets`. 
The generator creates strong, customizable passwords that meet specific complexity 
requirements using regular expressions to validate character composition.

---

## 🔍 What I Learned

Through this project, I gained hands-on experience with:

- ✅ **Regular Expressions** – pattern matching to enforce password rules  
- ✅ **Python Modules** – importing and utilizing `re`, `secrets`, and `string`  
- ✅ **Password Security** – generating cryptographically secure random passwords  
- ✅ **Constraint Validation** – ensuring output meets specified character requirements  

---

## ⚙️ How It Works

The password generator performs the following steps:

1. Accepts optional parameters for password length and minimum counts of:
   - Digits (`nums`)  
   - Special characters (`special_chars`)  
   - Uppercase letters (`uppercase`)  
   - Lowercase letters (`lowercase`)

2. Uses `secrets.choice()` to randomly assemble a password from:
   - Letters (`A-Z`, `a-z`)  
   - Digits (`0-9`)  
   - Symbols (e.g., `!@#$%^&*()`)

3. Uses `re.findall()` to match the generated password against the required character constraints.

4. Regenerates the password until all constraints are satisfied.

---

## 🧪 Example Output

```
Generated password: V9#t2pL!xN4@aBsY
```

This password:
- ✅ Is 16 characters long (default length)
- ✅ Includes **at least one digit** (`9`, `2`, `4`)
- ✅ Contains **special characters** (`#`, `!`, `@`)
- ✅ Has **uppercase letters** (`V`, `L`, `N`, `B`, `Y`)
- ✅ Includes **lowercase letters** (`t`, `p`, `x`, `a`, `s`)

Each time you run the script, a new secure password is generated that satisfies all the required constraints.

## 📦 Modules Used

- `secrets` – for cryptographic randomness
- `string` – for predefined character sets
- `re` – for regular expression pattern validation

## 🎓 Credits
This project is part of the "Learn Regular Expressions by Building a Password Generator" course by 
**[freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**.  
