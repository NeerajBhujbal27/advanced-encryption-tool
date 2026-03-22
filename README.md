# 🔐 Advanced Encryption Tool (AES-256)

## 📌 Project Overview
The Advanced Encryption Tool is a Python-based application designed to securely encrypt and decrypt files using strong cryptographic techniques. It utilizes modern encryption standards to protect sensitive data and demonstrates practical implementation of file security. This project is developed as part of a Cyber Security Internship Task (Task 4).

## 🎯 Objective
To design and implement a tool that:
- Encrypts files using advanced encryption techniques  
- Decrypts encrypted files securely  
- Ensures data confidentiality and integrity  
- Demonstrates practical usage of cryptography in cybersecurity  

## 🛠️ Technologies Used
- Python 3  
- cryptography library (Fernet – AES-256 based encryption)  
- os module for file handling  

## ⚙️ Features
- Encrypts files securely using AES-based encryption  
- Decrypts encrypted files back to original form  
- Generates and stores a secure encryption key  
- Simple command-line interface  
- Error handling for reliable execution  
- Lightweight and easy to use  

## 📂 Project Structure
advanced-encryption-tool/  
├── encryption_tool.py   # Main Python script  
├── secret.key           # Encryption key (generated at runtime)  
└── README.md            # Project documentation  

## ▶️ How to Run the Project
Step 1: Clone the Repository  
git clone https://github.com/your-username/advanced-encryption-tool.git  

Step 2: Navigate to the Project Directory  
cd advanced-encryption-tool  

Step 3: Install Required Library  
pip install cryptography  

Step 4: Run the Program  
python encryption_tool.py  

Step 5: Choose Operation  
1. Generate Key  
2. Encrypt File  
3. Decrypt File  

## 🧪 Sample Usage

### Generate Key
[INFO] Key generated and saved as secret.key  

### Encrypt File
Enter file path: test.txt  
[SUCCESS] File encrypted: test.txt.enc  

### Decrypt File
Enter file path: test.txt.enc  
[SUCCESS] File decrypted: test.txt  

## 🔍 How It Works
The tool generates a secure encryption key and uses it to encrypt file data. The encrypted data is stored in a new file with a .enc extension. During decryption, the same key is used to restore the original file content.

## 📌 Use Cases
- Protecting sensitive files  
- Secure file storage  
- Learning cryptographic concepts  
- Basic data security implementation  

## ⚠️ Important Notes
- Keep the secret.key file safe  
- Without the key, encrypted files cannot be decrypted  
- Do not share your encryption key publicly  

## 🚀 Future Enhancements
- GUI-based interface  
- Password-based key generation  
- Support for multiple encryption algorithms  
- File selection using file explorer  
- Batch file encryption  

## 👨‍💻 Author
Neeraj Bhujbal   

## 📎 Submission Note
This project is submitted as part of the Cyber Security Internship Task (Task 4), following the provided instructions and guidelines.