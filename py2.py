class student:
    def __init__(self):
        self.name="loki"
        self.age=21
        self.usn=420
        self.gender="male"
    def study(self):
        print("loki is not studying")
s1=student()
print(s1.name)
print(s1.age)
print(s1.usn)
print(s1.gender)
s1.study()