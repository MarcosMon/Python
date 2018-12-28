class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name


matz = Person('Yukihiro', 'Matsumoto', 47)
assert matz.full_name == 'Yukihiro Matsumoto'
assert matz.age == 47

joe = Person('Joe', 'Smith', 30)
assert joe.full_name == 'Joe Smith'
assert joe.age == 30
