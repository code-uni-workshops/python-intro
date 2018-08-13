import testc


my_test = testc.test()
my_test.equal(4, 5)
my_test.equal(5, 5)
my_test.output("Hello", "World", 42, expected="Hello World 42")
my_test.summary()

with testc.test() as test:
    test.equal(4, 5)
    test.equal(5, 5)
    test.output("Hello", "World", 42, expected="Hello World 42")


with testc.test() as test:
    test.equal(4, 5)
    test.output("Hello", "World", 42, expected="Hello World 42")

