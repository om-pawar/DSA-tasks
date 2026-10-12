x="global"

def outer():
    x="local"

    def inner():
        print(x)

    inner()

outer()