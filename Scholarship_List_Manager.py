#!/usr/bin/python
#-*- coding: utf-8 -*-
import Scholarship
import sqlite3
    
class Scholarship_List_Manager:
    def __init__(self):
        self._scholarshipList = []
        
    def addScholarshipToList(self, scholarship):
        self._scholarshipList.append(scholarship)

    def loadScholarshipListFromFile(self):
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("select * from Scholarships")
        item = cu.fetchall()
        cx.close()

        self._scholarshipList.clear()
        for ii, row in enumerate(item):
            scholarship = Scholarship.Scholarship()
            scholarship.setters(row[1], row[2], int(row[3]))
            self._scholarshipList.append(scholarship)
        print("Finish loading!")
        return True

    def storeScholarshipListToFile(self):
        if(len(self._scholarshipList)==0):
            return False
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("delete from Scholarships")
        for scholarship in self._scholarshipList:
            info = scholarship.getters()
            cu.execute("insert into Scholarships(name, dscp, amount) values ('{}', '{}', {})".format(info[0], info[1], info[2]))
        print("Finish storing!")
        cx.commit()
        cx.close()
        return True    

    def displayScholarshipList(self):
        if(len(self._scholarshipList)>0):
            for scholarship in self._scholarshipList:
                scholarship.displayScholarship()
        else:
            print("Empty")
