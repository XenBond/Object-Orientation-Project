#!/usr/bin/python
#-*- coding: utf-8 -*-
import Student
import sqlite3

class Student_List_Manager:
    def __init__(self):
        self._studentList = []
        
    def addStudentToList(self, student):
        self._studentList.append(student)
    
    def loadStudentListFromFile(self):
        # fetch data
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("select * from Students")
        item = cu.fetchall()
        cx.close()
        
        self._studentList.clear()
        for ii, row in enumerate(item):
            student = Student.Student()
            student.setters(row[1], row[2], row[3])
            self._studentList.append(student)
        print("Finish loading!")
        return True

    def storeStudentListToFile(self):
        if(len(self._studentList)==0):
            return False
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("delete from Students")
        for student in self._studentList:
            info = student.getters()
            cu.execute("insert into Students(firstname, lastname, email) values ('{}', '{}', '{}')".format(info[0], info[1], info[2]))
        print("Finish storing!")
        cx.commit()
        cx.close()
        return True    
    
    def displayStudentList(self):
        if(len(self._studentList)>0):
            for student in self._studentList:
                student.displayStudent()
        else:
            print("Empty")