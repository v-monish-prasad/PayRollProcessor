class Employee:
    def __init__(self, name):
        self.name = name

    def calculatePay(self, salary=0, hourlyRate=0, hoursWorked=0):  # method overloading is not directly supported in python
        if hourlyRate and hoursWorked:
            print("Salary for", self.name, ": ", hourlyRate * hoursWorked)
        else:
            print("Salary for", self.name, ": ", salary)


class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class HourlyWorker(Employee):
    def __init__(self, name, hourlyRate, hoursWorked):
        super().__init__(name)
        self.hourlyRate = hourlyRate
        self.hoursWorked = hoursWorked


salariedEmployee = SalariedEmployee("Monish", 1200000)
hourlyWorker = HourlyWorker("Akash", 3600, 24)
salariedEmployee.calculatePay(120000)
hourlyWorker.calculatePay(hourlyRate=3600, hoursWorked=24)

