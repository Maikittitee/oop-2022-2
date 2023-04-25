# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    helloexam.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ktunchar <ktunchar@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 09:30:12 by ktunchar          #+#    #+#              #
#    Updated: 2023/04/25 12:59:54 by ktunchar         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import enum
from datetime import datetime

class	Bank:
	def	__init__(self):
		self.users = []
		self.accounts = []
		self.atms = []
		self.atm_cards = []
	
	def	get_account_by_id(self, id):
		for account in self.accounts:
			if (account.account_id == id):
				return (account)
		return (None)


	def	create_new_user(self, name, account_id, pin):
		new_user = User(name, account_id, pin)
		self.users.append(new_user)
		return (new_user)
	
	def	create_new_account(self, user, account_id, remain):
		new_account = Account(account_id, remain)
		user.account_id = new_account.account_id
		self.accounts.append(new_account)
		return (new_account)

	def	create_new_atm(self, id, remain, bank1000 , bank500, bank100):
		new_atm = ATM(id, remain, bank1000 , bank500, bank100)
		self.atms.append(new_atm)
		return (new_atm)
	
	def	is_user_verify(self, user, pin):
		if (user.pin == pin):
			return (1)
		return (0)

class	ATM:
	def	__init__(self, id, remain, bank1000, bank500, bank100):
		self.id = id
		self.remain = remain
		self.bank1000 = bank1000
		self.bank100 = bank100
		self.bank500 = bank500
	
	def	select_activity(self, user):
		print("Select transaction:")
		print("1. Withdraw Cash")
		print("2. Deposite Cash")
		print("3. Transfer Cash")
		print("transaction (1, 2, 3):", end = "")
		ip = int(input())

		print(f"Available balance: {bank.get_account_by_id(user.account_id).remain}")
		if (ip == 1):
			activity = Withdraw()
			print("Enter amount to withdraw: ")
			ip = int(input())
			ac = activity.execute(user, self, ip)
			bank.get_account_by_id(user.account_id).activities.append(ac)
		elif (ip == 2):
			activity = Deposite()
			ac = activity.execute(user, self)
			bank.get_account_by_id(user.account_id).activities.append(ac)
		elif (ip == 3):
			activity = Transfer()
			print("Enter transfer account number: ",end ="")
			dst = str(input())
			ac = activity.execute(user, dst)
			bank.get_account_by_id(user.account_id).activities.append(ac)
		else :
			print("There have only 3 choice for you")
			return (0)
		print(f"Balance: {bank.get_account_by_id(user.account_id).remain}")
		return (ac)
	
	def	show_atm(self):
		print(f"remain: {self.remain}")
		print(f"bank100: {self.bank100}")
		print(f"bank500: {self.bank500}")
		print(f"bank1000: {self.bank1000}")
	    
class ATMCard:
	def	__init__(self, id, name, account_id, exp_date:datetime):
		self.id = id
		self.name = name
		self.account_id = account_id
		self.exp_date = exp_date
		
class User:
	def	__init__(self, name, account_id, pin):
		self.name = name
		self.account_id = account_id
		self.pin = pin
		
	def	insert_card(self, atm, card: ATMCard, user, pin):
		read_account_id = card.account_id
		read_pin = pin
		if (not	bank.is_user_verify(user, read_pin)):
			print("Account Incorrect")
			return (0)
		
		return(atm.select_activity(self))
		
	def	print_transaction(self):
		for ac in bank.get_account_by_id(self.account_id).activities:
			if (ac.typo == ActivityType.WITHDRAW):
				print(f"Withdraw {ac.ip} {ac.status}")
			if (ac.typo == ActivityType.DESPOSITE):
				print(f"Desposite {ac.ip} {ac.status}")
			if (ac.typo == ActivityType.TRANSFER):
				print(f"Transfer {ac.ip} to {ac.to.account_id} {ac.status}")
		
class ActivityType():
	WITHDRAW = 1,
	DESPOSITE = 2,
	TRANSFER = 3

class	ActivityStatus():
	PENDING = 1,
	CANCELED = 2,
	SUCCESS = 3
    

class Activity:
	def	__init__(self, date : datetime, status : ActivityStatus):
		self.date = date
		self.status = status

