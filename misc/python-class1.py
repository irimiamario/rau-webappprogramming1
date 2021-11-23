variable1 = "string 1"
print(variable1.find("str"))
"""
FE form collects user input
FE JS code makes an HTTP request to BE endpoint with the user input
BE receives request + input
BE figures out what to do (resource to use)
BE Resource will use the data + resource methods to execute what the user requested
BE Resource will return some result (error or data)
"""

"""
I can create an Account with the following information: username, password...

Once I have an Account, I can then change my password, log-in, and add a new card.

A card should hold the following details: card number, exp date, name, billing address, code ...

When I have a valid card, I can then search for products.

A product has name, price, description.

If I find a product I like, I can add it to cart.

Once I have some products added to cart I can purshase them using the card attached to my account.
"""

"""
Nouns:
- Account
-- properties
--> username
--> password
--> credit_card
-- actions
--> create
--> change_password
--> login
--> add_card


- CreditCard
- Product
- ShoppingCart
"""

class Account:
    def __init__(self, username, password, credit_card=None):
        self.username = username
        self.passwd = password
        self.credit_card = credit_card

    def change_password(self, old_password, new_password):
        if old_password == self.passwd:
            self.passwd = new_password
        else:
            raise Exception("Invalid data provided")

    def add_card(self, card):
        self.credit_card = card

class AdminAccount(Account):
    def __init__(self):
        username = "admin"
        password = "pass"
        super().__init__(username, password)

    def change_username(self, username):
        self.username = username

class CreditCard:
    def __init__(self):
        pass  

account1 = Account('luchicla', 'password1234')
print(f"Account username: {account1.username}; account password: {account1.passwd}")

admin1 = AdminAccount()
print(admin1.username, admin1.passwd)
admin1.change_password("pass", "new pass")
print(admin1.username, admin1.passwd)

credit_card1 = CreditCard()
account1.add_card(credit_card1)
print(account1.credit_card)

admin1.change_username('new username')
print(admin1.username, admin1.passwd)
