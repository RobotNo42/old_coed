class People:
    n = 23
    def __init__(self):
        self.age = 1200
    def walk(self):
        print("fuck u walk")


p = People()
p.z = 2
p.__dict__['fuk'] = 20
p.__dict__['z'] = 23
print(p.__dict__)