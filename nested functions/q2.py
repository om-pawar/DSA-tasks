def calculate_total(price,tax):
    def calculate_tax():
        return price*tax/100
    return price+calculate_tax()

total=calculate_total(1000,18)
print(total)