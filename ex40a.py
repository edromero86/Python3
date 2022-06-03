mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])


# this goes in mystuff.py
def apple():
	print("I AM APPLES!")

import mystuff
mystuff.apple()


def apple():
	print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

import mystuff

mystuff.apple()
print(mystuff.tangerine)



mystuff['apple'] # get apple from dic
mystuff.append() # get apple from module
mystuff.tangerine # same thing, it's just a variable



class MyStuff(object):

	def _init_(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")

		