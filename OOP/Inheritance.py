class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name=name

        ...
        
class Student(Wizard):

    ...


    def __init__(self,name,house):
     super().__init__(name)
     self.house=house

     ...
   
class Proffessor(Wizard):
    def __int__(self,name,subject):
      super().__init__(name)
      self.subject=subject

wizard=Wizard("Albus")
student =Student("Harry","Gryffindor")
proffessor =Proffessor("Severus","Defense Against the Dark Arts" )
...
        




