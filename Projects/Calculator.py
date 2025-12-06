# Today we start Calculator

# flow -> make_funciton add,sub,multiply,divide
def add(num1, num2):
     return num1 + num2;
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
     return (num1 * num2);
def divide(num1, num2):
     if(num2 == 0):
          return "Error !!! Division by Zero";
     else: 
          return (num1/num2);

print("PYTHON CALCULATOR");
while(True):
     print("1. ADD");
     print("2. SUBTRACT");
     print("3. MULTIPLY");
     print("4. DIVIDE");
     print("5. EXIT");
     choice = input("Enter Your Choice(1-5): ");

     if choice == '5':
          print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
          print("Exitting  Calculator...");
          print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

          break;
     if choice in ('1','2','3','4','5'):
          num1 = float(input("Enter first Number: "));
          num2 = float(input("Enter Second Number: "));

          if choice == '1':
               print("---------------xxxxxx------------------")
               print("Result: ", add(num1,num2) );
               print("---------------xxxxxx------------------")
          
          elif choice =='2':
               print("---------------xxxxxx------------------")
               print("Result: ",subtract(num1, num2));
               print("---------------xxxxxx------------------")
          elif choice == '3':
               print("---------------xxxxxx------------------")
               print("Result: ",multiply(num1,  num2));
               print("---------------xxxxxx------------------")
          elif choice == '4':
               print("---------------xxxxxx------------------")
               print("Result: ",divide(num1, num2));
               print("---------------xxxxxx------------------")
     else:
          print("---------------xxxxxx------------------")
          print("Invalid Choice..., Please Try Again"); 
          print("---------------xxxxxx------------------")




          
          




