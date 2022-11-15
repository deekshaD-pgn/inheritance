def f(surname,*firstnames):
	print(surname)
	print(firstnames)

def g(*args, **kwargs):
	print('Prepare!')
	f(*args, **kwargs)
	
g('Fitch','Alan','Rachel','Carol')
