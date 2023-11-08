usernames = ["Taha", "Ahmed", "Abdelazim", "Hussein", "Admin"]

for username in usernames:
    if username == "Admin":
        print("Hello Admin, Would you like to see a status report?")
    else:
        print(f"Welcome {username}, Here is what you missed")
