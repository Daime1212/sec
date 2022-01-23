import random

def good_password_genrator(length=19):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alphabet += '0123456789'
	alphabet += '!@#$%^&*()_+|'

	password = ''

	for i in range(length):
		password += random.choice(alphabet)
	return password


print(good_password_genrator(19))


