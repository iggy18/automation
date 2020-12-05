import re


def emails(file_to_be_written_to):
    with open("potential_contacts.txt", "r") as f:
        emails_in_file = f.read()
        regex = r"\w+@\w+\.\w+"
        email = re.findall(regex, emails_in_file)
        email.sort()

    with open(file_to_be_written_to, "w") as f:
        for contact in email:
            f.write(contact + "\n")


def numbers(file_to_be_written_to):
    with open("potential_contacts.txt", "r") as f:
        phone_numbers_in_file = f.read()
        regex = r"\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}"
        phone_numbers = re.findall(regex, phone_numbers_in_file)
        phone_numbers.replace("(", "")
        phone_numbers.sort()

    with open(file_to_be_written_to, "w") as f:
        for contact in phone_numbers:
            f.write(contact + "\n")


if __name__ == "__main__":
    emails("email.txt")
    numbers("numbers.txt")
