from datetime import date


class Birthday:
    
    def __init__(self):
        self.records = {}

    def add_friend(self, name, birthdate):
        self.records[name] = birthdate
        return self.records 
    
    def update_birthdate(self, name, new_birthday):
        self.records[name] = new_birthday
        return self.records

    def update_name(self, new_name, birthdate):
        self.records[new_name] = birthdate
        return self.records

day = Birthday()
print(day.add_friend("Vedant", "2005/09/23")) 
print(day.add_friend("Grace", "1997/07/20"))

print(day.update_birthdate("Vedant", "2004/09/23")) 

print(day.update_name("Phone", "2004/09/23")) 