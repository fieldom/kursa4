import lexer

while True:
	text = input('basic > ')
	result, error = lexer.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)