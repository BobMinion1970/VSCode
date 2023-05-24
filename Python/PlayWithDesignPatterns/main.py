# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

####################################### Functions ###################################
import datetime

def test_decorator():
    myfunc()

def logger(func):
    def wrapper():
        print(str(datetime.datetime.now()) + " --- Function call started: " + str(func))
        func()
        print(str(datetime.datetime.now()) + " --- Function call finished: " + str(func))
    return wrapper

@logger
def myfunc():
    print("Inside myfunc")

def main():
    test_decorator()
####################################### Main ########################################
main()
