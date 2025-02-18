import zipfile
import timeit
import sys
import socket
import os

def crack(dictionary_attack, zFile, filename):
    """
    Attempts to crack the password of a ZIP file using a dictionary attack.

    :param dictionary_attack: Path to the dictionary file containing potential passwords.
    :param zFile: The ZIP file object to be cracked.
    :param filename: The name of the ZIP file for logging purposes.
    """
    attempts = 0
    found_password = None

    with open(dictionary_attack, 'r') as wordlist:
        print("Started cracking password...")

        for line in wordlist:
            passwd = line.strip('\n')
            attempts += 1

            try:
                zFile.extractall(pwd=str.encode(passwd))
            except (RuntimeError, zipfile.BadZipFile):
                continue  # Ignore incorrect passwords
            else:
                found_password = passwd
                print(f"Password brute-forced: {found_password}")
                break

        print(f"Attempted {attempts} passwords from {filename}")

        if found_password is None:
            print(f"Password not found in {filename}")

def main_brute_force():
    """
    Main function to execute the password cracking process.
    """
    file_name = input("Enter ZIP file name: ")
    dictionary_name = input("Enter dictionary file name: ")

    # Validate file existence
    if not os.path.isfile(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    if not os.path.isfile(dictionary_name):
        print(f"Error: The dictionary file '{dictionary_name}' does not exist.")
        return

    try:
        zip_file = zipfile.ZipFile(file_name)
    except zipfile.BadZipFile:
        print(f"Error: The file '{file_name}' is not a valid ZIP file.")
        return

    start = timeit.default_timer()
    crack(dictionary_name, zip_file, file_name)
    stop = timeit.default_timer()

    print(f"Cracked password in {stop - start:.2f} seconds")

def scanHost(ip, startPort, endPort):
    """ Starts a TCP scan on a given IP address """
    print(f'[*] Starting TCP port scan on host {ip}')
    tcp_scan(ip, startPort, endPort)
    print(f'[+] TCP scan on host {ip} complete')

def scanRange(network, startPort, endPort):
    """ Starts a TCP scan on a given IP address range """
    print(f'[*] Starting TCP port scan on network {network}.0')

    # Iterate over a range of host IP addresses and scan each target
    for host in range(1, 255):
        ip = f'{network}.{host}'
        tcp_scan(ip, startPort, endPort)

    print(f'[+] TCP scan on network {network}.0 complete')

def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """
    for port in range(startPort, endPort + 1):
        try:
            # Create a new socket
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(0.01)  # Set a timeout for the connection attempt
            
            # Print if the port is open
            if not tcp.connect_ex((ip, port)):
                print(f'[+] {ip}:{port}/TCP Open')
            tcp.close()
            
        except socket.error as e:
            print(f'[-] Error connecting to {ip}:{port} - {e}')
            continue

def main_port_scanner():
    """ Main function to execute the port scanning process. """
    if len(sys.argv) < 4:
        print('Usage: python penetration_toolkit.py <IP address or network> <start port> <end port> [-n]')
        print('Example: python penetration_toolkit.py 192.168.1.10 1 65535\n')
        print('Usage: python penetration_toolkit.py <network> <start port> <end port> -n')
        print('Example: python penetration_toolkit.py 192.168.1 1 65535 -n')
        sys.exit(1)

    network = sys.argv[1]
    startPort = int(sys.argv[2])
    endPort = int(sys.argv[3])

    if len(sys.argv) == 5 and sys.argv[4] == '-n':
        scanRange(network, startPort, endPort)
    else:
        scanHost(network, startPort, endPort)

if __name__ == "__main__":
    choice = input("Choose an option:\n1. Brute Force ZIP Password Cracker\n2. TCP Port Scanner\nEnter 1 or 2: ")

    if choice == '1':
        main_brute_force()
    elif choice == '2':
        main_port_scanner()
    else:
        print("Invalid choice. Please select either 1 or 2.")
