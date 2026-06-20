import pandas as pd
# classes 

#Class to set Character

class Character:
    def __init__(self, name = None, age = None, gender = None ):
        self.name = name 
        self.age = age 
        self.gender = gender 

    def set_name(self, name):
        if self.name is None:
            self.name = name

    def set_age(self,age):
        if self.age is None:
            self.age = age
    
    def set_gender(self, gender):
        if self.gender is None:
            self.gender = gender 

    def description(self, more = None):
        if more is None:
            self.description = f"{self.name}, {self.gender}, age: {self.age}. \n \n"
        else:
            self.description = f"{self.name}, {self.gender}, age: {self.age}. \n \n{more}."

    def get_name(self):
        return self.name 
    
    def get_age(self):
        return self.age
    
    def get_gender(self):
        return self.gender 
    
    def get_des(self): 
        return self.description
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.age}")

        print(self.description)
    
class Search_engine:
    df = pd.read_csv("people_info.csv")
    def __init__(self, aim):
        self.aim = aim 
