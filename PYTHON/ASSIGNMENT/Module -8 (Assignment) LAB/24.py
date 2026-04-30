# 24) Write a Python program to show multiple inheritance. 


class Father:
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")

c = Child()
c.show_father()
c.show_mother()
c.show_child()