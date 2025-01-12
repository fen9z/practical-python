def grok():
    raise RuntimeError("Whoa!")  # Exception raised here


def spam():
    grok()  # Call that will raise exception


def bar():
    try:
        spam()
    except RuntimeError as e:  # Exception caught here
        print("bar", e)


def foo():
    try:
        bar()
    except RuntimeError as e:  # Exception does NOT arrive here
        print("foo", e)


foo()
