# password_checker.py
pw = input("Enter password: ")
print("Length:", len(pw))
if len(pw) < 8:
    print("Weak: less than 8 chars")
else:
    print("OK: consider adding numbers & symbols")
