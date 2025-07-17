try:
    a = 20
    print(a)
    del a
    print(a)
except NameError:
    print("a is not defined")
except:
    print("An exception occurred")