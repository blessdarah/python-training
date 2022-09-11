def print_hello():
    print("Hello")
    return;

def say_hi(name = "user"):
    if(name == ""):
        print("No name provided, using default name")
        name = "user"
        
    print("Hi", name)
    return;


print_hello()
say_hi()
say_hi("Benoit")
say_hi("")

