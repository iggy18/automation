with open("potential_contacts.txt", "r") as f:
    file = f.read()
    regex = "\w+(\.\w+)*@\w+\.\w+"

with open("potential_contacts.txt", "r") as f:
    file = f.read()
    regex = "\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}"
