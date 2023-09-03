# WAP to create a "login_required" decorator which if added to a function asks for a password. If the
# password is entered "123" then the function can be accessed else throw the message "Invalid Password"

def login_required(func):
    def inner_fxn(*args, **kwargs):
        password = input("Enter your password: ")
        if password == "123":
            return func(*args, **kwargs)
        else:
            return"Invalid password"
    return inner_fxn


@login_required
def addition(a, b):
    return a + b


result = addition(2, 3)
print(result)