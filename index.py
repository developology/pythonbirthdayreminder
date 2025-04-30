Employee = {
    "Riddhi": {
        "DOB": "16/01/04",
        "Email": "riddhiagrawal734@gmail.com"
    },
    "John": {
        "DOB": "06/02/99",
        "Email": "john@gmail.com"
    }
}

TodaysDate = input("Enter today's date (DD/MM/YY): ")

found = False
for name, details in Employee.items():
    if details["DOB"] == TodaysDate:
        found = True
        print(f"🎉 Happy Birthday, {name}!")
        print(f"📧 Email to: {details['Email']}")
        print(f"Subject: Happy Birthday {name}!\nBody: Wishing you a fantastic year ahead!\n")

if not found:
    print("No birthdays today.")

