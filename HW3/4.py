class BankDataBase:
    banks =dict()

    @classmethod
    def add_banks(cls,bank):
        cls.banks[bank.name] =bank

    @classmethod
    def search_back(cls,name):
        return cls.banks[name]


class Bank:
    def __init__(self,name):
        self.name =name
        self.__accounts =dict()
        BankDataBase.add_banks(self)

    def add_account(self,account):
        self.__accounts[account.serial] = account

    def get_account(self,serial):
        return self.__accounts.get(serial)


class Transaction:

    def __init__(self,source_serial,type,value,bank,destination_serial=None):
        self.type =type
        self.bank =bank
        self.source_serial =source_serial
        self.destination_serial =destination_serial
        self.value =value

    def do_transaction(self):
        if self.type == "in":
            self.transaction_validate()
        elif self.type =="out":
            self.transaction_validate()
        else:
            self.transaction_validate()

    def transaction_validate(self):
        in_acc = self.bank.get_account(self.source_serial)
        out_acc = self.bank.get_account(self.destination_serial)

        if self.type == "transfer":
            if not in_acc or \
                    not out_acc:
                print("Wrong Serial Input")
            else:
                in_ = self.bank.get_account(self.source_serial)
                out_ = self.bank.get_account(self.destination_serial)
                in_.acc_transaction(self)
        else:
            print(in_acc)
            if not in_acc :
                print("Wrong Serial Input")
            else:
                in_ = self.bank.get_account(self.source_serial)
                in_.acc_transaction(self)


class BankAccount:

    def __init__(self,serial,bankname):
        self.serial = serial
        self.bankname = bankname
        self.__name =""
        self.__account_blance =0
        self.__leas_account_balance =10000
        self.__account_passowrd =""


    def bank_validate(self):
        if not BankDataBase.banks.get(self.bankname):
            print("The Bank do not Exist")
            return False
        return True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, usrname):
        self.__name = usrname

    @property
    def acc_balance(self):
        return self.__account_blance

    @acc_balance.setter
    def acc_balance(self,value):
        if value<0 :
            print("Error : Negetive Initial Balance ")
        else:
            self.__account_blance = value

    def transaction(self):
        type = input("Enter your favourite Transaction: \n1_ in\n2_ out\n3_ transfer\nType: ")
        value = int(input("Enter Value: "))
        out_serial = None
        if type =="transfer":
            out_serial = int(input("destination_serial: "))
        t1 = Transaction(value=value,type=type,source_serial=self.serial,
        destination_serial=out_serial,bank=BankDataBase.search_back(self.bankname))
        t1.do_transaction()

    @property
    def acc_pass(self):
        return

    @acc_pass.setter
    def acc_pass(self,value):
            self.__account_passowrd = value



    def acc_transaction(self,transaction):
       self.__validate_transaction(transaction)


    def __validate_transaction(self,transaction):
        if transaction.type =="in":
            self.__account_blance += transaction.value

        else:
            if self.__account_blance - transaction.value \
             < self.__leas_account_balance :
                print("Not enough Balance")
            else:
                self.__account_blance -= transaction.value
                if transaction.type == "transfer":
                   out_acc = BankDataBase.banks.get(self.bankname).get_account(transaction.destination_serial)
                   transaction.type ="in"
                   out_acc.acc_transaction(transaction)
                else:
                    pass

    def register(self):
        print(f"----Welcome To {self.bankname}------")
        print("     |Register Page|    \n")
        self.name = input("Enter your Name : ")
        self.acc_balance = int(input("Enter your Account_Balance :"))
        self.acc_pass =int(input("Enter your password: "))
        BankDataBase.search_back(self.bankname).add_account(self)



#------------------------------Main_Program------------------------------------#


Bank = Bank("Meli")
bank_account1 = BankAccount(87492874298, "Meli")
bank_account1.register()
bank_account2 = BankAccount(874928783, "Meli")
bank_account2.register()
bank_account1.transaction()
print(bank_account1.acc_balance,bank_account2.acc_balance)



















