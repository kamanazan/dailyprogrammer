from sys import stdin

candy_lists = []
candy_qty = 0
candy_type = []
candy_stats = {}

for line in stdin:
    candy_lists.append(line.strip())

candy_type = set(candy_lists)

candy_qty = len(candy_lists)

for candy in candy_type:
    candy_stats[candy] = candy_lists.count(candy)
    prcnt = (candy_stats[candy] / float(candy_qty)) * 100
    amount = candy_stats[candy]
    print "Permen: %s ada %d(%.1f%%)" % (candy,amount,prcnt)


