import re

def validate_email(email):
    # Define a regex pattern for email validation
    pattern = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+"
    # Use re.match() to find matches
    if re.match(pattern, email):
        return True
    else:
        return False


# Validate the input
if validate_email(user_input):
    print("Valid email address")
else:
    print("Invalid email address")
