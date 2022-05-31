# your User class goes here
class User:
    def __init__(self, name, email, dni, *other):
        self.name = name
        self.email = email
        self.dni = dni
        self.other=[other]
    def __str__(self):
        return f"User {self.name} added"
    
    
jose = User("Jose","jose@user.com","Z1235675H")
print(jose)
andres = User("Andres","Andres@user.com","Z1243475H")
print(andres)
carolina = User("Carolina","Carolina@user.com","Z12356454K")
print(carolina)
monica = User("Monica","monica@user.com","Z12353312G")
print(monica)
