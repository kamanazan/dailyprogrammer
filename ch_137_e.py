#challange 137 easy
'''
http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/
it can be helpful sometimes to rotate a string 90-degrees, like a big vertical "SALES" poster or your business name on vertical neon lights, like this image from Las Vegas. Your goal is to write a program that does this, but for multiples lines of text. This is very similar to a Matrix Transposition, since the order we want returned is not a true 90-degree rotation of text.

Author: nint22

#Input Description

You will first be given an integer N which is the number of strings that follows. N will range inclusively from 1 to 16. Each line of text will have at most 256 characters, including the new-line (so at most 255 printable-characters, with the last being the new-line or carriage-return).

#Output Description

Simply print the given lines top-to-bottom. The first given line should be the left-most vertical line.

#Sample Input 1

1
Hello, World!

#Sample Output 1

H
e
l
l
o
,

W
o
r
l
d
!

#Sample Input 2

5
Kernel
Microcontroller
Register
Memory
Operator

#Sample Output 2

KMRMO
eieep
rcgme
nrior
eosra
lctyt
 oe o
 nr r
 t
 r
 o
 l
 l
 e
 r

'''
import sys

num = int(sys.stdin.next())
print num
str_list = []
max_len = 0
for x in range(num):
	tmp = sys.stdin.next().replace('\n','')
	if len(tmp) > max_len:
		max_len = len(tmp)
	str_list.append(tmp)
str_transpose = [[" " for x in xrange(num)] for x in xrange(max_len)]

for x in range(num):
	lgt = len(str_list[x])
	for y in range(max_len):
		if y < lgt:	
			str_transpose[y][x] = str_list[x][y]
	
for a in str_transpose:
	print ''.join(a)
