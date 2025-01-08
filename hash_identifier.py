#!/usr/bin/env python3

import re
import sys

# Extended hash patterns dictionary
hash_patterns = {
    "MD5": r"^[a-f0-9]{32}$",
    "SHA-1": r"^[a-f0-9]{40}$",
    "SHA-224": r"^[a-f0-9]{56}$",
    "SHA-256": r"^[a-f0-9]{64}$",
    "SHA-384": r"^[a-f0-9]{96}$",
    "SHA-512": r"^[a-f0-9]{128}$",
    "SHA3-224": r"^[a-f0-9]{56}$",
    "SHA3-256": r"^[a-f0-9]{64}$",
    "SHA3-384": r"^[a-f0-9]{96}$",
    "SHA3-512": r"^[a-f0-9]{128}$",
    "NTLM": r"^[a-f0-9]{32}$",
    "LM": r"^[a-f0-9]{32}$",
    "CRC32": r"^[a-f0-9]{8}$",
    "bcrypt": r"^\$2[aby]?\$\d{2}\$[./A-Za-z0-9]{53}$",
    "MySQL": r"^[a-f0-9]{16}$",
    "MySQL5": r"^[a-f0-9]{40}$",
    "MySQL160": r"^[a-f0-9]{64}$",
    "MSSQL2000": r"^0x[a-f0-9]{8}$",
    "MSSQL2005": r"^0x0100[a-f0-9]{80}$",
    "PostgreSQL": r"^[a-f0-9]{32}$",
    "Oracle 10g": r"^S:[A-Z0-9]{60}$",
    "Oracle 11g": r"^[a-f0-9]{64}$",
    "DES": r"^.{13}$",
    "Blowfish(Eggdrop)": r"^\+[a-zA-Z0-9\/\.]{12}$",
    "WPA/WPA2": r"^[a-f0-9]{64}$",
    "RIPEMD-128": r"^[a-f0-9]{32}$",
    "RIPEMD-160": r"^[a-f0-9]{40}$",
    "RIPEMD-256": r"^[a-f0-9]{64}$",
    "RIPEMD-320": r"^[a-f0-9]{80}$",
    "GOST R 34.11-94": r"^[a-f0-9]{64}$",
    "GOST R 34.11-2012": r"^[a-f0-9]{64}$",
    "Snefru-128": r"^[a-f0-9]{32}$",
    "Snefru-256": r"^[a-f0-9]{64}$",
    "Whirlpool": r"^[a-f0-9]{128}$",
    "Tiger-128": r"^[a-f0-9]{32}$",
    "Tiger-160": r"^[a-f0-9]{40}$",
    "Tiger-192": r"^[a-f0-9]{48}$",
    "Haval-128": r"^[a-f0-9]{32}$",
    "Haval-160": r"^[a-f0-9]{40}$",
    "Haval-192": r"^[a-f0-9]{48}$",
    "Haval-224": r"^[a-f0-9]{56}$",
    "Haval-256": r"^[a-f0-9]{64}$",
}

def identify_hash(hash_value):
    for hash_type, pattern in hash_patterns.items():
        if re.match(pattern, hash_value, re.IGNORECASE):
            return hash_type
    return "Unknown hash type"

def main():
    while True:
        # Prompt user for input
        hash_input = input("\nEnter the hash (or type 'kill' to exit): ").strip()
        
        # Check for "kill" command
        if hash_input.lower() == "kill":
            print("Tool terminated.")
            sys.exit()

        # Identify the hash type
        result = identify_hash(hash_input)
        print(f"Hash Type: {result}")

if __name__ == "__main__":
    main()
