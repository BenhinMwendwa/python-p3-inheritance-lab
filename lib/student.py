#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self,knowledge,first_name, last_name):
        self.knowledge = knowledge
        super().__init__(first_name, last_name)
        knowledge=[]
        
    def learn(self,str):
        self.knowledge.append(str)
        pass