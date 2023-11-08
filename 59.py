usernames = ["Taha", "Ahmed", "Abdelazim", "Hussein", "Admin"]
# usernames = []
if usernames:        
    for username in usernames:
        if username == "Admin":
            print("Hello Admin, Would you like to see a status report?")
        else:
            print(f"Welcome {username}, Here is what you missed")
else:
    print("We need to find some users!")r