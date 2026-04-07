class human:
    def __init__(self , age , name):
        self.age = age
        self.name= name
    
    def __str__(self):
        return  'a human with name ' + self.name + '.' + " and her age is " +str(self.age)+'.'
    def __repr__(self):
        return 'a human with name ' + self.name + '.' + " and her age is " +str(self.age)+'.'
    
    def older_younger_than(self,age):
        if self.age> age :
            print("our age is bigger than their age.")
        elif self.age== age:
            print("our age is equal to their age.")
        else: 
            print("our age is less than their age.")
h = human (age=19 , name= 'shreshtha')
print(h)
h.older_younger_than(20)