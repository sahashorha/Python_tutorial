# Docstrings are special strings used to document python code
# Declared using triple quotes """ or '''

# Triple of Docstring

def divide(a, b):
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        Dividend.
    b : float
        Divisor.

    Returns
    -------
    float
        Quotient of division.
    """
  
    if b == 0:
        raise ValueError("Division by zero not allowed.")
    return a / b
# print(divide(6, 2))
# print(divide.__doc__)
# __doc__  used is printing the docstrings
def fib(n : 'int', output:'list' = []) -> 'list':
    if n == 0:
        return output
    else:
        if len(output) < 2:
            output.append(1)
            fib(n-1,output)
        else :
            last = output[-1]
            second = output[-2]
            output.append(last + second)
            fib(n-1,output)
        return output
    
print(fib.__annotations__)



# Exception
# Exception Handling 
n = 10;
try:
    res = n/0;
except ZeroDivisionError:
    print("can't divided by Zero");


# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.

from contextlib import contextmanager;
@contextmanager
def open_file(filename,mode):
    file = open(filename,mode)
    try:
        yield file;
    finally:
        file.close()
with open_file('example.txt','w') as file:
    file.write("Hello, World");

file = open("example.txt","w")
try:
    file.write("Hello Rahul Poddar")
finally:    
    file.close()