def is_valid_email(email):
    email_parts = email.split("@")
    if len(email_parts) <= 1:
        return False
    second_email_parts = email_parts[1].split(".")
    if len(second_email_parts) <= 1:
        return False
    username = email_parts[0]
    website = second_email_parts[0]
    extension = second_email_parts[1]
    username = username.replace("_", "")
    username = username.replace("-", "")
    if not username.isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3 or len(extension) < 1:
        return False
    return True


n = input()
n = int(n)

emails = []
for i in range(n):
    email = input()
    emails.append(email)

valid_emails = []
for email in emails:
    is_valid = is_valid_email(email)
    if is_valid:
        valid_emails.append(email)

valid_emails.sort()
print(f"Valid emails: {valid_emails}")

