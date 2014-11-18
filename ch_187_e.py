from sys import stdin

comm_dict = {}

c=0

comm = ''
special_comm = {}
inputs = []
for line in stdin:
    inputs.append(line)
c = int(inputs[0])

for args in inputs[1:c+1]:
    arg,desc = args.split(':')
    if arg.startswith('*'):
        arg = arg.replace('*','')
        special_comm[arg]=desc
    comm_dict[arg]=desc
comm = inputs[-1]
print comm_dict
print comm
pending_text = ''
for line in comm.split(' '):

    if line.startswith('--'):
        line = line.replace('--','')
        if line.count('='):
            line,param = line.split('=')
            print 'flag: %s (values: %s)' % (line.strip(),param.strip())
        #if line in special_comm.values():
        #    pending_text = 'flag:%s' % (line)
        else:
            print 'flag:',line
    elif line.startswith('-'):
        line = line.replace('-','')
        line = line.replace('\n','')
        for x in line:
            if x in special_comm.keys():
                pending_text = 'flag: %s' % (comm_dict[x].strip())
            else:
                print 'flag:',comm_dict[x].strip()
    else:
        if pending_text:
            print pending_text,'(values: %s)' % line
            pending_text = ''
        else:
            print 'parameter:',line
