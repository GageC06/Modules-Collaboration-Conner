class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user1 = User("Melissa", "Broyles")
user2 = User("Skyler", "Broyles")
user3 = User("Chasidee", "Broyles")
user4 = User("William", "Walker")
user5 = User("Angel", "Perez")

users = [user1, user2, user3, user4, user5]

for user in users:
    user.describe_user()
    user.greet_user()
