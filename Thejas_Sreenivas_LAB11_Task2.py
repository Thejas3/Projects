class EmailFormatError(Exception):
    pass


def is_valid_email(email):
    try:
        username, domain = email.split('@')
        if not username[0].isalpha():
            raise EmailFormatError("Username must start with a letter")
        if not domain.endswith("student.gsu.edu"):
            raise EmailFormatError("Domain must end with 'student.gsu.edu'")
    except ValueError:
        raise EmailFormatError("Please enter a valid email address.")
    except EmailFormatError as e:
        print("Error:", e)
        return False
    return True


# Test the function
email1 = "example@student.gsu.edu"
email2 = "123@example.com"
email3 = "invalidemail@student.gsu.edu"

print(is_valid_email(email1))  # Should print True
print(is_valid_email(email2))  # Should print False and raise EmailFormatError
print(is_valid_email(email3))  # Should print False and raise EmailFormatError
