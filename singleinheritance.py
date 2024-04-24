class Person:
    def __init__(self,name,age):
        self.name='shalu'
        self.age=20
        
class Professor(Person):
    def is_professor(self):
        return f'{self.name} is professor'
sir=Professor()
print(sir.is_professor)

    