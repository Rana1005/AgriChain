class Checkout:
    items_cost = {
        "A":50,
        "B":30,
        "C":20,
        "D":15
    }
    def __init__(self, cart_item):
        self.cart_item = cart_item

    def calculate_price(self):
        cart_item = {
            "A":0,
            "B":0,
            "C":0,
            "D":0
        }

        for i in self.cart_item:
            cart_item[i] += 1
        price = 0
        for key in cart_item.keys():
            if  key == "A":
                    A3group = cart_item[key]//3
                    remain_A= cart_item[key]%3
                    price += A3group*130 + remain_A*50

            elif key == "B":
                B2group = cart_item[key]//2
                remain_B= cart_item[key]%2
                price += B2group*45 + remain_B*30

            else:
                price += cart_item[key]*self.items_cost[key]

        print(price)
       
checkout = Checkout("AABBCC")
checkout.calculate_price()


