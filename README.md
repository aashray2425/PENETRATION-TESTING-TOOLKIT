# PENETRATION-TESTING-TOOLKIT

COMPANY: CODTECH IT SOLUTIONS

NAME: Aashray Premkumar Dhone

INTERN ID: CODHC173

DOMAIN: Cyber Security & Ethical Hacking

BATCH DURATION: January 30th, 2025 to March 2nd, 2025

MENTOR NAME: Neela Santhosh Kumar

This Python script provides two functionalities: Brute Force ZIP Password Cracker: Uses a dictionary attack to attempt password cracking on a ZIP file.

TCP Port Scanner: Scans a given host or network for open TCP ports.

Features ZIP Password Cracker: Reads a list of possible passwords from a dictionary file.

Attempts to extract the ZIP file with each password.

Stops when the correct password is found or when the list is exhausted.

OutPut : ![Screenshot 2025-01-30 161009](https://github.com/user-attachments/assets/60fb0c0d-6bf4-4179-9ad2-cc6d92f9b553)

![Screenshot 2025-01-30 161055](https://github.com/user-attachments/assets/f9df30ec-6d32-4bdd-819a-e5c5eda49260)

TCP Port Scanner: Scans a single host or an entire network for open ports.

Uses socket programming to establish TCP connections.

Reports open ports within a specified range.

Requirements Ensure you have Python installed along with the following modules:

zipfile

timeit

sys

socket

os

No external libraries are required.

Usage Running the Script Run the script using the command:

python penetration_toolkit.py

The script will prompt you to choose between the ZIP password cracker and the TCP port scanner.

ZIP Password Cracker When prompted, enter 1 to use the ZIP password cracker.

Choose an option: Brute Force ZIP Password Cracker TCP Port Scanner Enter 1 or 2: 1 Then, provide the path to the ZIP file and the dictionary file.

Example: Enter ZIP file name: secret.zip Enter dictionary file name: wordlist.txt

The script will attempt to crack the password using the given wordlist.

TCP Port Scanner To scan a host for open ports, choose 2 when prompted:

Choose an option:

Brute Force ZIP Password Cracker TCP Port Scanner Enter 1 or 2: 2 Then, run the script with the required parameters:

python penetration_toolkit.py [-n]

Examples: python penetration_toolkit.py 192.168.1.10 1 65535 python penetration_toolkit.py 192.168.1 1 65535 -n

The first example scans a single host.

The second example scans an entire network (-n flag for network scanning).

Notes The ZIP password cracker relies on a dictionary file. A strong, well-curated wordlist increases the chances of success.

The TCP port scanner may take time to complete depending on the port range and network latency.

Ensure you have permission before scanning any network or cracking any files.

Disclaimer This tool is intended for educational and authorized security testing purposes only. Unauthorized use may violate legal and ethical guidelines.
