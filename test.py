import sys

FRENCH_NUMBERS = [
	'zero',
	'un',
	'deux',
	'trois',
	'quatre',
	'cinq',
	'six',
	'sept',
	'huit',
	'neuf',
]

FRENCH_TEN = [
	'',
	'vingt ',
	'trente ',
	'quarante ',
	'cinquante ',
	'soixante ',
	'soixante - ',
	'quatre - vingt ',
	'quatre - vingt - ',
]
FRENCH_NUMBERS_TEN = [
	'dix',
	'onze',
	'douze',
	'treize',
	'quatorze',
	'quinze',
	'seize',
	'dix - sept',
	'dix - huit',
	'dix - neuf'
]

FRENCH_HUNDRED = 'cent '
FRENCH_THOUSAND = 'mille '

def main(scalar:int) -> str:
	if scalar < 0:
		return False

	final_str = ''
	str_scalar = str(scalar)

	if str_scalar == '0':
		return FRENCH_NUMBERS[scalar]

	if len(str_scalar) > 3:
		final_str += process_thousand(str_scalar[0])

	if len(str_scalar) > 2:
		final_str += process_hundred(str_scalar[-3])

	if len(str_scalar) > 1:
		final_str += process_ten(str_scalar[-2])

	try:
		if int(str_scalar[-1]) > 0 and int(str_scalar[-2]) not in [1, 7, 9]:
			final_str += FRENCH_NUMBERS[int(str_scalar[-1])]
		elif int(str_scalar[-1]) > 0 and int(str_scalar[-2]) in [1, 7, 9]:
			final_str += FRENCH_NUMBERS_TEN[int(str_scalar[-1])]
		elif int(str_scalar[-1]) == 0 and int(str_scalar[-2]) in [1, 7, 9]:
			final_str += FRENCH_NUMBERS_TEN[int(str_scalar[-1])]
	except IndexError:
		final_str += FRENCH_NUMBERS[int(str_scalar[-1])]

	return final_str

def process_ten(x:int) -> str:
	x = int(x)
	x = max(0, x-1)
	return FRENCH_TEN[x]

def process_thousand(x:int) -> str:
	x = int(x)
	if x == 1:
		return FRENCH_THOUSAND
	
	return FRENCH_NUMBERS[x] + ' ' + FRENCH_THOUSAND

def process_hundred(x:int) -> str:
	x = int(x)

	if x == 0:
		return ''

	if x == 1:
		return FRENCH_HUNDRED

	return FRENCH_NUMBERS[x] + ' ' + FRENCH_HUNDRED

if __name__ == '__main__':
	num = int(sys.argv[1])
	french = main(num)
	print(french)

	# 1 = un, 2 = deux, 12 = douze, 104 = cent quatre

	# 2285 => deux mille deux cent quatre-vingt cinq
	#		 	FN + TH    FN + FT      FT + FN
	
	# 1170 => mille cent soixante dix