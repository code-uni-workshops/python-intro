import test

test.equal(4, 5)
test.equal(5, 5)
test.output("Hello", "World", 42, expected="Hello World 42")

test.summary()