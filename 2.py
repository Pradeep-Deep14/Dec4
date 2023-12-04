class student:
    def __init__(self,id_):
        self.id_ = id_
obj=student(100)
obj.__dict__['name']='John'
print(obj.id_ + len(obj.__dict__))

#102
