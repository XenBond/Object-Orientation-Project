#!/usr/bin/python
#-*- coding: utf-8 -*-
import Scholarship_System_Facade
import os

class Scholarship_Client:
    def __init__(self):
        self._scholarship_system_facade = Scholarship_System_Facade.Scholarship_System_Facade()

    def main(self):
        while 1:
            os.system('cls')
            print("This program is for maintaining a scholarship system.\n",\
                  "1: Display all students.\n",\
                  "2: Enter new student\n",\
                  "3: Load student csv file.\n",\
                  "4: Store student csv file.\n",\
                  "5: Display all scholarships.\n",\
                  "6: Enter new scholarship\n",\
                  "7: Load scholarship csv file.\n",\
                  "8: Store scholarship csv file.\n",\
                  "else: exit")
            input_ = input("Your choice: ")
            if(input_=='1'):
                self._scholarship_system_facade.displayAllStudents()
            elif(input_=='2'):
                self._scholarship_system_facade.enterNewStudent()
            elif(input_=='3'):
                self._scholarship_system_facade.loadStudentListFromFile()
            elif(input_=='4'):
                self._scholarship_system_facade.storeStudentListToFile()
            elif(input_=='5'):
                self._scholarship_system_facade.displayAllScholarship()
            elif(input_=='6'):
                self._scholarship_system_facade.enterNewScholarship()
            elif(input_=='7'):
                self._scholarship_system_facade.loadScholarshipListFromFile()
            elif(input_=='8'):
                self._scholarship_system_facade.storeScholarshipListToFile()
            else:
                break
            os.system('pause')

client = Scholarship_Client()
client.main()
