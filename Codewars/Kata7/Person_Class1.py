class Person(object):

    def __init__(self,name):
        self.name=name

    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)


jack = Person("Jack")
jill = Person("Jill")


if __name__ == '__main__':


	assert jack.greet("Jill") == "Hello Jill, my name is Jack"
	assert jack.greet("Mary") == "Hello Mary, my name is Jack"

	assert jill.greet("Jack") == "Hello Jack, my name is Jill"
	assert jill.name, 'Jill' == "Person's name could not be retrieved"