class Withdraw(Activity):

	def	__init__(self):
		Activity.__init__(self,datetime.now(), ActivityStatus.PENDING)
		self.typo = ActivityType.WITHDRAW

	def	execute(self, user:User, atm:ATM, ip):
		self.ip = ip
		if (atm.remain < ip):
			print("Cash not enough")
			self.status = ActivityStatus.CANCELED
			return (self)
		elif (bank.get_account_by_id(user.account_id).remain < ip):
			print("You have not enough money")
			self.status = ActivityStatus.CANCELED
			return (self) 
		elif (ip % 100 != 0):
			print("There have 100 cash be a mininum")
			self.status = ActivityStatus.CANCELED
			return (self)
		else :
			num = ip 
			bank.get_account_by_id(user.account_id).remain -= num
			self.bank1000 = 0
			self.bank500 = 0
			self.bank100 = 0

			while (num > 0):
				if (atm.bank1000 != 0 and num >= 1000):
					self.bank1000 += 1
					atm.bank1000 -= 1
					atm.remain -= 1000
					num -= 1000
				elif (atm.bank500 != 0 and num >= 500 ):
					self.bank500 += 1
					atm.bank500 -= 1
					atm.remain -= 500
					num -= 500
				elif (atm.bank100 != 0 and num >= 100):
					self.bank100 += 1
					atm.bank100 -= 1
					atm.remain -= 100
					num -= 100
			
			self.status = ActivityStatus.SUCCESS
			return (self)
		
class Transfer(Activity):
	def	__init__(self):
		Activity.__init__(self,datetime.now(), ActivityStatus.PENDING)
		self.typo = ActivityType.TRANSFER

	def	execute(self, user:User, dst_account_id):
		self.ip = 0
		src_account = bank.get_account_by_id(user.account_id)
		dst_account = bank.get_account_by_id(dst_account_id)
		if (not dst_account):
			print("Invalid Transfered account")
			self.status = ActivityStatus.CANCELED
		else:
			self.to = dst_account
			print("Enter amount to Transfer: ", end = "")
			ip = int(input())
			if (bank.get_account_by_id(user.account_id).remain < ip):
				print("You have not enough money")
				self.status = ActivityStatus.CANCELED
			else:
				dst_account.remain += ip
				src_account.remain -= ip
				self.status = ActivityStatus.SUCCESS 
		
		return (self)
	
class	Deposite(Activity):
	def	__init__(self):
		Activity.__init__(self,datetime.now(), ActivityStatus.PENDING)
		self.typo = ActivityType.DESPOSITE

	def	execute(self, user:User, atm:ATM):
		print("Enter amount to Desposite: ", end = "")	
		ip = int(input())
		self.ip = ip
		self.bank1000 = 0
		self.bank500 = 0
		self.bank100 = 0
		print("Number of 1000 bills: ", end = "")
		self.bank1000 = int(input())
		print("Number of 500 bills: ", end = "")
		self.bank500 = int(input())
		print("Number of 100 bills: ", end = "")
		self.bank100 = int(input())
		print("Your desposite has been recieced")
		calculate_from_bank = (1000 * self.bank1000) + (500 * self.bank500) + (100 * self.bank100)
		if (calculate_from_bank != ip):
			print("Your amount and your cash is not match")
			self.status = ActivityStatus.CANCELED
		else:
			atm.bank1000 += self.bank1000
			atm.bank500 += self.bank500
			atm.bank100 += self.bank100
			bank.get_account_by_id(user.account_id).remain += ip
			atm.remain += ip

		return (self)

class	Account:
	def	__init__(self, account_id, remain):
		self.account_id = account_id
		self.remain = remain
		self.activities = []
        
bank = Bank()

user1 = bank.create_new_user("Mai", "65010030", "0030")
user2 = bank.create_new_user("Best", "65010031", "0031")

bank.create_new_account(user1, "65010030", 10000)
bank.create_new_account(user2, "65010031", 0)

card1 = ATMCard("65010030","Mai","65010030",datetime.now())

atm1 = bank.create_new_atm("65010030", 160000, 100, 100, 100)

while (1):
	print("Please insert your card(Y/N)", end = "")
	ip = input()
	if (ip == "y" or ip == "Y"):
		something = user1.insert_card(atm1, card1, user1, "0030")		
	else:
		user1.print_transaction()
		break













        
        