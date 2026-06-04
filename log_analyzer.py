import re
import os


def extract_errors(logfile):
    return re.findall(r"ERROR.*", logfile)


def extract_ips(logfile):
    return re.findall(r"\d+\.\d+\.\d+\.\d+", logfile)


def extract_warnings(logfile):
    return re.findall(r"WARNING.*", logfile)


def extract_emails(logfile):
    return re.findall(r"\w+@\w+\.\w+", logfile)


def extract_admin_email(logfile):
    return re.findall(r"admin@\w+\.\w+", logfile)


# Ask user for file path
filepath = input("Enter log file path: ")

# Check if file exists
if not os.path.exists(filepath):
    print("Error: File not found!")
    exit()

# Read logfile
with open(filepath, "r") as file:
    logfile = file.read()
    print(logfile)

# Menu
while True:
    print("\n===== LOG ANALYZER =====")
    print("1. Show all IP addresses")
    print("2. Show all ERROR lines")
    print("3. Show all WARNING lines")
    print("4. Show all emails")
    print("5. Show admin email")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        ips = extract_ips(logfile)

        if ips:
            print("\nIP Addresses Found:")
            for ip in ips:
                print(ip)
        else:
            print("No IP addresses found.")

    elif choice == "2":
        errors = extract_errors(logfile)

        if errors:
            print("\nError Lines Found:")
            for error in errors:
                print(error)
        else:
            print("No errors found.")

    elif choice == "3":
        warnings = extract_warnings(logfile)

        if warnings:
            print("\nWarning Lines Found:")
            for warning in warnings:
                print(warning)
        else:
            print("No warnings found.")

    elif choice == "4":
        emails = extract_emails(logfile)

        if emails:
            print("\nEmails Found:")
            for email in emails:
                print(email)
        else:
            print("No emails found.")

    elif choice == "5":
        admin_emails = extract_admin_email(logfile)

        if admin_emails:
            print("\nAdmin Email:")
            for email in admin_emails:
                print(email)
        else:
            print("No admin email found.")

    elif choice == "6":
        print("Exiting Log Analyzer...")
        break

    else:
        print("Invalid choice. Please try again.")