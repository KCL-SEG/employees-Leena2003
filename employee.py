"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, comissions, comission_pay, bonus_comission, salary, hours=0):
        self.name = name
        self.comissions = comissions
        self.comission_pay = comission_pay
        self.bonus_comission = bonus_comission
        self.salary = salary
        self.hours = hours

    def get_pay(self):
        total = 0

        if self.hours == 0:
            total += self.salary
            if self.comissions!=0:
                total += (self.comissions*self.comission_pay)
            elif self.bonus_comission !=0:
                total += self.bonus_comission
            return total

        else:
            total += (self.salary * self.hours)
            if self.comissions != 0:
                total += (self.comissions * self.comission_pay)
            elif self.bonus_comission != 0:
                total += self.bonus_comission
            return total


    def __str__(self):
        final_string = self.name + " works on a "
        if self.hours !=0: #if hourly worker
            final_string += "contract of " + str(self.hours) + " hours at " + str(self.salary) + "/hour"

            if self.comissions > 0:
                final_string += " and recieves a comission for " + str(self.comissions) + " contract(s) at " + str(
                    self.comission_pay) + "/contract. Their total pay is " + str(self.get_pay()) + "."

            elif (self.bonus_comission != 0):
                final_string += " and recieves a bonus comission of " + str(
                    self.bonus_comission) + ". Their total pay is " + str(self.get_pay()) + "."

            else:
                final_string += ". Their total pay is " + str(self.get_pay()) + "."

            return final_string
        else:
            final_string += "monthly salary of " + str(self.salary)
            if self.comissions > 0:
                final_string += " and recieves a comission for " + str(self.comissions) + " contract(s) at " + str(
                    self.comission_pay) + "/contract. Their total pay is " + str(self.get_pay()) + "."

            elif (self.bonus_comission != 0):
                final_string += " and recieves a bonus comission of " + str(
                    self.bonus_comission) + ". Their total pay is " + str(self.get_pay()) + "."

            else:
                final_string += ". Their total pay is " + str(self.get_pay()) + "."

            return final_string

billie = Employee('Billie',0,0,0,4000)

charlie = Employee('Charlie', 0, 0, 0, 25, 100)

renee = Employee('Renee', 4, 200, 0, 3000)

jan = Employee('Jan', 3, 220, 0, 25, 150)

robbie = Employee('Robbie', 0, 0, 1500, 2000)

ariel = Employee('Ariel', 0, 0, 600, 30, 120)


