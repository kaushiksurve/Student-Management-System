def validate_student_email(email):
    """Check whether a student email has a basic valid format."""
    if not isinstance(email, str) or not email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    username, domain = parts

    return bool(username and "." in domain and not domain.startswith(".") and not domain.endswith("."))


def main():
    email = "student@example.com"

    if validate_student_email(email):
        print("Valid student email")
    else:
        print("Invalid student email")


if __name__ == "__main__":
    main()
