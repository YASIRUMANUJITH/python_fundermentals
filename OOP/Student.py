class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing Name")
        if house not in("Gryffindor","Hufflepuff","Slytherin"):
            raise ValueError("Invalid House")
        
        self.name=name
        self.house=house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
def main():
    student=get_student()
    student.house="Number Four,Privet Drive"
    print(student)

def get_student():
    name=input("Name:")
    house=input("House:")
    return Student(name,house)

if __name__ == "__main__":
    main()
