from faker import Faker

fake = Faker("en_US")


def print_bs_article():
    content = ""
    for i in range(100):
        content += fake.paragraph()
        content += " " + fake.email() + " "
        content += fake.sentence()
        content += fake.phone_number()
        content += fake.paragraph()
    return content


output = print_bs_article()

with open("potential_contacts_test.txt", "w") as f:
    f.write(output)

with open("existing_contacts_test.txt", "w") as f:
    f.write(output)
