import time
def timestamp(function):
        def wrapper():
            s = time.ctime()
            print(s)
            function()

        return wrapper
