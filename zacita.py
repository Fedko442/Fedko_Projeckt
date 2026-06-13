class Group:

    def __init__(self, name, phone, department):
        self.name = name
        self.phone = phone
        self.department = department


employees = {
    "emp1": Group("Иван", "89281419630", "IT"),
    "emp2": Group("Петр", "89081953622", "Бухгалтерия"),
    "emp3": Group("Анна", "89289043540", "Маркетинг")
}

print(employees["emp1"].phone)
print(employees["emp2"].phone)
print(employees["emp3"].phone)