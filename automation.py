import re

with open("potential_contacts.txt", "r") as f:
    emails_in_file = f.read()
    regex = r"\w+(\.\w+)*@\w+\.\w+"
    email = re.findall(regex, emails_in_file)
    sorted_email = email.sort()
    print(email)


with open("potential_contacts.txt", "r") as f:
    phone_numbers_in_file = f.read()
    regex = r"\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}"
    phone_numbers = re.findall(regex, phone_numbers_in_file)
    sorted_phone_numbers = phone_numbers.sort()
    print(phone_numbers)