def pass_is_strong(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in  '@#$%^&*'for char in password):
        return False
    return True

check=pass_is_strong("CHARACTER")
print(check)