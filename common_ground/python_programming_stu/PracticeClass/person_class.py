class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print('저의 이름은 {0}, 나이는{1}, 성별은 {2}입니다'.format(self.name, self.age, self.gender))


# 자식 클래스
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_data):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_data = hire_data

    def about_me(self):
        super().about_me()
        print(f'제 급여는 {self.salary}, 입사일은 {self.hire_data}')


myPerson = Person('길동', 30, '남')
myEmployee = Employee('둘리', 100, '남', 3000000, '2020/06/30')
myPerson.about_me()
myEmployee.about_me()
