def IwillDecorate(func):
    def wrapper(*args, **kwargs):
        print("###")
        func(*args, **kwargs)
        print("###")
    return wrapper


@IwillDecorate
def sayYourName(name):
    print(name.capitalize())

# when you call this function it will be passed like a parameter to decorator


if __name__ == '__main__':
    sayYourName(input())
