"""
from abc import abstractmethod

class ITSTEP:
    @abstractmethod
    def show_info(self):
        pass

    def simple_method(self):
        print("...")








class IFITSTE(ITSTEP):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_info(self):
        return f"Name: {self.name} id: {self.id}"



class KalushITSTEL(ITSTEP):
    def __init__(self, name, id, count):
        self.name = name
        self.id = id
        self.count = count

    def show_info(self):
        return f"Name: {self.name} id: {self.id} count : {self.count}"


obj = IFITSTE("IF","001")

obj1= KalushITSTEL("Kalush", "002", 500)




class Transport:
    def __init__(self,name):
        self.name= name

    @abstractmethod
    def show_transort(self):
        pass


class car(Transport):
    def __init__(self, name, speed):
        super().__init__(name)
        self.name = name
        self.speed = speed


    def show_transort(self):
        return f"Name: {self.name} speed: {self.speed}"




class moto(Transport):
    def __init__(self, name, speed, type):
        self.name = name
        self.speed = speed
        self.type = type

    def show_transort(self):
        return f"Name: {self.name} speed: {self.speed} , type {self.type}"


"""
import os

"""
Створити файл , назвати його ITSTEPTEST.txt 
запитати в користувача інформацію , та записати її у файл, якщо користувач ввів STOP - зупинити програму 





myfile = open("ITSTEP.txt", "w")

text = " "

while text != "stop":
    text = input("Enter info : ")
    myfile.write(text)

myfile.close()

"""

file = "NEWFILE.txt"

with open("NEWFILE.txt","w") as itstepFile:
    itstepFile.write("NEW INFO")


with open(file, "r") as myFile:
    print(myFile.readlines())


"""
створити файл - записати у нього інфо про себе 
ім'я , вік , дата народження , ід 

використовуємо конструкцію with open

"""