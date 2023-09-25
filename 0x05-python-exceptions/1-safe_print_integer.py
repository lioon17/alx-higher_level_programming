#!/usr/bin/python3
def safe_print_integer(value):
	try:
		formatted_value = "{:d}".format(value)
		print(formatted_value)
		return True
	except (ValueError, TypeError):
		return False
value = 42
result = safe_print_integer(value)
if result:
	print("Successfully printed an integer.")
else:
	print("Failed to print an integer.")
