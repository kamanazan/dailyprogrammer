from sys import argv
num = argv[1]

angka = {"1":"satu","2":"dua","3":"tiga","4":"empat","5":"lima","6":"enam","7":"tujuh",
		"8":"delapan","9":"sembilan"}

digit = {2:"puluh",3:"ratus",4:"ribu",5:"puluh",7:"juta"}
print "digit:",digit[len(num)]
count = len(num)
if len(num) == 2 and num[0] == "1":
	print angka[num[1]] + "belas"
else:
	for x in num:
		
