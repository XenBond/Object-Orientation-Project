#!/usr/bin/python
#-*- coding: utf-8 -*-

class Student:
    def __init__(self):
        self._first = None
        self._last = None
        self._email = None

    def setters(self, first_name, last_name, email):
        self._first = first_name
        self._last = last_name
        self._email = email
        return True

    def getters(self):
        return [self._first, self._last, self._email]

    def toString(self):
        return ' '.join(['First_name', self._first, 'Last_name', self._last, 'Email', self._email])

    def displayStudent(self):
        print("----------------------------------------------------")
        print("First name:", self._first, "  last name:", self._last)
        print("Email:", self._email)
        
        

