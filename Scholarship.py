#!/usr/bin/python
#-*- coding: utf-8 -*-

class Scholarship:
    def __init__(self):
        self._id = None
        self._description = None
        self._amount = None

    def getters(self):
        return [self._id, self._description, int(self._amount)]

    def setters(self, id_, description, amount):
        self._id = id_
        self._description = description
        self._amount = int(amount)
        return True

    def toString(self):
        return ' '.join(['ID', self._id, 'Description', self._description, 'Amount', self._amount])

    def displayScholarship(self):
        print("----------------------------------------------------")
        print("ID: ", self._id)
        print("Description: ", self._description)
        print("Amount: ", self._amount)
