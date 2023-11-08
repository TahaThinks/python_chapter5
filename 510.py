current_users = ["taha", "ahmed", "abdelazim", "hussein"]
new_users = ["andrew", "karim", "minem", "Ahmed", "Hussein"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry '{new_user}' is taken, try again with another username")
    else:
        print(f"This username is available")
