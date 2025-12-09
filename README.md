# Directory Brute Forcer (Python)

A simple Python script for brute forcing website directories using a wordlist.  
Useful for penetration testing, CTF challenges, or learning basic web enumeration techniques.

---

## 🚀 Features
- Reads directory names from a wordlist
- Checks each path on a target server
- Detects valid directories via status codes (200, 301, 302, 403)
- Handles connection errors and timeouts gracefully

---

## 📦 Requirements
Install dependencies:

```bash
pip install requests
