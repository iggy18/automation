from faker import Faker

fake = Faker("en_US")


def print_bs_article():
    content = ""
    for i in range(100):
        contents += fake.paragraph()
        contents += " " + fake.email() + " "
        contents += fake.sentence()
        contents += fake.phone_number()
        contents += fake.paragraph()
    print(content)


print_bs_article()

with open("potential-contacts.txt", "w") as f:
    f.write(potential_contacts)

with open("existing-contacts.txt", "w") as f:
    f.write(existing_contacts)
