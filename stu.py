class Student():
    name = None
    age = 18
    weight = 'null'
    __kt = 9

    def doSomething(self):
        print('i am doing...')
        return  None


young = Student()
for i in young.__dict__.keys():
    print(1)
#print(young.age)
#print(young.weight)
#young.doSomething()


def sayst():
    print("i want you ")

print(type(young.__dict__))
print(young.age)
