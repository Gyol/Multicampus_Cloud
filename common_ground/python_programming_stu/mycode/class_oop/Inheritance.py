# 상속!!!
# 클래스의 공통 속성, 매서드는 부모쪽에 몰아넣고 자식은 그 외 개별적인것들? 뭐 이런식인 것 같음
# 이하 부모
class Person(object):
    def __init__(self, name, age, gender):
        self.name1 = name
        self.age1 = age
        self.gender1 = gender

    def about_me(self):
        print(f'Person의 이름은 {self.name1}, 나이는 {self.age1}세 입니다.')

# 이하 자식
class Employee(Person):
    def __init__(self, name, age, sex, salary, hired_date):
        super().__init__(name, age, sex)
        self.salary1 = salary
        self.hired_date1 = hired_date

    def about_me(self):
        # 여기서 super치고 tab누르니까 바로 아래같이 뜨는데 왜그러는지? 근데 우리는 비워서 코딩하자너
        # super(Employee, self).about_me()
        super().about_me()
        print(f'급여는 {self.salary1}, 입사일자는 {self.hired_date1}.')

myPerson = Person('Gyol', 27, 'F')
myEmployee = Employee('Ming', 27, 'M', '7K', 2014)
myPerson.about_me()
myEmployee.about_me()
