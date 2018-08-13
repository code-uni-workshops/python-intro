import io 

num_tests = 0
failed_tests = 0

def equal(expr, expected):
    global num_tests
    global failed_tests
    num_tests += 1
    if(expr == expected):
        print("Test Passed with result: '", expr, "'", sep = '')
    else:
        failed_tests += 1
        print("Failed!\n  expected: '", expected, "'\n  but got : '", expr, "'", sep = '')
    return

def str_print(*objects):
    out = io.StringIO()
    print(*objects, file=out, end="")
    res = out.getvalue()
    return res

def output(*objects, expected=""):
    out = str_print(*objects)
    equal(out, expected)
    return

def summary():
    print("-------------------------------------------")
    if failed_tests == 0:
        print("All", num_tests, "passed!")
    else:
        print("{} out of {} tests failed!".format(failed_tests, num_tests))
