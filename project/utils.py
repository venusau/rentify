# backend/utils.py
def validate_email(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    import re
    return re.match(r"^\+?[1-9]\d{1,14}$", phone)
