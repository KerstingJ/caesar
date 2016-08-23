def alpha_position(letter):
	'''returns position of ltr on a 0-25 scale'''
	return ord(letter.lower()) - 97

def rotate_char(ltr, num):
	"""rotates letter by num positions"""
	return chr(((alpha_position(ltr)  + num)  % 26) + 97)