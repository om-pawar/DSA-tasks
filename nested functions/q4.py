x="global"

def outer():
    x="local"
    def inner():
        x="inner"
        print(x)

    inner()

outer()