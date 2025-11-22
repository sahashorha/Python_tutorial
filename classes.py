class Animal:
      def walk(self):
            print("Walking...");
# inherit the properties of anuimal
class Dogesh(Animal):
      # Constructor
      def __init__(self, name, age):
            self.name = name;
            self.age = age;
      # function
      def bark(self):
            print(" wolf! ");
roger = Dogesh("Roger", 8)
print(roger.bark());
print(roger.age);
print(roger.name);
roger.bark();
roger.walk();
# Inheritance
