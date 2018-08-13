import io 

def str_print(*objects):
    out = io.StringIO()
    print(*objects, file=out, end="")
    res = out.getvalue()
    return res

class test:
    num_tests = 0
    failed_tests = 0

    def equal(self, expr, expected):
        self.num_tests += 1
        if(expr == expected):
            print("Test Passed with result: '", expr, "'", sep = '')
        else:
            self.failed_tests += 1
            print("Failed!\n  expected: '", expected, "'\n  but got : '", expr, "'", sep = '')
        return


    def output(self, *objects, expected=""):
        out = str_print(*objects)
        self.equal(out, expected)
        return

    def summary(self):
        print("------------------------------")
        if self.failed_tests == 0:
            print("All", self.num_tests, "passed!")
        else:
            print("{} out of {} tests failed!".format(self.failed_tests, self.num_tests))

    def __enter__(self, *args):
        print("\n\n------------------------------\n New Test run\n------------------------------")
        return self

    def __exit__(self, *args):
        self.summary()