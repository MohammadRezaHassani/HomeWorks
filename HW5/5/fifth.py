import pickle
from operator import attrgetter

#import User


class User:
    def __init__(self, id, first_name, last_name, phone):
        self.id = id
        self.first_name=first_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self):
        return f"{self.id} : {self.first_name}: {self.last_name} : <{self.phone}>"

    def ret_full_name(self):
        return f"{self.first_name} : {self.last_name}"




#unpickled List of users
user_list = pickle.load(open("users.pickled","rb"))

###########################################################
# sorted list of user
# new_list =sorted(user_list,key=attrgetter("id"))


# my_file=open("output-q-5-1.txt","ab")
# pickle.dump(new_list,my_file)
# my_file.close()


# my_file=open("output-q-5-1.txt","rb")
# obj1=pickle.load(my_file)
# print(obj1)

###################################################################################
#phone_list
# my_file=open("output-q-5-2.txt","ab")
# new_list=[i for i in user_list if i.phone.startswith("0919")]
# pickle.dump(new_list,my_file)
# my_file.close()


# my_file=open("output-q-5-2.txt","rb")
# obj1=pickle.load(my_file)
# print(obj1)

######################################################################################

# my_file=open("output-q-5-3.txt","ab")
# names_list=[]
# for i in user_list:
#     full_name=i.ret_full_name()
#     names_list.append(full_name)
#
# pickle.dump(names_list,my_file)
# my_file.close()
#
# my_file=open("output-q-5-3.txt","rb")
# obj1=pickle.load(my_file)
# print(obj1)




