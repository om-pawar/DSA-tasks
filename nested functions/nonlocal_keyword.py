def outer():
    x=10

    def inner():
        nonlocal x

        x=x+10

        print(x)

    inner()

outer()