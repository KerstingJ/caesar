from helpers import rotate_char
from sys import argv, exit

def encrypt(message, num):
	"""scrambles message by num places"""
	
	scram = ""
	
	for ltr in message:
		if ltr.isalpha() == True and ltr.isupper():
			scram += rotate_char(ltr, num).upper()
			#print(ltr, h.rotate_char(ltr, num))
			
		elif ltr.isalpha() == True:
			scram += rotate_char(ltr, num)
			#print(ltr, h.rotate_char(ltr, num))
			
		else:
			scram += ltr
		

	return scram

def user_input_is_valid(cl_args):
	args = cl_args[1:]
	if len(args) < 2:
		print('enter cypher in format "word", number')
		return False
	if not args[1].isdigit():
		print('enter cypher in format "word", number')
		return False
	return True

#if __name__ == '__main__':
	#if user_input_is_valid(argv) == False:
		#print('enter cypher in format "word", number')
		#exit()
	
	#cyph = encrypt(argv[1], int(argv[2]))
	#print(cyph)
