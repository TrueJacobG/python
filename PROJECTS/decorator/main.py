def IwillDecorate(func):
    def wrapper(*args, **kwargs):
        print("My name is ")
        func(*args, **kwargs)
        print("Nice to meet you")
    return wrapper


@IwillDecorate
def sayYourName(name):
    print(name.capitalize())

# when you call this function it will be passed like a parameter to decorator


sayYourName(input())
