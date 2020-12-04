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

with open("potential-contacts.txt", "w") as f:
    f.write(output)

with open("existing-contacts.txt", "w") as f:
    f.write(f"{print_bs_article()}")
