# coding=utf-8
# import AnalysisRates as ar
# import Estimate_1 as es1
import numpy as np
# import LeadStatement as ls
import math as mt
import pandas as pd

pd.set_option('max_colwidth', 0)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)


def conveyance(x):
    'For conveyance of Rough stone, xetal, khoa, chips, moorum, earth and sand etc.(per 1cum.)'
    if x <= 5:
        return 156.4
    elif 5 < x & x <= 50:
        return 156.4 + (x - 5) * 9.2
    else:
        return 156.4 + 45 * 9.2 + 6.5 * (x - 50)


def conveyance_wood(x):
    'For conveyance of wood of 1cum volume'
    if x <= 5:
        return 169.0 / 1.25
    elif 5 < x & x <= 50:
        return (169 + (x - 5) * 8.6) / 1.25
    else:
        return (169 + 45 * 8.6 + (x - 50) * 7.3) / 1.25


def conveyance_cement(x):
    'For conveyance of wood of 1cum volume'
    if x <= 5:
        return 16.9
    elif 5 < x & x <= 50:
        return (16.9 + (x - 5) * 0.86)
    else:
        return (16.9 + 45 * 0.86 + (x - 50) * 0.73)


def conveyance_brick(x):
    'Bricks of 25cm size for 1 no. '
    if x <= 5:
        return 1010.8 / 2000
    elif 5 < x & x <= 50:
        return (1010.8 + (x - 5) * 41.4) / 2000
    else:
        return (1010.8 + 45 * 41.4 + (x - 50) * 33.3) / 2000


m = [['bricks', 1, 'local', 15, 3.38, 0], ['sand', 1, 'Mahanadi', 10, 55.0, 27.5],
     ['course sand', 1, 'Mahanadi', 10, 48.0, 27.5],
     ['cement', 1, 'Binka', 10, 622.00, 0], ['HYSD bar', 1, 'Binka', 10, 4000, 0], ['wood', 1, 'local', 5, 0, 0],
     ['stone', 1, 'Singijuba', 20, 254.0, 98.9], ['10mm c.b.g. chips', 1, 'Singijuba', 30, 1150, 98.9],
     ['12mm c.b.g. chips', 1, 'Singijuba', 30, 1150, 98.9],
     ['20mm c.b.g. chips', 1, 'Singijuba', 30, 1130, 98.9], ['40mm h.g. metal', 1, 'Singijuba',30, 780, 98.9],
     ['moorum',1,'Local',5,50,27.5],['fly ash bricks',1,'local',15,4.2,0]]


def cost_of_material(mm, i, c=['Description', 'qty', 'quarry', 'lead', 'basic cost', 'Royalty']):
    table = pd.DataFrame(mm, index=i, columns=c)
    return table
a = cost_of_material([m[0]], [1])
a.insert(4,'conveyance',conveyance_brick(m[0][3]))
a['qty']=a['qty'].map('{:.0f}no'.format)
b=cost_of_material([m[1]],[2])
b.insert(4,'conveyance',conveyance(m[1][3]))
b['qty']=b['qty'].map('{:.0f}cum'.format)

c=cost_of_material([m[2]],[3])
c.insert(4,'conveyance',conveyance(m[2][3]))
c['qty']=c['qty'].map('{:.0f}cum'.format)

d=cost_of_material([m[3]],[4])
d.insert(4,'conveyance',conveyance_cement(m[3][3]))
d['qty']=d['qty'].map('{:.0f}qtl'.format)

e=cost_of_material([m[4]],[5])
e.insert(4,'conveyance',conveyance_cement(m[4][3]))
e['qty']=e['qty'].map('{:.0f}qtl'.format)

f=cost_of_material([m[5]],[6])
f.insert(4,'conveyance',conveyance_wood(m[5][3]))
f['qty']=f['qty'].map('{:.0f}cum'.format)

g=cost_of_material([m[6]],[7])
g.insert(4,'conveyance',conveyance(m[6][3]))
g['qty']=g['qty'].map('{:.0f}cum'.format)

h=cost_of_material([m[7]],[8])
h.insert(4,'conveyance',conveyance(m[7][3]))
h['qty']=h['qty'].map('{:.0f}cum'.format)

i=cost_of_material([m[8]],[9])
i.insert(4,'conveyance',conveyance(m[8][3]))
i['qty']=i['qty'].map('{:.0f}cum'.format)

j=cost_of_material([m[9]],[10])
j.insert(4,'conveyance',conveyance(m[9][3]))
j['qty']=j['qty'].map('{:.0f}cum'.format)

k=cost_of_material([m[10]],[11])
k.insert(4,'conveyance',conveyance(m[10][3]))
k['qty']=k['qty'].map('{:.0f}cum'.format)

l=cost_of_material([m[11]],[12])
l.insert(4,'conveyance',conveyance(m[11][3]))
l['qty']=l['qty'].map('{:.0f}cum'.format)

n=cost_of_material([m[12]],[13])
n.insert(4,'conveyance',conveyance_brick(m[12][3]))
n['qty']=n['qty'].map('{:.0f}no'.format)


z = a.append(b).append(c).append(d).append(e).append(f).append(g).append(h).append(i).append(j).append(k).append(l).append(n)
z.insert(7,'total cost',z['conveyance']+z['basic cost']+z['Royalty'])



if __name__ == "__main__":
    z['total cost'] = z['total cost'].map('Rs.{:.2f}'.format)
    z['Royalty'] = z['Royalty'].map('Rs.{:.2f}'.format)
    z['basic cost'] = z['basic cost'].map('Rs.{:.2f}'.format)
    z['conveyance'] = z['conveyance'].map('Rs.{:.2f}'.format)
    z['lead'] = z['lead'].map('{:.0f}km'.format)

    print (z,'\n\n\n','The lead of different materials as stated above is least and economical.')
    print ('\n\n\n\tJunior Engineer\t\tAssistant Engineer\t\tBlock Development Officer')
    print ('\tBinka Block Office\tBinka Block Office\t\t\t\tBinka')
