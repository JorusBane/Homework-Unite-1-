def testfunction():
    def innerfunction():
        print("Я в области видимости функции testfunction")

testfunction()
#innerfunction()
#NameError: name 'innerfunction' is not defined