class ShoppingCart:
    def __init__(self):
        self.cart={}
        self.discount_codes={"Save10":0.10, "Save20":0.20}
        self.total_price= 0

    def add_item(self,item,quantity,price):
        if item in self.cart:
            self.cart[item]["quantity"]+= quantity
        else:
            self.cart[item]={"quantity":quantity,"price":price}
            print(f"Added {quantity} of {item} to the cart.")

    def remove_item(self,item):
        if item in self.cart:
            del self.cart[item]
            print(f"Remove {item} from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        for item,details in self.cart.items():
            total_item_price = details["quantity"] * details["price"]
            print(f"{item}: {details['quantity']} x ${details['price']} = ${total_item_price:.2f}")

    def get_total_price(self):
        self.total_price=sum(details['quantity']*details['price'] for details in self.cart.values())
        return self.total_price
    def apply_discount(self,code):
        discount=self.discount_codes.get(code,0)
        if discount>0:
            discount_amount=self.get_total_price()*discount
            self.total_price-=discount_amount
            print(f"Discount applied: {discount_amount} off.")
        else:
            print("Invalid discount code.")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Receipt:")
        self.view_cart()
        print(f"Total : {self.get_total_price():.2f}")
        print("Thank You for shopping!")
        self.cart.clear()
        self.total_price=0

cart=ShoppingCart()

cart.add_item("Apple",7,200.00)
cart.add_item("Banana",12,150.00)
cart.view_cart()
cart.apply_discount("Save20")
cart.checkout()