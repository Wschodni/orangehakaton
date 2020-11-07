class Date:
    __day = 0
    __month = 0
    __year = 0

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def PrintDate(self):
        print(self.__day, ' ', self.__month, ' ', self.__year, ' ')


class Person:
    name = ""
    surname = ""

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Beneficiary(Person):
    accountNumber = ""

    def __init__(self, name, surname, accountNumber):
        self.name = name
        self.surname = surname
        self.accountNumber = accountNumber


class User(Person):
    __birthday = Date(0, 0, 0)
    __phoneNumber = ""
    __accountNumber = ""
    __amountOfMoney = 0
    __email = ""
    __password = ""
    __isRegistered = False
    __id = 0
    x = Beneficiary('Lalka', 'Lolka', '047863')
    y = Beneficiary('Eugene', 'Bat', '01')
    z = Beneficiary('Tima', 'Sex', '1245124124')
    __beneficiaries = [x, y, z]

    def __init__(self, name, surname, email, date, phoneNumer, password):
        self.name = name
        self.surname = surname
        self.__email = email
        self.__phoneNumber = phoneNumer
        self.__password = password
        self.__birthday = date

    def PrintFullInfo(self):
        print(self.name, ' ', self.surname, ' ', self.__email, ' ')
        self.__birthday.PrintDate()
        print(self.__phoneNumber, ' ', self.__amountOfMoney, ' ', self.__id, ' ', self.__isRegistered, ' ',
              self.__password)

    def AddBeneficiary(self, name, surname, accountNumber):
        newBeneficiary = Beneficiary(name, surname, accountNumber)
        self.__beneficiaries.append(newBeneficiary)

    def PrintBeneficiaries(self):
        for i in self.__beneficiaries:
            print(i.name, ' ', i.surname, ' ', i.accountNumber)


if __name__ == "__main__":
    x = 0