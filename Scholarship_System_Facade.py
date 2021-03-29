#!/usr/bin/python
#-*- coding: utf-8 -*-

import Student_Manager
import Student_List_Manager
import Scholarship_Manager
import Scholarship_List_Manager
import sqlite3



class Scholarship_System_Facade:
    def __init__(self):
        
        # initialize the dataset
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("create table if not exists Students (id INTEGER primary key autoincrement, firstname TEXT, lastname TEXT, email TEXT)")
        cu.execute("create table if not exists Scholarships (sid INTEGER primary key autoincrement, name TEXT, dscp TEXT, amount INTEGER)")
        cu.execute("create table if not exists Connections (id INTEGER, sid INTEGER, qty INTEGER)")
        cx.commit()
        cx.close()
        
        # initialize manager object
        self._studentManager = Student_Manager.Student_Manager()
        self._studentListManager = Student_List_Manager.Student_List_Manager()
        self._scholarshipManager = Scholarship_Manager.Scholarship_Manager()
        self._scholarshipListManager = Scholarship_List_Manager.Scholarship_List_Manager()

    # Student
    def displayAllStudents(self):
        self._studentListManager.displayStudentList()

    def enterNewStudent(self):
        first_name = input("Please input the student's first name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        student = self._studentManager.addStudent(first_name, last_name, email)
        self._studentListManager.addStudentToList(student)

    def loadStudentListFromFile(self):
        self._studentListManager.loadStudentListFromFile()
        
    def storeStudentListToFile(self):
        self._studentListManager.storeStudentListToFile()
        
    # Scholarship
    def displayAllScholarship(self):
        self._scholarshipListManager.displayScholarshipList()

    def enterNewScholarship(self):
        id_ = input("Please input number as scholarship's ID: ")
        description = input("Scholarship's description: ")
        amount = input("Amount: ")
        scholarship = self._scholarshipManager.addScholarship(id_, description, amount)
        self._scholarshipListManager.addScholarshipToList(scholarship)

    def loadScholarshipListFromFile(self):
        self._scholarshipListManager.loadScholarshipListFromFile()
        
    def storeScholarshipListToFile(self):
        self._scholarshipListManager.storeScholarshipListToFile()