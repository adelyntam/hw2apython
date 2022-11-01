import time
def timeme(function):

    def wrapper():
            a = time.time()
            function()
            b = time.time()
            print('Total time ' + f'{b-a}')

    return wrapper
