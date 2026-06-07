username={
    "aynan" : "aynan123",
    "john" : "john123",
    "jane" : "jane123"
}
print("Enter your username:")
user_input = input()

print("Enter your password:")
password_input = input()    

if user_input in username and username[user_input] == password_input:
    print("Login successful!") 
else:    print("Login failed! Invalid username or password.")

total_attempts = 3
attempts = 0    
while attempts < total_attempts:
    print("Enter your username:")
    user_input = input()

    print("Enter your password:")
    password_input = input()    

    if user_input in username and username[user_input] == password_input:
        print("Login successful!") 
        break
    else:    
        print("Login failed! Invalid username or password.")
        attempts += 1
if attempts == total_attempts:
    print("Too many failed attempts. Account locked.")