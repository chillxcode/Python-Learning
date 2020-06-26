#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:59:24 2020

@author: emrecelik
"""

class Employee:
    
    raiseRatio = 0.4
    counter = 0         # Class Variabe
    
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname + "@gmail.com"
        
        Employee.counter = Employee.counter + 1
    
    def getFullName(self):
        return self.name + " " + self.surname
    
    def applySalaryIncrease(self):
        self.salary = self.salary  + self.salary * self.raiseRatio
    
employee1 = Employee("Emre", "Celik", 100)
print(employee1.getFullName())

print("Salary:",employee1.salary)
employee1.applySalaryIncrease()
print("Salary:",employee1.salary)

print(employee1.counter)
employee2 = Employee("Sude", "Ucyildiz", 150)
print(employee2.counter)



