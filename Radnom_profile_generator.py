from faker import Faker
fake = Faker()

print("------------------ User Information: ------------------")
print("Full name: ", fake.name())
print("Age: ", fake.random_int(min=18, max=99))
print("Address: ", fake.address())
print("City: ", fake.city())
print("Country: ", fake.country() )
print("Phone: ", fake.phone_number())
print("Email: ", fake.email())

