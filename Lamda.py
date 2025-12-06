from functools import reduce
lambda num : num* 2
multiply = lambda a, b : a*b
print(multiply(2,3));

# map filter and reduce 
# number = [1,2,3];
# def double(a):
#       return a * 2;
# result = map(double, number);
# print(list(result));

# using lambda function

# result = map(lambda a:a*2, number);
# print(list(result));

# takes filter

# filter is perform operation in list and dictionaries and tuples . 
# it perform ineach elements of any data structure and print which element return true;

numbers = [1,2,3,4,5,6,7,8]
# def isEven(n):
#       return n%2==0;
result = filter(lambda a: a%2 == 0,numbers);
# print(list(result));

words = ["Success", "Beautifull Job","GF","Bike","Mercedes" "Beautifull Girlfriend",];
filter_words =filter(lambda w: len(w) > 3, words)
print(list(filter_words));

# reduce(function, iterable);

numbers = [1,2,3,4,5]
result = reduce(lambda a, b : a + b,numbers)
print(result);

words = ["Python","is","awesome"];
result = reduce(lambda x,y : x + " " + y, words);
print(result);

#recursion
#decorators
def logtime(func):
      def wrapper():
            print("Before");
            val = func();
            print("after");
            return val;
      return wrapper
@logtime
def hello():
      print("Hello");
hello()


# One example of decorator
def auth_required(func):
      def wrapper(user):
            if user != "admin":
                  print("Access Denied");
                  return
            result  = func(user)
            print("Rahul Poddar")
            return result;
      return wrapper;
@auth_required
def delete_database(user):
      print(f" {user} deleted the database ! ");
delete_database("guest");
delete_database("admin");