def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

@announce       # calls decorator on hello function
def hello():
    print("Hello, world!")

hello()