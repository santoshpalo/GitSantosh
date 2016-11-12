#===============================================================================
# print ('''Earth work in hard soil including breaking of clods from 5 to 7cm
#     # in size and laying in layers not exceeding 30cm in height\n''')
#===============================================================================
    #     print( fl.foundation(0)
    #     print( '''\nExcavation of foundation trench in hard soil including
    # dressing of sides and levelling of bed etc. complete.\n'''
    #     print( fl.foundation(1)
    #     fl.sandfilling()
    #     fl.concrete(2)
    #     fl.concrete(3)
    #     fl.rscs(3)
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:01:00 2015

@author: spalo
"""
from imp import reload
import sys
#===============================================================================
# reload(sys)  # Reload does the trick!
# sys.setdefaultencoding('UTF8')
#===============================================================================


import numpy as np
import pandas as pd
import LeadStatement1 as ls

a=200
b=220
c=240
d=260

pd.set_option('display.precision',4)
d1={'quantity':[0.43],
   'rate':[a],
'amount':[0]
   
}
index1=['unskilled labour']
columns =['quantity','rate','amount']
table1 = pd.DataFrame(d1,index = index1,columns = columns)
table1['amount']= table1.quantity*table1.rate
table1['amount'] = table1['amount'].map('\u20B9{:,.2f}'.format)
table1['rate'] = table1['rate'].map('\u20B9{:,.2f}'.format)
table1['quantity'] = table1['quantity'].map('{:,.2f}no.'.format)
#Excavation of foundation in hard soil
d2={'quantity':[0.43*1.2],
   'rate':[a],
'amount':[0]
   
}
index2=['unskilled labour']
columns =['quantity','rate','amount']
table2 = pd.DataFrame(d2,index = index2,columns = columns)
table2['amount']= table2.quantity*table2.rate
table2['rate'] = table2['rate'].map('\u20B9{:,.2f}'.format)
table2['quantity'] = table2['quantity'].map('{:,.2f}no.'.format)
#Cement concrete (1:4:8)
d31={'quantity':[3.9,0.18],
   'rate':[a,c],
'amount':[0]
   
}
index31=['unskilled labour','mason II']
columns =['quantity','rate','amount']
table31 = pd.DataFrame(d31,index = index31,columns = columns)
table31['amount']= table31.quantity*table31.rate
table31['quantity'] = table31['quantity'].map('{:,.2f}no.'.format)

d32={'quantity':[1.72],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index32=['cement']
columns =['quantity','rate','amount']
table32 = pd.DataFrame(d32,index = index32,columns = columns)
table32['amount']= table32.quantity*table32.rate
table32['quantity'] = table32['quantity'].map('{:,.4f}qtl'.format)

d33={'quantity':[0.96,0.48],
    'rate':[ls.z['total cost'][11],ls.z['total cost'][2]],
    'amount':[0,0]}


index33=['40mm h.g metal','sand']
columns =['quantity','rate','amount']
table33 = pd.DataFrame(d33,index = index33,columns = columns)

table33['amount']= table33.quantity*table33.rate
table33['quantity'] = table33['quantity'].map('{:,.2f}cum'.format)

table3 = table31.append(table32).append(table33)
Tamount3 = round(table3.amount.sum(),2)
#Cement concrete (1:3:6)
d41={'quantity':[3.9,0.18],
   'rate':[a,c],
'amount':[0]
   
}
index41=['unskilled labour','mason II']
columns =['quantity','rate','amount']
table41 = pd.DataFrame(d41,index = index41,columns = columns)
table41['amount']= table41.quantity*table41.rate
table41['quantity'] = table41['quantity'].map('{:,.2f}no.'.format)

d42={'quantity':[2.29],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index42=['cement']
columns =['quantity','rate','amount']
table42 = pd.DataFrame(d42,index = index32,columns = columns)
table42['amount']= table42.quantity*table42.rate
table42['quantity'] = table42['quantity'].map('{:,.4f}qtl'.format)

d43={'quantity':[0.96,0.48],
    'rate':[ls.z['total cost'][11],ls.z['total cost'][2]],
 'amount':[0]
    
 }


index43=['40mm h.g metal','sand']
columns =['quantity','rate','amount']
table43 = pd.DataFrame(d43,index = index33,columns = columns)

table43['amount']= table43.quantity*table33.rate
table43['quantity'] = table43['quantity'].map('{:,.2f}cum'.format)

table4 = table41.append(table42).append(table43)
Tamount4 = round(table4.amount.sum(),2)
#cement concrete (1:2:4)
d51={'quantity':[4.6,0.68],
   'rate':[a,c],
'amount':[0]
   
}
index51=['unskilled labour','mason II']
columns =['quantity','rate','amount']
table51 = pd.DataFrame(d51,index = index51,columns = columns)
table51['amount']= table51.quantity*table51.rate
table51['quantity'] = table51['quantity'].map('{:,.2f}no.'.format)

d52={'quantity':[3.24],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index52=['cement']
columns =['quantity','rate','amount']
table52 = pd.DataFrame(d52,index = index52,columns = columns)
table52['amount']= table52.quantity*table52.rate
table52['quantity'] = table52['quantity'].map('{:,.4f}qtl'.format)

d53={'quantity':[0.9,0.45],
    'rate':[ls.z['total cost'][10],ls.z['total cost'][2]],
 'amount':[0]
    
 }


index53=['12mm c.b.g. chips','sand']
columns =['quantity','rate','amount']
table53 = pd.DataFrame(d53,index = index53,columns = columns)

table53['amount']= table53.quantity*table53.rate
table53['quantity'] = table53['quantity'].map('{:,.2f}cum'.format)

table5 = table51.append(table52).append(table53)
Tamount5 = round(table5.amount.sum(),2)
#Cement concrete (1:1.5:3)
d61={'quantity':[4.6,0.68],
   'rate':[a,c],
'amount':[0]
   
}
index61=['unskilled labour','mason II']
columns =['quantity','rate','amount']
table61 = pd.DataFrame(d61,index = index51,columns = columns)
table61['amount']= table61.quantity*table51.rate
table61['quantity'] = table61['quantity'].map('{:,.2f}no.'.format)

d62={'quantity':[4.29],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index62=['cement']
columns =['quantity','rate','amount']
table62 = pd.DataFrame(d62,index = index62,columns = columns)
table62['amount']= table62.quantity*table62.rate
table62['quantity'] = table62['quantity'].map('{:,.4f}qtl'.format)

d63={'quantity':[0.9,0.45],
    'rate':[ls.z['total cost'][10],ls.z['total cost'][2]],
 'amount':[0]
    
 }


index63=['12mm c.b.g. chips','sand']
columns =['quantity','rate','amount']
table63 = pd.DataFrame(d63,index = index63,columns = columns)

table63['amount']= table63.quantity*table63.rate
table63['quantity'] = table63['quantity'].map('{:,.2f}cum'.format)

table6 = table61.append(table62).append(table63)
Tamount6 = round(table6.amount.sum(),2)
#R.C.C. M-20grade concrete
d71={'quantity':[20.0/15,0.86/15,1.5/15],
   'rate':[a,b,c],
'amount':[0]
   
}
index71=['unskilled labour','mate','mason II']
columns =['quantity','rate','amount']
table71 = pd.DataFrame(d71,index = index71,columns = columns)
table71['amount']= table71.quantity*table71.rate
table71['quantity'] = table71['quantity'].map('{:,.2f}no.'.format)

d72={'quantity':[5.21*10/15],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index72=['cement']
columns =['quantity','rate','amount']
table72 = pd.DataFrame(d72,index = index72,columns = columns)
table72['amount']= table72.quantity*table72.rate
table72['quantity'] = table72['quantity'].map('{:,.4f}qtl'.format)

d73={'quantity':[8.1/15,5.4/15,0.45],
    'rate':[ls.z['total cost'][10],ls.z['total cost'][8],ls.z['total cost'][2]],
 'amount':[0]
    
 }


index73=['20mm c.b.g. chips','10mm c.b.g. chips','sand']
columns =['quantity','rate','amount']
table73 = pd.DataFrame(d73,index = index73,columns = columns)

table73['amount']= table73.quantity*table73.rate
table73['quantity'] = table73['quantity'].map('{:,.2f}cum'.format)
d74={'quantity':[0.4,0.4],
    'rate':[200.0,177.00],
 'amount':[0]
    
 }


index74=['33KVA generator','Concrete Mixer']
columns =['quantity','rate','amount']
table74 = pd.DataFrame(d74,index = index74,columns = columns)

table74['amount']= table74.quantity*table74.rate
table74['quantity'] = table74['quantity'].map('{:,.2f}cum'.format)

table7 = table71.append(table72).append(table73).append(table74)
Tamount7 = round(table7.amount.sum(),2)
#R.C.C. M-25grade concrete
d81={'quantity':[20.0/15,0.86/15,1.5/15],
   'rate':[a,b,c],
'amount':[0]
   
}
index81=['unskilled labour','mate','mason II']
columns =['quantity','rate','amount']
table81 = pd.DataFrame(d81,index = index81,columns = columns)
table81['amount']= table81.quantity*table81.rate
table81['quantity'] = table81['quantity'].map('{:,.2f}no.'.format)

d82={'quantity':[6.05*10/15],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index82=['cement']
columns =['quantity','rate','amount']
table82 = pd.DataFrame(d82,index = index82,columns = columns)
table82['amount']= table82.quantity*table82.rate
table82['quantity'] = table82['quantity'].map('{:,.4f}qtl'.format)

d83={'quantity':[8.1/15,5.4/15,0.45],
    'rate':[ls.z['total cost'][10],ls.z['total cost'][8],ls.z['total cost'][2]],
 'amount':[0]
    
 }

index83=['20mm c.b.g. chips','10mm c.b.g. chips','sand']
columns =['quantity','rate','amount']
table83 = pd.DataFrame(d83,index = index73,columns = columns)

table83['amount']= table83.quantity*table83.rate
table83['quantity'] = table83['quantity'].map('{:,.2f}cum'.format)
d84={'quantity':[0.4,0.4],
    'rate':[c,177.00],
 'amount':[0]
   
 }

index84=['33KVA generator','Concrete Mixer']
columns =['quantity','rate','amount']
table84 = pd.DataFrame(d84,index = index84,columns = columns)

table84['amount']= table84.quantity*table84.rate
table84['quantity'] = table84['quantity'].map('{:,.2f}cum'.format)

table8 = table81.append(table82).append(table83).append(table84)
Tamount8 = round(table8.amount.sum(),2)
#Reinforcement works
d91={'quantity':[0.8,0.044,0.3],
   'rate':[a,b,d],
'amount':[0]
   
}
index91=['unskilled labour','mate','mason I']
columns =['quantity','rate','amount']
table91 = pd.DataFrame(d91,index = index91,columns = columns)
table91['amount']= table91.quantity*table91.rate
table91['quantity'] = table91['quantity'].map('{:,.2f}no.'.format)

d92={'quantity':[1.05],
    'rate':[ls.z['total cost'][5]],
 'amount':[0]
    
 }
index92=['HYSD bar']
columns =['quantity','rate','amount']
table92 = pd.DataFrame(d92,index = index92,columns = columns)
table92['amount']= table92.quantity*table92.rate
table92['quantity'] = table92['quantity'].map('{:,.4f}qtl'.format)

d93={'quantity':[0.8],
    'rate':[75],
 'amount':[0]
    
 }

index93=['M.S. binding wire']
columns =['quantity','rate','amount']
table93 = pd.DataFrame(d93,index = index93,columns = columns)

table93['amount']= table93.quantity*table93.rate
table93['quantity'] = table93['quantity'].map('{:,.2f}kg'.format)
table9 = table91.append(table92).append(table93)
Tamount9 = round(table9.amount.sum(),2)
#Rigid and smooth centering and shuttering
#Slab and chajja

d101={'quantity':[2.75,2.75],
   'rate':[b,c],
'amount':[0]
   
}
index101=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table101 = pd.DataFrame(d101,index = index101,columns = columns)
table101['amount']= table101.quantity*table101.rate
table101['quantity'] = table101['quantity'].map('{:,.2f}no.'.format)

d102={'quantity':[56],
    'rate':[104],
 'amount':[0]
    
 }
index102=['120mm dia sal bullah']
columns =['quantity','rate','amount']
table102 = pd.DataFrame(d102,index = index102,columns = columns)
table102['amount']= table102.quantity*table102.rate
table102['quantity'] = table102['quantity'].map('{:,.2f}m'.format)

d103={'quantity':[0.112,0.34,1.142],
    'rate':[19650,19650,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index103=['Non Sal wood scantling','planks 38mm','Carriage of wood']
columns =['quantity','rate','amount']
table103 = pd.DataFrame(d103,index = index103,columns = columns)

table103['amount']= table103.quantity*table103.rate
table103['quantity'] = table103['quantity'].map('{:,.2f}cum'.format)
table10 = table103.append(table102)
Tamount10= round(table10.amount.sum(),2)
Tamount101=round(table101.amount.sum(),2)
Tamount104=Tamount10/10+Tamount101
    
#R.C.C. stairs

d111={'quantity':[2.75,2.75],
   'rate':[b,c],
'amount':[0]
   
}
index111=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table111 = pd.DataFrame(d111,index = index101,columns = columns)
table111['amount']= table111.quantity*table111.rate
table111['quantity'] = table111['quantity'].map('{:,.2f}no.'.format)

d112={'quantity':[6.5],
    'rate':[60],
 'amount':[0]
    
 }
index112=['120mm dia non sal bullah']
columns =['quantity','rate','amount']
table112 = pd.DataFrame(d112,index = index112,columns = columns)
table112['amount']= table112.quantity*table112.rate
table112['quantity'] = table112['quantity'].map('{:,.2f}m'.format)

d113={'quantity':[0.039,0.238,0.35],
    'rate':[19650,19650,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index113=['Non Sal wood scantling','planks 38mm','Carriage of wood']
columns =['quantity','rate','amount']
table113 = pd.DataFrame(d113,index = index113,columns = columns)

table113['amount']= table113.quantity*table113.rate
table113['quantity'] = table113['quantity'].map('{:,.2f}cum'.format)
table11 = table113.append(table112)
Tamount11= round(table11.amount.sum(),2)
#R.C.C. plinth bend and footings

d121={'quantity':[0.5,0.5],
   'rate':[b,c],
'amount':[0]
   
}
index121=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table121 = pd.DataFrame(d121,index = index121,columns = columns)
table121['amount']= table121.quantity*table121.rate
table121['quantity'] = table121['quantity'].map('{:,.2f}no.'.format)

d123={'quantity':[12.6],
    'rate':[49.0],
 'amount':[0]
    
 }
index123=['80mm dia non sal bullah']
columns =['quantity','rate','amount']
table123 = pd.DataFrame(d123,index = index123,columns = columns)
table123['amount']= table123.quantity*table123.rate
table123['quantity'] = table123['quantity'].map('{:,.2f}m'.format)

d123={'quantity':[0.267,0.3284],
    'rate':[19650.0,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index123=['non sal planks 25mm','Carriage of wood']
columns =['quantity','rate','amount']
table123 = pd.DataFrame(d123,index = index123,columns = columns)

table123['amount']= table123.quantity*table123.rate
table123['quantity'] = table123['quantity'].map('{:,.2f}cum'.format)
table12 = table123.append(table123)
Tamount12= round(table12.amount.sum(),2)
#R.C.C. plinth bend and footings

d121={'quantity':[0.5,0.5],
   'rate':[b,c],
'amount':[0]
   
}
index121=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table121 = pd.DataFrame(d121,index = index121,columns = columns)
table121['amount']= table121.quantity*table121.rate
table121['quantity'] = table121['quantity'].map('{:,.2f}no.'.format)

d122={'quantity':[12.6],
    'rate':[49.0],
 'amount':[0]
    
 }
index122=['80mm dia non sal bullah']
columns =['quantity','rate','amount']
table122 = pd.DataFrame(d122,index = index122,columns = columns)
table122['amount']= table122.quantity*table122.rate
table122['quantity'] = table122['quantity'].map('{:,.2f}m'.format)

d123={'quantity':[0.267,0.3284],
    'rate':[19650.0,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index123=['non sal planks 25mm','Carriage of wood']
columns =['quantity','rate','amount']
table123 = pd.DataFrame(d123,index = index123,columns = columns)

table123['amount']= table123.quantity*table123.rate
table123['quantity'] = table123['quantity'].map('{:,.4f}cum'.format)
table12 = table122.append(table123)
Tamount12= round(table12.amount.sum(),2)
Tamount121=round(table121.amount.sum(),2)
Tamount124=Tamount12/10+Tamount121
    
#R.C.C. beams, columns, grider and bressmer etc. 

d131={'quantity':[2.75,2.75],
   'rate':[b,c],
'amount':[0]
   
}
index131=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table131 = pd.DataFrame(d131,index = index131,columns = columns)
table131['amount']= table131.quantity*table131.rate
table131['quantity'] = table131['quantity'].map('{:,.2f}no.'.format)

d132={'quantity':[15.6,8.00],
    'rate':[104.0,104.0],
 'amount':[0]
    
 }
index132=['120mm dia sal bullah','80mm dia non sal bullah']
columns =['quantity','rate','amount']
table132 = pd.DataFrame(d132,index = index132,columns = columns)
table132['amount']= table132.quantity*table132.rate
table132['quantity'] = table132['quantity'].map('{:,.2f}m'.format)

d133={'quantity':[0.218,0.456],
    'rate':[19650.0,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index133=['non sal planks 38mm','Carriage of wood']
columns =['quantity','rate','amount']
table133 = pd.DataFrame(d133,index = index133,columns = columns)

table133['amount']= table133.quantity*table133.rate
table133['quantity'] = table133['quantity'].map('{:,.2f}cum'.format)
table13 = table133.append(table132)
Tamount13= round(table13.amount.sum(),2)
Tamount131=round(table131.amount.sum(),2)
Tamount134=Tamount13/10+Tamount131
    
#R.C.C. lintels 

d141={'quantity':[1.25,1.25],
   'rate':[b,c],
'amount':[0]
   
}
index141=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table141 = pd.DataFrame(d141,index = index141,columns = columns)
table141['amount']= table141.quantity*table141.rate
table141['quantity'] = table141['quantity'].map('{:,.2f}no.'.format)

d142={'quantity':[21.0],
    'rate':[60.0],
 'amount':[0]
    
 }
index142=['120mm dia non sal bullah']
columns =['quantity','rate','amount']
table142 = pd.DataFrame(d142,index = index142,columns = columns)
table142['amount']= table142.quantity*table142.rate
table142['quantity'] = table142['quantity'].map('{:,.2f}m'.format)

d143={'quantity':[0.413,0.689],
    'rate':[19650.0,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index143=['non sal planks 38mm','Carriage of wood']
columns =['quantity','rate','amount']
table143 = pd.DataFrame(d143,index = index143,columns = columns)

table143['amount']= table143.quantity*table143.rate
table143['quantity'] = table143['quantity'].map('{:,.2f}cum'.format)
table14 = table143.append(table142)
Tamount14= round(table14.amount.sum(),2)
Tamount141=round(table141.amount.sum(),2)
Tamount144=Tamount14/10+Tamount141
#R.C.C. walls and fins including attached pillasters Data for 23.90 sqm
d151={'quantity':[13.5,13.5],
   'rate':[b,c],
'amount':[0]
   
}
index151=['semiskilled labour','mason II']
columns =['quantity','rate','amount']
table151 = pd.DataFrame(d151,index = index151,columns = columns)
table151['amount']= table151.quantity*table151.rate
table151['quantity'] = table151['quantity'].map('{:,.2f}no.'.format)

d152={'quantity':[100.8],
    'rate':[60.0],
 'amount':[0]
    
 }
index152=['120mm dia non sal bullah']
columns =['quantity','rate','amount']
table152 = pd.DataFrame(d152,index = index152,columns = columns)
table152['amount']= table152.quantity*table152.rate
table152['quantity'] = table152['quantity'].map('{:,.2f}m'.format)

d153={'quantity':[0.954,0.269,2.4161],
    'rate':[19650.0,19650.0,ls.z['total cost'][6]],
 'amount':[0]
    
 }

index153=['non sal planks 38mm','non sal wood scantling','Carriage of wood']
columns =['quantity','rate','amount']
table153 = pd.DataFrame(d153,index = index153,columns = columns)

table153['amount']= table153.quantity*table153.rate
table153['quantity'] = table153['quantity'].map('{:,.2f}cum'.format)
table15 = table153.append(table152)
Tamount15= round(table15.amount.sum(),2)
#R.R.H.G. stone masonry in c.m.(1:6)
d161={'quantity':[0.35,1.41,3.17],
   'rate':[d,c,a],
'amount':[0]
   
}
index161=['mason I','mason II','unskilled labour']
columns =['quantity','rate','amount']
table161 = pd.DataFrame(d161,index = index161,columns = columns)
table161['amount']= table161.quantity*table161.rate
table161['quantity'] = table161['quantity'].map('{:,.2f}no.'.format)

d162={'quantity':[0.8151],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index162=['cement']
columns =['quantity','rate','amount']
table162 = pd.DataFrame(d162,index = index162,columns = columns)
table162['amount']= table162.quantity*table162.rate
table162['quantity'] = table162['quantity'].map('{:,.4f}qtl'.format)

d163={'quantity':[1.0,0.34],
    'rate':[ls.z['total cost'][7],ls.z['total cost'][2]],
 'amount':[0]
    
 }


index163=['Rough stone granite quarried','sand']
columns =['quantity','rate','amount']
table163 = pd.DataFrame(d163,index = index163,columns = columns)

table163['amount']= table163.quantity*table163.rate
table163['quantity'] = table163['quantity'].map('{:,.2f}cum'.format)

table16 = table161.append(table162).append(table163)
Tamount16 = round(table16.amount.sum(),2)

#C.R.H.G. stone masonry in c.m.(1:6)
d171={'quantity':[0.35+2.47,1.41,1.41,1.41+0.25],
   'rate':[d,c,b,a],
'amount':[0]
   
}
index171=['mason I','mason II','semi skilled labour','unskilled labour']
columns =['quantity','rate','amount']
table171 = pd.DataFrame(d171,index = index171,columns = columns)
table171['amount']= table171.quantity*table171.rate
table171['quantity'] = table171['quantity'].map('{:,.2f}no.'.format)

d172={'quantity':[0.572],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index172=['cement']
columns =['quantity','rate','amount']
table172 = pd.DataFrame(d172,index = index172,columns = columns)
table172['amount']= table172.quantity*table172.rate
table172['quantity'] = table172['quantity'].map('{:,.4f}qtl'.format)

d173={'quantity':[1.0,0.24],
    'rate':[ls.z['total cost'][7],ls.z['total cost'][2]],
 'amount':[0]
    
 }


index173=['Rough stone granite quarried','sand']
columns =['quantity','rate','amount']
table173 = pd.DataFrame(d173,index = index173,columns = columns)

table173['amount']= table173.quantity*table173.rate
table173['quantity'] = table173['quantity'].map('{:,.2f}cum'.format)

table17 = table171.append(table172).append(table173)
Tamount17 = round(table17.amount.sum(),2)
#Brick masonry in c.m. (1:6) using c.b. bricks in fndn and plinth
d181={'quantity':[0.35,1.41,2.96,350],
   'rate':[d,c,a,ls.z['total cost'][1]],
'amount':[0]
   
}
index181=['mason I','mason II','unskilled labour','c.b. bricks']
columns =['quantity','rate','amount']
table181 = pd.DataFrame(d181,index = index181,columns = columns)
table181['amount']= table181.quantity*table181.rate
table181['quantity'] = table181['quantity'].map('{:,.2f}no.'.format)

d182={'quantity':[0.672],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index182=['cement']
columns =['quantity','rate','amount']
table182 = pd.DataFrame(d182,index = index182,columns = columns)
table182['amount']= table182.quantity*table182.rate
table182['quantity'] = table182['quantity'].map('{:,.4f}qtl'.format)

d183={'quantity':[0.24],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index183=['sand']
columns =['quantity','rate','amount']
table183 = pd.DataFrame(d183,index = index183,columns = columns)

table183['amount']= table183.quantity*table183.rate
table183['quantity'] = table183['quantity'].map('{:,.2f}cum'.format)

table18 = table181.append(table182).append(table183)
Tamount18 = round(table18.amount.sum(),2)
#Brick masonry in c.m. (1:6) using fly ash bricks in fndn and plinth
d281={'quantity':[0.35,1.41,2.96,350],
   'rate':[d,c,a,ls.z['total cost'][13]],
'amount':[0]
   
}
index281=['mason I','mason II','unskilled labour','c.b. bricks']
columns =['quantity','rate','amount']
table281 = pd.DataFrame(d281,index = index281,columns = columns)
table281['amount']= table281.quantity*table281.rate
table281['quantity'] = table281['quantity'].map('{:,.2f}no.'.format)

d282={'quantity':[0.672],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index282=['cement']
columns =['quantity','rate','amount']
table282 = pd.DataFrame(d282,index = index282,columns = columns)
table282['amount']= table282.quantity*table282.rate
table282['quantity'] = table282['quantity'].map('{:,.4f}qtl'.format)

d283={'quantity':[0.24],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index283=['sand']
columns =['quantity','rate','amount']
table283 = pd.DataFrame(d283,index = index283,columns = columns)

table283['amount']= table283.quantity*table283.rate
table283['quantity'] = table283['quantity'].map('{:,.2f}cum'.format)

table28 = table281.append(table282).append(table283)
Tamount28 = round(table28.amount.sum(),2)

#12mm thick cement mortar plaster on brick masonry walls
d191={'quantity':[0.14,0.12],
   'rate':[c,a],
'amount':[0]
   
}
index191=['mason II','unskilled labour']
columns =['quantity','rate','amount']
table191 = pd.DataFrame(d191,index = index191,columns = columns)
table191['amount']= table191.quantity*table191.rate
table191['quantity'] = table191['quantity'].map('{:,.2f}no.'.format)

d192={'quantity':[0.0358],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index192=['cement']
columns =['quantity','rate','amount']
table192 = pd.DataFrame(d192,index = index192,columns = columns)
table192['amount']= table192.quantity*table192.rate
table192['quantity'] = table192['quantity'].map('{:,.4f}qtl'.format)

d193={'quantity':[0.015],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index193=['sand']
columns =['quantity','rate','amount']
table193 = pd.DataFrame(d193,index = index193,columns = columns)

table193['amount']= table193.quantity*table193.rate
table193['quantity'] = table193['quantity'].map('{:,.3f}cum'.format)

table19 = table191.append(table192).append(table193)
Tamount19 = round(table19.amount.sum(),2)
#16mm thick cement mortar plaster on brick masonry walls
d201={'quantity':[0.16,0.24],
   'rate':[c,a],
'amount':[0]
   
}
index201=['mason II','unskilled labour']
columns =['quantity','rate','amount']
table201 = pd.DataFrame(d201,index = index201,columns = columns)
table201['amount']= table201.quantity*table201.rate
table201['quantity'] = table201['quantity'].map('{:,.2f}no.'.format)

d202={'quantity':[0.043],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index202=['cement']
columns =['quantity','rate','amount']
table202 = pd.DataFrame(d202,index = index202,columns = columns)
table202['amount']= table202.quantity*table202.rate
table202['quantity'] = table202['quantity'].map('{:,.4f}qtl'.format)

d203={'quantity':[0.018],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index203=['sand']
columns =['quantity','rate','amount']
table203 = pd.DataFrame(d203,index = index203,columns = columns)

table203['amount']= table203.quantity*table203.rate
table203['quantity'] = table203['quantity'].map('{:,.3f}cum'.format)

table20 = table201.append(table202).append(table203)
Tamount20 = round(table20.amount.sum(),2)
#20mm thick cement mortar plaster on brick masonry walls
d211={'quantity':[0.16,0.24],
   'rate':[c,a],
'amount':[0]
   
}
index211=['mason II','unskilled labour']
columns =['quantity','rate','amount']
table211 = pd.DataFrame(d211,index = index201,columns = columns)
table211['amount']= table211.quantity*table201.rate
table211['quantity'] = table211['quantity'].map('{:,.2f}no.'.format)

d212={'quantity':[0.057],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index212=['cement']
columns =['quantity','rate','amount']
table212 = pd.DataFrame(d212,index = index212,columns = columns)
table212['amount']= table212.quantity*table212.rate
table212['quantity'] = table212['quantity'].map('{:,.4f}qtl'.format)

d213={'quantity':[0.021],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index213=['sand']
columns =['quantity','rate','amount']
table213 = pd.DataFrame(d213,index = index213,columns = columns)

table213['amount']= table213.quantity*table203.rate
table213['quantity'] = table213['quantity'].map('{:,.3f}cum'.format)

table21 = table211.append(table212).append(table213)
Tamount21 = round(table21.amount.sum(),2)
#6mm thick cement mortar plaster on brick masonry walls
d221={'quantity':[0.14,0.17],
   'rate':[c,a],
'amount':[0]
   
}
index221=['mason II','unskilled labour']
columns =['quantity','rate','amount']
table221 = pd.DataFrame(d221,index = index201,columns = columns)
table221['amount']= table221.quantity*table201.rate
table221['quantity'] = table221['quantity'].map('{:,.2f}no.'.format)

d222={'quantity':[0.0372],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index222=['cement']
columns =['quantity','rate','amount']
table222 = pd.DataFrame(d222,index = index222,columns = columns)
table222['amount']= table222.quantity*table222.rate
table222['quantity'] = table222['quantity'].map('{:,.4f}qtl'.format)

d223={'quantity':[0.0075],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index223=['sand']
columns =['quantity','rate','amount']
table223 = pd.DataFrame(d223,index = index223,columns = columns)

table223['amount']= table223.quantity*table203.rate
table223['quantity'] = table223['quantity'].map('{:,.4f}cum'.format)

table22 = table221.append(table222).append(table223)
Tamount22 = round(table22.amount.sum(),2)

#12mm thick cement mortar(1:4) plaster on concrete surfaces
d231={'quantity':[0.14,0.17],
   'rate':[c,a],
'amount':[0]
   
}
index231=['mason II','unskilled labour']
columns =['quantity','rate','amount']
table231 = pd.DataFrame(d231,index = index231,columns = columns)
table231['amount']= table231.quantity*table231.rate
table231['quantity'] = table231['quantity'].map('{:,.2f}no.'.format)

d232={'quantity':[0.0543],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index232=['cement']
columns =['quantity','rate','amount']
table232 = pd.DataFrame(d232,index = index232,columns = columns)
table232['amount']= table232.quantity*table232.rate
table232['quantity'] = table232['quantity'].map('{:,.4f}qtl'.format)

d233={'quantity':[0.015],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index233=['sand']
columns =['quantity','rate','amount']
table233 = pd.DataFrame(d233,index = index233,columns = columns)

table233['amount']= table233.quantity*table233.rate
table233['quantity'] = table233['quantity'].map('{:,.3f}cum'.format)

table23 = table231.append(table232).append(table233)
Tamount23 = round(table23.amount.sum(),2)
#20mm thick cement mortar(1:4) plaster on concrete surfaces
d241={'quantity':[0.16,0.24],
   'rate':[c,a],
'amount':[0]
   
}
index241=['mason II','unskilled labour']
columns =['quantity','rate','amount']
table241 = pd.DataFrame(d241,index = index241,columns = columns)
table241['amount']= table241.quantity*table241.rate
table241['quantity'] = table241['quantity'].map('{:,.2f}no.'.format)

d242={'quantity':[0.0744],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index242=['cement']
columns =['quantity','rate','amount']
table242 = pd.DataFrame(d242,index = index242,columns = columns)
table242['amount']= table242.quantity*table242.rate
table242['quantity'] = table242['quantity'].map('{:,.4f}qtl'.format)

d243={'quantity':[0.021],
    'rate':[ls.z['total cost'][2]],
 'amount':[0]
    
 }


index243=['sand']
columns =['quantity','rate','amount']
table243 = pd.DataFrame(d243,index = index243,columns = columns)

table243['amount']= table243.quantity*table243.rate
table243['quantity'] = table243['quantity'].map('{:,.3f}cum'.format)

table24 = table241.append(table242).append(table243)
Tamount24 = round(table24.amount.sum(),2)
#A.S. flooring 2.5cm thick using c.c.(1:2:4)
d251={'quantity':[0.13,0.36],
   'rate':[d,a],
'amount':[0]
   
}
index251=['mason I','unskilled labour']
columns =['quantity','rate','amount']
table251 = pd.DataFrame(d251,index = index251,columns = columns)
table251['amount']= table251.quantity*table251.rate
table251['quantity'] = table251['quantity'].map('{:,.2f}no.'.format)

d252={'quantity':[0.0858],
    'rate':[ls.z['total cost'][4]],
 'amount':[0]
    
 }
index252=['cement']
columns =['quantity','rate','amount']
table252 = pd.DataFrame(d252,index = index252,columns = columns)
table252['amount']= table252.quantity*table252.rate
table252['quantity'] = table252['quantity'].map('{:,.4f}qtl'.format)

d253={'quantity':[0.012,0.023],
    'rate':[ls.z['total cost'][2],ls.z['total cost'][9]],
 'amount':[0]
    
 }


index253=['sand','12mm c.b.g. chips']
columns =['quantity','rate','amount']
table253 = pd.DataFrame(d253,index = index253,columns = columns)

table253['amount']= table253.quantity*table253.rate
table253['quantity'] = table253['quantity'].map('{:,.3f}cum'.format)

table25 = table251.append(table252).append(table253)
Tamount25 = round(table25.amount.sum(),2)
#painting with priming
d261={'quantity':[1.25/9.3,1.6/9.3],
   'rate':[d,a],
'amount':[0]
   
}
index261=['painter I','unskilled labour']
columns =['quantity','rate','amount']
table261 = pd.DataFrame(d261,index = index261,columns = columns)
table261['amount']= table261.quantity*table261.rate
table261['quantity'] = table261['quantity'].map('{:,.2f}no.'.format)

d262={'quantity':[0.125,0.054],
    'rate':[249.0,116.0],
 'amount':[0]
    
 }
index262=['paint','primer']
columns =['quantity','rate','amount']
table262 = pd.DataFrame(d262,index = index262,columns = columns)
table262['amount']= table262.quantity*table262.rate
table262['quantity'] = table262['quantity'].map('{:,.4f}l'.format)

d263={'quantity':[0.012,0.023],
    'rate':[ls.z['total cost'][2],ls.z['total cost'][10]],
 'amount':[0]
    
 }


index263=['sand','12mm c.b.g. chips']
columns =['quantity','rate','amount']
table263 = pd.DataFrame(d263,index = index263,columns = columns)

table263['amount']= table263.quantity*table263.rate
table263['quantity'] = table263['quantity'].map('{:,.3f}cum'.format)

table26 = table261.append(table262)
Tamount26 = round(table26.amount.sum(),2)
#Water proofing cement paint
d271={'quantity':[.022,0.032],
   'rate':[d,a],
'amount':[0]
   
}
index271=['painter I','unskilled labour']
columns =['quantity','rate','amount']
table271 = pd.DataFrame(d271,index = index271,columns = columns)
table271['amount']= table271.quantity*table271.rate
table271['quantity'] = table271['quantity'].map('{:,.2f}no.'.format)

d272={'quantity':[0.25],
    'rate':[35.0],
 'amount':[0]
    
 }
index272=['w.p.c.paint']
columns =['quantity','rate','amount']
table272 = pd.DataFrame(d272,index = index272,columns = columns)
table272['amount']= table272.quantity*table272.rate
table272['quantity'] = table272['quantity'].map('{:,.4f}l'.format)

d273={'quantity':[0.012,0.023],
   'rate':[ls.z['total cost'][2],ls.z['total cost'][10]],
'amount':[0]

}


index273=['sand','12mm c.b.g. chips']
columns =['quantity','rate','amount']
table273 = pd.DataFrame(d273,index = index273,columns = columns)

table273['amount']= table273.quantity*table273.rate
table273['quantity'] = table273['quantity'].map('{:,.3f}cum'.format)

table27 = table271.append(table272)
Tamount27 = round(table27.amount.sum(),2)





















if __name__ == "__main__":
    print( '\t\t\tANALYSIS OF RATES')
    print( ' _'*40)
    print( '''Name of the work:-Construction of  centre at Baunsuni Talipada
    ''')
    print( '-'*75)
    print( 'Estimated Cost:-',('\u20B92,00,000.00\t\tHead of Account:-Biju K.B.K.(2016-17)'))
    print( '-'*75)
#===============================================================================
# #===============================================================================
# #     print( '''Earth work in hard soil including rough dressing, breaking of clods from
#===============================================================================
# 5 to 7cm in size and laying in layers not exceeding 30cm. in height,
# within intial lead of 50m and lift 1.50m etc. complete.''')
#     print( table1)
#===============================================================================
    print( '''\nExcavation of foundation trench in hard soil including dressing of sides
and levelling of bed and depositing the excavated earth within initial lead of
50.0m and lift of 1.50m etc. complete.''')

    table2['amount'] = table2['amount'].map('\u20B9{:,.2f}'.format)

    print( table2)
    print( '''\nCement concrete (1:4:8) using 40mm size h.g. metal including cost,
conveyance and royalty etc. complete,''')
    table3['amount'] = table3['amount'].map('\u20B9{:,.2f}'.format)
    table3['rate']=table3['rate'].map('\u20B9{:,.2f}'.format)
    print( table3)
    print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount3)
    #==========
#===============================================================================
#     print( '''\nCement concrete (1:3:6) using 40mm size h.g. metal including cost,
# conveyance and royalty etc. complete,''')
#     table4['amount'] = table4['amount'].map('\u20B9{:,.2f}'.format)
#     table4['rate']=table4['rate'].map('\u20B9{:,.2f}'.format)
#     print( table4)
#     print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount4)
#===============================================================================
#===============================================================================
#     print( '''\nCement concrete (1:2:4) using 12mm size c.b.g. chips including cost,
# conveyance and royalty etc. complete,''')
#     table5['amount'] = table5['amount'].map('\u20B9{:,.2f}'.format)
#     table5['rate']=table5['rate'].map('\u20B9{:,.2f}'.format)
#     print( table5)
#     print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount5)
#     print( '''\nCement concrete (1:1.5:3) using 12mm size c.b.g. chips including cost,
# conveyance and royalty etc. complete,''')
#     table6['amount'] = table6['amount'].map('\u20B9{:,.2f}'.format)
#     table6['rate']=table6['rate'].map('\u20B9{:,.2f}'.format)
#     print( table6)
#     print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount6)
#===============================================================================
    print( '''\nR.C.C. M-20 grade using 20mm downgrade size c.b.g. chips including cost,
conveyance and royalty etc. complete,''')
    table7['amount'] = table7['amount'].map('\u20B9{:,.2f}'.format)
    table7['rate']=table7['rate'].map('\u20B9{:,.2f}'.format)
    print( table7)
    print ( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount7)
#===============================================================================
#     print( '''\nR.C.C. M-25 grade using 20mm down grade size c.b.g. chips including cost,
# conveyance and royalty etc. complete,''')
#     table8['amount'] = table8['amount'].map('\u20B9{:,.2f}'.format)
#     table8['rate']=table8['rate'].map('\u20B9{:,.2f}'.format)
#     print( table8)
#     print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount8)
#===============================================================================
    #=============
    print( '''\nSupplying, fiting and placing uncoated HYSD bar reinforcement complete
as per drawing and technical specification.,''')
    table9['amount'] = table9['amount'].map('\u20B9{:,.2f}'.format)
    table9['rate']=table9['rate'].map('\u20B9{:,.2f}'.format)
    print( table9)
    print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount9)
    #=============
    print( '''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling then after casting including cost of materials
complete in ground floor''')
    print( '-'*75)
    print( '''R.C.C. floor and roof slabs, landins, balconies, projecting sunshades
and chajjas upto 4.3m height''')
    table10['amount'] = table10['amount'].map('\u20B9{:,.2f}'.format)
    table10['rate']=table10['rate'].map('\u20B9{:,.2f}'.format)
    print( table10)
    print( 'Total cost for 10 times use for 9.0sqm area =\t',(u"\u20B9"),Tamount10)
    print( 'Total cost for 1 time use for 9.0sqm area =',(u"\u20B9"),Tamount10/10)
    Tamount101 = round(table101.amount.sum(),2)
    Tamount104=Tamount10/10+Tamount101
    
    table101['amount'] = table101['amount'].map('\u20B9{:,.2f}'.format)
    table101['rate']=table101['rate'].map('\u20B9{:,.2f}'.format)
    
    print( table101)
    print( 'Labour charges for 9.0sqm area = \t',(u"\u20B9"),Tamount101)
    print( 'Total rate for 9.0sqm area = \t\t',(u"\u20B9"),Tamount104)
    print( 'Total rate for 1.0sqm area = \t\t',(u"\u20B9"),round(Tamount104/9,2))
    #==============
    #===========================================================================
    # print( '''\nR.C.C. stairs excluding landing but including railing details for 5.0 sqm''')
    # table11['amount'] = table11['amount'].map('\u20B9{:,.2f}'.format)
    # table11['rate']=table11['rate'].map('\u20B9{:,.2f}'.format)
    # print( table11)
    # print( 'Total cost for 10 times use for 5.0sqm area =\t',(u"\u20B9"),Tamount11)
    # print( 'Total cost for 1 time use for 5.0sqm area =',(u"\u20B9"),Tamount11/10)
    # Tamount111=round(table111.amount.sum(),2)
    # Tamount114=Tamount11/10+Tamount101
    # 
    # table111['amount'] = table111['amount'].map('\u20B9{:,.2f}'.format)
    # table111['rate']=table111['rate'].map('\u20B9{:,.2f}'.format)
    # 
    # print( table111)
    # print( 'Labour charges for 5.0sqm area = \t',(u"\u20B9"),Tamount111)
    # print( 'Total rate for 5.0sqm area = \t\t',(u"\u20B9"),round(Tamount114,2))
    # print( 'Total rate for 1.0sqm area = \t\t',(u"\u20B9"),round(Tamount114/5,2))
    #===========================================================================
#    #===============
    print( '''\nR.C.C. foundation, plinth band and footings bases of columns mass
concrete precast slabs etc. for 10.0 sqm''')
    table12['amount'] = table12['amount'].map('\u20B9{:,.2f}'.format)
    table12['rate']=table12['rate'].map('\u20B9{:,.2f}'.format)
    print( table12)
    print( 'Total cost for 10 times use for 10.0sqm area =\t',(u"\u20B9"),Tamount12)
    print( 'Total cost for 1 time use for 10.0sqm area =',(u"\u20B9"),Tamount12/10)
    Tamount121=round(table121.amount.sum(),2)
    Tamount124=Tamount12/10+Tamount121
    
    table121['amount'] = table121['amount'].map('\u20B9{:,.2f}'.format)
    table121['rate']=table121['rate'].map('\u20B9{:,.2f}'.format)
    
    print( table121)
    print( 'Labour charges for 10.0sqm area = \t',(u"\u20B9"),Tamount121)
    print( 'Total rate for 10.0sqm area = \t\t',(u"\u20B9"),round(Tamount124,2))
    print( 'Total rate for 1.0sqm area = \t\t',(u"\u20B9"),round(Tamount124/10,2))
    #===============
    print( '''\nR.C.C. beams, colums, grider and bressmer etc. Data for 4.20 sqm''')
    table13['amount'] = table13['amount'].map('\u20B9{:,.2f}'.format)
    table13['rate']=table13['rate'].map('\u20B9{:,.2f}'.format)
    print( table13)
    print( 'Total cost for 10 times use for 4.2sqm area =\t',(u"\u20B9"),Tamount13)
    print( 'Total cost for 1 time use for 4.2sqm area =',(u"\u20B9"),round(Tamount13/10,2))
    Tamount131=round(table131.amount.sum(),2)
    Tamount134=Tamount13/10+Tamount131
    
    table131['amount'] = table131['amount'].map('\u20B9{:,.2f}'.format)
    table131['rate']=table131['rate'].map('\u20B9{:,.2f}'.format)
    
    print( table131)
    print( 'Labour charges for 4.2sqm area = \t',(u"\u20B9"),Tamount131)
    print( 'Total rate for 4.2sqm area = \t\t',(u"\u20B9"),round(Tamount134,2))
    print( 'Total rate for 1.0sqm area = \t\t',(u"\u20B9"),round(Tamount134/4.2,2))
#    #===============
    print( '''\nR.C.C. Lintels. Data for 7.8 sqm''')
    table14['amount'] = table14['amount'].map('\u20B9{:,.2f}'.format)
    table14['rate']=table14['rate'].map('\u20B9{:,.2f}'.format)
    print( table14)
    print( 'Total cost for 10 times use for 7.8sqm area =\t',(u"\u20B9"),Tamount14)
    print( 'Total cost for 1 time use for 7.8sqm area =',(u"\u20B9"),round(Tamount14/10,2))


    
    table141['amount'] = table141['amount'].map('\u20B9{:,.2f}'.format)
    table141['rate']=table141['rate'].map('\u20B9{:,.2f}'.format)
    
    print( table141)
    print( 'Labour charges for 7.8sqm area = \t',(u"\u20B9"),Tamount141)
    print( 'Total rate for 7.8sqm area = \t\t',(u"\u20B9"),round(Tamount144,2))
    print( 'Total rate for 1.0sqm area = \t\t',(u"\u20B9"),round(Tamount144/7.8,2))
    #===============
    #===========================================================================
    # print( '''\nR.C.C. walls and ins including attached pillasters Data for 23.90 sqm''')
    # table15['amount'] = table15['amount'].map('\u20B9{:,.2f}'.format)
    # table15['rate']=table15['rate'].map('\u20B9{:,.2f}'.format)
    # print( table15)
    # print( 'Total cost for 10 times use for 23.90 sqmsqm area =\t',(u"\u20B9"),Tamount15)
    # print( 'Total cost for 1 time use for 23.90 sqm area =',(u"\u20B9"),round(Tamount15/10,2))
    # Tamount151=round(table151.amount.sum(),2)
    # Tamount154=Tamount15/10+Tamount151
    # 
    # table151['amount'] = table151['amount'].map('\u20B9{:,.2f}'.format)
    # table151['rate']=table151['rate'].map('\u20B9{:,.2f}'.format)
    # 
    # print( table151)
    # print( 'Labour charges for 23.90 sqm area = \t',(u"\u20B9"),Tamount151)
    # print( 'Total rate for 2.90 sqm area = \t\t',(u"\u20B9"),round(Tamount154,2))
    # print( 'Total rate for 1.0sqm area = \t\t',(u"\u20B9"),round(Tamount154/23.9,2))
    #===========================================================================
    #===============
#===============================================================================
#     print( '''\nRandom rubble hard granite stone masonry in c.m. (1:6) including cost,
# conveyance and royalty of all materials''')
#     table16['amount'] = table16['amount'].map('\u20B9{:,.2f}'.format)
#     table16['rate']=table16['rate'].map('\u20B9{:,.2f}'.format)
#     print( table16)
#     print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount16)
#     #===============
#     print( '''\nCoursed rubble hard granite stone masonry in c.m. (1:6) including cost,
# conveyance and royalty of all materials''')
#     table17['amount'] = table17['amount'].map('\u20B9{:,.2f}'.format)
#     table17['rate']=table17['rate'].map('\u20B9{:,.2f}'.format)
#     print( table17)
#     print( 'Total cost =\t\t\t\t',(u"\u20B9"),Tamount17)
#     #===============
#     print( '''\nBrick masonry in c.m. (1:6) using C.B. bricks in F & P including cost,
# conveyance and royalty of all materials''')
#     table18['amount'] = table18['amount'].map('\u20B9{:,.2f}'.format)
#     table18['rate']=table18['rate'].map('\u20B9{:,.2f}'.format)
#     print( table18)
#     print( 'Total cost for 1.0cum of brick work in foundation and plinth =',(u"\u20B9"),Tamount18)
#     print( 'Total Cost for 1.0cum of brick work in super structure =',(u"\u20B9"),Tamount18+33)
#===============================================================================
    #===============
    print( '''\nBrick masonry in c.m. (1:6) using fly ash bricks in F & P including cost,
conveyance and royalty of all materials''')
    table28['amount'] = table28['amount'].map('\u20B9{:,.2f}'.format)
    table28['rate']=table28['rate'].map('\u20B9{:,.2f}'.format)
    print( table28)
    print( 'Total cost for 1.0cum of brick work in foundation and plinth =',(u"\u20B9"),Tamount28)
    print( 'Total Cost for 1.0cum of brick work in super structure =',(u"\u20B9"),Tamount28+33)
    
    #===============
    print( '''\nCement mortar plaster (1:6) on brick walls 12mm thick including cost,
conveyance and royalty of all materials''')
    table19['amount'] = table19['amount'].map('\u20B9{:,.2f}'.format)
    table19['rate']=table19['rate'].map('\u20B9{:,.2f}'.format)
    print( table19)
    print( 'Total cost for 1.0sqm of 12mm thick plaster with c.m. (1:6) =',(u"\u20B9"),Tamount19)
    #===============
    print( '''\nCement mortar plaster (1:6) 16mm thick on brick walls 16mm thick including cost,
conveyance and royalty of all materials''')
    table20['amount'] = table20['amount'].map('\u20B9{:,.2f}'.format)
    table20['rate']=table20['rate'].map('\u20B9{:,.2f}'.format)
    print( table20)
    print( 'Total cost for 1.0sqm of 16mm thick plaster with c.m. (1:6) =',(u"\u20B9"),Tamount20)
    #===============
    print( '''\nCement mortar plaster (1:6) 20mm thick on brick walls 16mm thick including cost,
conveyance and royalty of all materials''')
    table21['amount'] = table21['amount'].map('\u20B9{:,.2f}'.format)
    table21['rate']=table21['rate'].map('\u20B9{:,.2f}'.format)
    print( table21)
    print( 'Total cost for 1.0sqm of 20mm thick plaster with c.m. (1:6) =',(u"\u20B9"),Tamount21)
    #===============
    print( '''\nCement mortar plaster (1:4) on brick walls 6mm thick including deep
chipping and slurry treatment cost,conveyance and royalty of all materials''')
    table22['amount'] = table22['amount'].map('\u20B9{:,.2f}'.format)
    table22['rate']=table22['rate'].map('\u20B9{:,.2f}'.format)
    print( table22)
    print( 'Total cost for 1.0sqm of 6mm thick plaster with c.m. (1:4) =',(u"\u20B9"),Tamount22)
    #===============
    print( '''\nCement mortar plaster (1:4) on brick walls 12mm thick including
cost,conveyance and royalty of all materials''')
    table23['amount'] = table23['amount'].map('\u20B9{:,.2f}'.format)
    table23['rate']=table23['rate'].map('\u20B9{:,.2f}'.format)
    print( table23)
    print( 'Total cost for 1.0sqm of 12mm thick plaster with c.m. (1:4) =',(u"\u20B9"),Tamount23)
    #===============
    print( '''\nCement mortar plaster (1:4)20mm thick on roof slab top including
cost,conveyance and royalty of all materials''')
    table24['amount'] = table24['amount'].map('\u20B9{:,.2f}'.format)
    table24['rate']=table24['rate'].map('\u20B9{:,.2f}'.format)
    print( table24)
    print( 'Total cost for 1.0sqm of 20mm thick plaster with c.m. (1:4) =',(u"\u20B9"),Tamount24)
    
    #===============
    print( '''\n2.5cm thick A.S. flooring sing c.c. (1:2:4) with 12mm c.b.g. chips including
cost,conveyance and royalty of all materials''')
    table25['amount'] = table25['amount'].map('\u20B9{:,.2f}'.format)
    table25['rate']=table25['rate'].map('\u20B9{:,.2f}'.format)
    print( table25)
    print( 'Total cost for 1.0sqm of 2.5 thick A.S. flooring with c.c (1:2:4) =',(u"\u20B9"),Tamount25)
    #===============
    print( '''\nPainting 2 coats over a coat of priming including cost,conveyance
and royalty of all materials''')
    table26['amount'] = table26['amount'].map('\u20B9{:,.2f}'.format)
    table26['rate']=table26['rate'].map('\u20B9{:,.2f}'.format)
    print( table26)
    print( 'Total cost for 1.0sqm painting and priming =',(u"\u20B9"),round(Tamount26,2))
    #===============
    print( '''\nFinishing newly plastered wall surface with water proofing cement paint
including cost,conveyance and royalty of all materials''')
    table27['amount'] = table27['amount'].map('\u20B9{:,.2f}'.format)
    table27['rate']=table27['rate'].map('\u20B9{:,.2f}'.format)
    print( table27)
    print( 'Total cost for 1.0sqm painting and priming =',(u"\u20B9"),round(Tamount27,2))  
    
    
    
    print('\n\nJunior Engineer\t\t Assistant Engineer\t\tBlock Development Officer')
    print('Binka Block Ofiice\tBinka Block Office\t\t\tBinka')
