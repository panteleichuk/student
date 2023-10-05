class Student:
    def __init__(self, name, surname, group,
                  age, logiks, login, password, telegram ):
        self.name = name
        self.surname =surname
        self.group = group
        self.age = age
        self.logiks = logiks
        self.login = login
        self.password = password
        self.telegram = telegram

    def all_info(self):
        print("=======All info about student:=========")
        print("Name:", self.name)
        print("Surname:",self.surname )
        print("Group:",self.group )
        print("Age:",self.age)
        print("Logiks:",self.logiks )
        print("Login:",self.login )
        print("Password:",self.password )
        print("Telegram:",self.telegram )
        print("===========================================")
    
    def print_logiks(self):
        print("=======Logiks of student======")
        lg = ""
        for logik in self.logiks:
            lg+=str(logik)+" "
        print(lg)
        print("All logiks:", sum(self.logiks))
        print("==============================")
    
    def print_name(self):
        print("=======NAme about student:=========")
        print("Name:", self.name)
        print("Surname:",self.surname )
        print("Age:",self.age)
        print("===========================================")

    def print_login(self):
        print("=======Login info about student:=========")
        print("Group:",self.group )
        print("Login:",self.login )
        print("Password:",self.password )
        print("===========================================")

student_list = list()

student = Student("Maria","Ivanova","Python",
                  14,[5,6,4,5,6],"mrivanova","5679","@ivanova")
student_list.append(student)

student = Student("Nastia","Sidorova","Python",
                  15,[5,6,4,5,6],"sidor","5679","@sidor")
student_list.append(student)

student = Student("Oleg","Budko","Python",
                  15,[5,6,4,5,6],"budko","5679","@budko")
student_list.append(student)

print("List of student")
for i in range(len(student_list)):
    print(i,"-",student_list[i].surname," ",student_list[i].name)

while True:
    print("What do you want? 1- all info, 2-logiks,3-name,4-login,5-exit")
    do = int(input())
    if do==1:
        id_st = int(input("Id student?"))
        student_list[id_st].all_info()
    elif do==2:
        id_st = int(input("Id student?"))
        student_list[id_st].print_logiks()
    elif do==3:
        id_st = int(input("Id student?"))
        student_list[id_st].print_name()
    elif do==4:
        id_st = int(input("Id student?"))
        student_list[id_st].print_login()
    elif do==5:
        break