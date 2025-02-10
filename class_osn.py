class Andrew:
    def __init__(self, name=None, surname=None, birth_year=None):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def calculator_kurs(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        if age < 16:
            return "Ще не студент"
        return min((age - 16) + 1, 4)

    def list_name_surname(self):
        return [self.name, self.surname]

    def print_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Прізвище: {self.surname}")
        print(f"Рік народження: {self.birth_year}")
        print(f"Курс: {self.calculator_kurs()}")


student = Andrew("Андрій", "Кравчик", 2008)
student.print_info()
