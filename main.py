class Test:
    someOption = 7

    def __dir__(self):
        return [self.someOption]


test = Test()
print(test.someOption)

test.someOption = 42
print(test.someOption)

someOtherOption = dir(test)[0]
print(someOtherOption)

someOtherOption = 90
print(someOtherOption)
print(test.someOption)

