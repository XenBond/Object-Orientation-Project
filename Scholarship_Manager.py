#!/usr/bin/python
#-*- coding: utf-8 -*-
import Scholarship
import pickle
import sqlite3

class Scholarship_Manager:
    def __init__(self):
        pass

    def addScholarship(self, name, description, amount):
        scholarship = Scholarship.Scholarship()
        scholarship.setters(name, description, int(amount))
        return scholarship
    
    def loadScholarshipFromFile(self, idx):
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        cu.execute("select * from Scholarships where id like '%d'" % idx)
        record = cu.fetchall()[0]
        cx.close()
        scholarship = Scholarship.Scholarship()
        scholarship.setters(record[1], record[2], int(record[3]))
        return scholarship
        
    def storeScholarshipToFile(self, scholarship):
        cx = sqlite3.connect('test.db')
        cu = cx.cursor()
        info = scholarship.getters()
        cu.execute("insert into Scholarships(name, dscp, amount) values ('{}', '{}', {})".format(info[0], info[1], info[2]))
        cx.commit()
        cx.close()