class User:
    id = 0
    user_name: str
    phone: str
    email: str
    password: str
    user_list = []

    def __init__(self, user_name, phone, email, password,id=None):
        self.user_name = user_name
        self.phone = phone
        self.email = email
        self.password = password
        if id:
            self.id = id
        else:
            self.id = User.id
            User.id += 1
        User.user_list.append(self.__dict__)

    @classmethod
    def extract_user_by_dict(cls, user_dict):
        user_name = user_dict["user_name"]
        phone = user_dict["phone"]
        password = user_dict["password"]
        id = user_dict["id"]
        email = user_dict["email"]
        return cls(user_name=user_name, phone=phone, email=email, password=password, id=id)

    # for the user representation we use this function in order to show them
    def __str__(self):
        return f"""
detailed info for : {self.user_name:<20}  
     phone: {self.phone:<20}              
     email: {self.email:<20}              
     password: {self.password:<20}        
     id: {self.id:<20}                    
--------------------------------------    
        """


