from first_main import IwillDecorate


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"This function is called {self.count} times")
        return self.func(*args, **kwargs)


@CountCalls
@IwillDecorate
def print_name(name):
    print(f"My name is {name}!")


# you can use call as a decorator <3
print_name("Bob")
print_name("Bob")
