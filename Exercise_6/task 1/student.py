from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name

        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(title.get_title())
        self.grades[title.get_title()] = title.get_grade()


    def get_list_modules(self):
        print("Modules of student {0}: ".format(str(self.name)))
        for item in self.modules:
            print("\t"+item)

    def get_grades(self):
        print("Grades of student {0}: ".format(str(self.name)))
        for mod, gr in self.grades.items():
            print ("\t"+str(mod) + ": " + str(gr))


### test cases ###


me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
