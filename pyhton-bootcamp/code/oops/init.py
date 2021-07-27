class User:
    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age
        print(f"New user created {self.name}")
    
user1 = User("Sunil","Gaikwad",29)
user2 = User("Solo","Ronald", "28")

print(f"user1: {user1.name, user1.last, user1.age}")
print(f"user2: {user2.name, user2.last, user2.age}")
