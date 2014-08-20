from sys import argv
num = argv[1]

angka = {"1":"satu","2":"dua","3":"tiga","4":"empat","5":"lima","6":"enam","7":"tujuh",
		"8":"delapan","9":"sembilan"}

digit = {2:"puluh",3:"ratus",4:"ribu",5:"puluh",7:"juta"}
'''
for x in [9,6,3,2,1]:
	if num < 10 ** x:
		if x == 1 and num < 20:
			kpt = "belas"
			break
		else:
			kpt = digit[x]
			break
return kpt,x

def to_word(num):
	if num < 10:
		return angka[num]
	else:
		kpt,x = getKelipatan(num)
		process_num = num / 10 ** x
		sisa = num - (process_num * 10 ** x)
		return 	to_word(process_num) + kpt + to_word(sisa)
'''
print "digit:",digit[len(num)]
count = len(num)
if len(num) == 2 and num[0] == "1":
	print angka[num[1]] + "belas"
else:
	for x in num:
		
