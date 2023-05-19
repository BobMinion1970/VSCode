# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
import Classes.MyMessage as mym
################################ Functions #####################################
def testVenv():
    _message1 = mym.MyMessage(theMessage="This is an error message!", error=True)
    _message2 = mym.MyMessage(theMessage="This is an info message.")
def main():
    testVenv()

################################# Main ########################################
main()
