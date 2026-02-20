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
    
    def upcoming_birthdays(self, in_days):
        today = date.today()
        upcoming = []

        for name, birthdate in self.records.items():
            next_birthday = birthdate.replace(year=today.year)
            
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            
            days_till = (next_birthday - today).days
            
            if days_till <= in_days:
                upcoming.append(name)
        
        return upcoming

day = Birthday()
print(day.add_friend("Vedant", "2005/09/23")) 
print(day.add_friend("Grace", "1997/07/20"))
print(day.add_friend("Georgi", date(2006, 2, 21)))

# print(day.update_birthdate("Vedant", "2004/09/23")) 

# print(day.update_name("Phone", "2004/09/23")) 

print(day.upcoming_birthdays(5))