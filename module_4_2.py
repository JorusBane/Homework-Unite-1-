def testfunction():
    def innerfunction():
        print("Я в области видимости функции testfunction")
    innerfunction()

testfunction()
#innerfunction()
#NameError: name 'innerfunction' is not defined