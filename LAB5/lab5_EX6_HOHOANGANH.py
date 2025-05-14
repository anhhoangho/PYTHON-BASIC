# Hồ Hoàng anh - 22115054122103

datapath = input('input file: ')
outpath = input('output file: ')

outfile = open(outpath, 'w')

with open(datapath, 'r') as datafile:
    name= datafile.readline().strip()
    hours= []
    total = 0
    while True:
        data= datafile.readline().strip()
        if not data:
            break
        if data.isnumric():
            hours.append(int(data))
            total += int(data)
        else:
            total= sum(hours)
            outfile.write(name+': '+','.join(hours))
            outfile.write(' (' +str(total)+')\n')
            name= data
            hours=[]
            total = 0

outfile.write(name+': '+','.join(hours))
outfile.write(' (' +str(total)+')\n')

outfile.close()



