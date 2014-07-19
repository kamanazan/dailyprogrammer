input = "18 3C 7E 7E 18 18 18 18"

def process(input):
	hex_list = input.split(" ")
	for hex_val in hex_list:
		bin_val = hex2bin(hex_val)
		draw_ascii(bin_val)

def hex2bin(hex_val):
	return bin(int(hex_val,16))[2:].zfill(8)

def draw_ascii(bin_val):
	ascii_line = []
	for bit in bin_val:
		char = "x" if (bit == "1") else " "
		ascii_line.append(char)
	print "".join(ascii_line)

process(input)


