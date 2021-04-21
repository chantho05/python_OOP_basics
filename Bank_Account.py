class BankAccount:
	def __init__(self, account_type, amount):
		self.account_type = account_type
		self.amount = amount

	def deposit(self, deposit_amount):
		self.amount += deposit_amount

	def withdraw(self, withdraw_amount):
		self.amount -= withdraw_amount

	def __str__(self):
		return "{} Amount: {}".format(self.account_type, self.amount)



mike = BankAccount("Checkings", 100)

print(mike.account_type)
print(mike.amount)

mike.deposit(30)
print(mike.amount)

mike.withdraw(45)
print(mike)

