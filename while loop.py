correct_password="Shweta@123"
password=input("Enter password:")
while password!=correct_password:
    password = input("Wrong Password!Enter Again:")
print("Logged in")