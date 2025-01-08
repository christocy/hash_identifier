# hash_identifier

## Overview
This tool is a Python-based hash identifier that helps you identify the type of hash used in a given string. It supports a wide range of hash algorithms and works interactively, allowing you to test multiple hashes without restarting the script.

---
## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/christocy/hash_identifier.git
   cd hash_identifier
   ```

2. Make the script executable:
   ```bash
   chmod +x hash_identifier.py
   ```

---

## Usage
1. Run the script:
   ```bash
   ./hash_identifier.py
   ```

2. Enter the hash you want to identify when prompted. Example:
   ```
   Enter the hash (or type 'kill' to exit): 5d41402abc4b2a76b9719d911017c592
   Hash Type: MD5
   ```

3. To exit the tool, type `kill`:
   ```
   Enter the hash (or type 'kill' to exit): kill
   Tool terminated.
   ```
---

## Supported Hashes
The tool supports the following hash types:
- **MD5**
- **SHA (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512)**
- **SHA3 (SHA3-224, SHA3-256, SHA3-384, SHA3-512)**
- **NTLM**
- **bcrypt**
- **MySQL (MySQL, MySQL5, MySQL160)**
- **MSSQL (MSSQL2000, MSSQL2005)**
- **PostgreSQL**
- **Oracle (10g, 11g)**
- **DES**
- **WPA/WPA2**
- **RIPEMD**
- **GOST**
- **Whirlpool**
- **Tiger**
- **Haval**

---

## Requirements
- Python 3.6 or later

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.



