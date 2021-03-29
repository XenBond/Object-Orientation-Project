#!/usr/bin/python
#-*- coding: utf-8 -*-
import Student
import sqlite3

class Student_Manager:
    def __init__(self):
        pass

    def addStudent(self, first_name, last_name, email):
        student = Student.Student()
        student.setters(first_name, last_name, email)
        return student
    
    def loadStudentFromFile(self, idx):
        # input has been modified 
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("select * from Students where id like '%d'" % idx)
        record = cu.fetchall()[0]
        cx.close()
        student = Student.Student()
        student.setters(record[1], record[2], record[3])
        return student
        
    def storeStudentToFile(self, student):
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        info = student.getters()
        cu.execute("insert into Students(firstname, lastname, email) values ('{}', '{}', '{}')".format(info[0], info[1], info[2]))
        cx.commit()
        cx.close()
