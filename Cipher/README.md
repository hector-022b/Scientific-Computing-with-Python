# Cipher - String Manipulation & Encryption 🔐  

**Description:**  
This project focuses on learning string manipulation by building a simple cipher for encoding and decoding messages. Ciphers are widely used in cryptography to secure communication by transforming text into unreadable formats.  

## 🔥 What I Learned  
Through this project, I gained hands-on experience with:  
- ✅ **String manipulation** – slicing, replacing, and shifting characters  
- ✅ **Encryption basics** – encoding and decoding messages  
- ✅ **Algorithmic thinking** – applying logic to secure data transmission  

## 🛠 How It Works  
The cipher follows these steps:  
1️⃣ Accept user input (message and shift value)  
2️⃣ Shift each letter by the specified number of positions in the alphabet  
3️⃣ Maintain the case of letters (uppercase/lowercase)  
4️⃣ Return the encrypted or decrypted message  

## 📌 Example Usage  
```python
message = "Hello, World!"
shift = 3
encoded = encrypt_message(message, shift)
print(encoded)  # Output: "Khoor, Zruog!"
