class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name=first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f"{self.id} : {self.first_name}: {self.last_name} : <{self.phone}>"

