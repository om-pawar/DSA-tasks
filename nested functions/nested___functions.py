def outer():
    def inner():
        print("hello from inner");
   
    inner()

outer()
