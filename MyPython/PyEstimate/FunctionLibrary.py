import colorama
colorama.init()
start = "\033[1;31m"
end = "\033[0;0m"
print (" " + start + "" + end)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#import LeadStatement as ls
import LeadStatement1 as ls1
import math as mt
import pandas as pd
def area_triangle(x):
    s=(x[0]+x[1]+x[2])/2
    return round(mt.sqrt(s*(s-x[0])*(s-x[1])*(s-x[2])),2)
def triangle(t,d,i,c=['side1','side2','side3']):
    table1=pd.DataFrame(d,index = i,columns = c)
    table1['area']=table1[['side1','side2','side3']].apply(area_triangle,axis=1)
    table1.tarea=table1['area'].sum()

    table1['side1']=table1['side1'].map('{:.2f}m'.format)
    table1['side2']=table1['side2'].map('{:.2f}m'.format)
    table1['side3']=table1['side3'].map('{:.2f}m'.format)
    table1['area']=table1['area'].map('{:.2f}sqm'.format)
    print (t,table1,'\n\t\tTotal area of the quadrilateral =','{:.2f}sqm'.format(table1.tarea))
def volume(t,r,d,i,c=['no','length','width','depth']):
    table1=pd.DataFrame(d,index = i, columns = c)
    table1['quantity']=table1['no']*table1['length']*table1['width']*table1['depth'].round(2)
    table1.tquantity = table1['quantity'].sum()

    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)
    table1['depth']=table1['depth'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}cum'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def volume_1(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns = ['no','no_1','length','width','depth'])
    table1['quantity']=table1['no']*table1['no_1']*table1['length']*table1['width']*table1['depth'].round(2)

    table1.tquantity = table1['quantity'].sum()

    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['no_1']=table1['no_1'].map('{:.2f}no'.format)

    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)
    table1['depth']=table1['depth'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}cum'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def volume_trapezoidal1(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns =['no','no_1','length','width at bottom','width at top','height'])
    table1['quantity']=table1['no']*table1['no_1']*table1['length']*(table1['width at bottom']+table1['width at top'])/2*table1['height'].round(2)
    table1.tquantity = table1['quantity'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['no_1']=table1['no_1'].map('{:.0f}no'.format)

    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width at bottom']=table1['width at bottom'].map('{:.2f}m'.format)
    table1['width at top']=table1['width at top'].map('{:.2f}m'.format)

    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}cum'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def volume_cylinder(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns =['no','coef','pi','dia','height'])
    table1['dia^2']=table1['dia']*table1['dia']

    table1['quantity']=table1['no']*table1['coef']*table1['pi']*table1['dia^2']*table1['height']
    table1.tquantity = table1['quantity'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['coef']=table1['coef'].map('{:.2f}'.format)

    table1['dia']=table1['dia'].map('{:.2f}m'.format)
    table1['dia^2']=table1['dia^2'].map('{:.2f}sqm'.format)


    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}cum'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)

def volume_trapezoidal(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns =['no','top_length','bottom_length','height'])
    table1['area_1']=table1['top_length']*table1['top_length']
    table1['area_2']=table1['bottom_length']*table1['bottom_length']
    table1['quantity']=table1['no']*(table1['area_1']+table1['area_2']+mt.sqrt(table1['area_1']*table1['area_2']))*table1['height']/3
    table1.tquantity = table1['quantity'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['top_length']=table1['top_length'].map('{:.2f}m'.format)
    table1['bottom_length']=table1['bottom_length'].map('{:.2f}m'.format)
    table1['area_1']=table1['area_1'].map('{:.2f}sqm'.format)
    table1['area_2']=table1['area_2'].map('{:.2f}sqm'.format)
    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}cum'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)

def volume_ring(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns =['no','pi','dia at centre line','width','height',])
    # table1['length at centre']=table1['pi']*table1['dia at centre line']

    table1['quantity']=table1['no']*table1['pi']*table1['dia at centre line']*table1['width']*table1['height']
    table1.tquantity = table1['quantity'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['pi']=table1['pi'].map('{:.2f}'.format)

    table1['dia at centre line']=table1['dia at centre line'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)


    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}cum'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)





def hArea(t,r,d,i):
    """no,length,width
    :rtype: floatbrea
    """
    table1=pd.DataFrame(d,index = i, columns = ['no','length','width'])
    table1['quantity']=table1['no']*table1['length']*table1['width'].round(2)
    table1.tquantity = (table1['quantity'].sum())

    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)

    table1['quantity']=table1['quantity'].map('{:.2f}sqm'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}sqm'.format(table1.tquantity),' @','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def hArea_1(t,r,d,i,c=['no','no_1','length','width']):
    table1=pd.DataFrame(d,index = i, columns = c)
    table1['quantity']=table1['no']*table1['no_1']*table1['length']*table1['width'].round(2)

    table1.tquantity = (table1['quantity'].sum())

    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['no_1']=table1['no_1'].map('{:.0f}no'.format)

    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)

    table1['quantity']=table1['quantity'].map('{:.2f}cum'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}sqm'.format(table1.tquantity),' @','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def vArea(t,r,d,i,c=['no','length','height']):
    table1=pd.DataFrame(d,index = i, columns = c)
    table1['quantity']=table1['no']*table1['length']*table1['height'].round(2)
    table1.tquantity = (table1['quantity'].sum())

    table1['no']=table1['no'].map('{:.2f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}sqm'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}sqm'.format(table1.tquantity),' @','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def vArea_1(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns = ['no','no_1','length','height'])
    table1['quantity']=table1['no']*table1['no_1']*table1['length']*table1['height'].round(2)

    table1.tquantity = table1['quantity'].sum()

    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['no_1']=table1['no_1'].map('{:.2f}no'.format)

    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}sqm'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}sqm'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
#Curved surface area of a cylinder
def area_curved_cylinder(t,r,d,i):
    table1=pd.DataFrame(d,index = i, columns = ['no','pi','dia','height'])
    table1['quantity']=table1['no']*table1['dia']*table1['height'].round(2)

    table1.tquantity = table1['quantity'].sum()

    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['pi']=table1['pi'].map('{:.2f}'.format)

    table1['dia']=table1['dia'].map('{:.2f}m'.format)
    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}sqm'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}sqm'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)


def area(t,r,d,i,c=['area']):
    table1=pd.DataFrame(d,index = i,columns=c)
    table1.tquantity=table1.area.sum()
    table1['area']=table1['area'].map('{:.2f}sqm'.format)
    print (t,'\n',table1,'\n\t\t\t\t\t\t','{:.2f}sqm'.format(table1.tquantity),'@','Rs.{:.2f}'.format(r),'=',color.BOLD+'Rs.{:.2f}'.format(round(r*table1.tquantity))+color.END)
def foundation(x):
    if x == 1:
        table1=pd.DataFrame({'quantity':[0.43*1.2],'rate':[200]},index=['unskilled labour'],columns=['quantity','rate'])
    else:
        table1 = pd.DataFrame({'quantity': [0.43], 'rate': [200]}, index=['unskilled labour'],
                              columns=['quantity', 'rate'])

    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table1['quantity']=table1['quantity'].map('{:.2f}no'.format)
    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    return table1
def reinforcement_detailed(d,i,c=['description','no','no_1','length','coefficient']):
    def total_length(d):
        return round(d[1]*d[2]*d[3],2)
    def weight(d):
        return round(d[1]*d[2]*d[3]*d[4],2)

    table1=pd.DataFrame(d,index = i,columns =c)
    table1['total length']=table1.apply(total_length,axis=1)
    table1['weight']=table1.apply(weight,axis=1)
    table1['length']=table1['length'].map('{:.2f}m'.format)

    #table1['total length']=table1['total length'].map('{:.2f}m'.format)
    #table1['weight']=table1['weight'].map('{:.2f}kg'.format)
    table1['coefficient']=table1['coefficient'].map('{:.3f}'.format)
    return table1,'\n',table1.weight.sum(),'\n',table1['total length'].sum()




def concrete(l):
    if l==1:
        t='''Cement concretre (1:4:8) using 40mm size granite metal
including cost,conveyance and royalty etc. complete'''
        d1={'quantity':[3.9,0.18],'rate':[200,240]}
        d2={'quantity':[1.72],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[0.96,0.48],'rate':[ls1.z['total cost'][11],ls1.z['total cost'][2]]}
        i1=['unskilled labour','mason II']
        i2=['cement']
        i3=['40mm h.g. metal','fine sand']
    elif l==2:
        t='''Cement concretre (1:3:6) using 40mm size granite metal
including cost,conveyance and royalty etc. complete'''
        d1={'quantity':[3.9,0.18],'rate':[200,240]}
        d2={'quantity':[2.29],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[0.96,0.48],'rate':[ls1.z['total cost'][11],ls1.z['total cost'][2]]}
        i1=['unskilled labour','mason II']
        i2=['cement']
        i3=['40mm h.g. metal','fine sand']
    elif l==3:
        t='''Cement concretre (1:2:4) using 12mm size granite chips
including cost,conveyance and royalty etc. complete'''
        d1={'quantity':[4.6,0.68],'rate':[200,240]}
        d2={'quantity':[3.23],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[0.9,0.45],'rate':[ls1.z['total cost'][9],ls1.z['total cost'][2]]}
        i1=['unskilled labour','mason II']
        i2=['cement']
        i3=['12mm h.g. chips','fine sand']
    elif l==4:
        t='''Cement concretre (1:1.5:3) using 12mm size granite chips
including cost,conveyance and royalty etc. complete'''
        d1={'quantity':[4.6,0.68],'rate':[200,240]}
        d2={'quantity':[4.29],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[0.9,0.45],'rate':[ls1.z['total cost'][9],ls1.z['total cost'][2]]}
        i1=['unskilled labour','mason II']
        i2=['cement']
        i3=['12mm h.g. chips','fine sand']
    else:
        t=''
        d1={'quantity':[0],'rate':[200,240]}
        d2={'quantity':[0],'rate':[ls1.z['total cost'][5]]}
        d3={'quantity':[0],'rate':[ls1.z['total cost'][10],ls1.z['total cost'][0]]}
        i1=['unskilled labour','mason II']
        i2=['cement']
        i3=['40mm h.g. metal','fine sand']




    table1=pd.DataFrame(d1,index=i1,columns=['quantity','rate'])
    table2=pd.DataFrame(d2,index=i2,columns=['quantity','rate'])
    table3=pd.DataFrame(d3,index=i3,columns=['quantity','rate'])
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table3['amount']=table3['quantity']*table3['rate'].round(2)
    # table1['quantity']=table1['quantity'].map('{:.0f}no'.format)
    # table2['quantity']=table2['quantity'].map('{:.2f}qtl'.format)
    # table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}no'.format)
    table2['quantity']=table2['quantity'].map('{:.2f}qtl'.format)
    table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)

    table4=table1.append(table2).append(table3)
    table4.tamount = (table4['amount'].sum())


    # table1['quantity']=table1['quantity'].map('{:.0f}no'.format)
    # table2['quantity']=table2['quantity'].map('{:.2f}qtl'.format)
    # table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)



    table4['rate']=table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount']=table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table4,'\n\tCost for 1.00cum of concrete= ',color.BOLD+'Rs.{:.2f}'.format(table4.tamount)+color.END)
def rscs(x):
    if x==1:
        t='''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling them after casting including cost of
materials complete in ground floor i) R.C.C. floor and roof slabs,
landings,balconies, projecting sun shades and chajjas upt 4.3m height
Details for 9 sqm.'''
        d1={'quantity':[56,0,0,0],'rate':[104,60,104,49]}
        d2={'quantity':[.112,.34,1.142],'rate':[19650,19650,ls1.z['total cost'][6]]}
        d3={'quantity':[2.75,2.75],'rate':[220,240]}
        s=9.0
    elif x==2:
        t='''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling them after casting including cost of
materials complete in ground floor  R.C.C. beams and columns
 4.3m height Details for 4.2 sqm.'''
        d1={'quantity':[15.2,0,8,0],'rate':[104,60,104,49]}
        d2={'quantity':[.218,0,0.456],'rate':[19650,19650,ls1.z['total cost'][6]]}
        d3={'quantity':[2.75,2.75],'rate':[220,240]}
        s=4.2
    elif x==3:
        t='''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling them after casting including cost of
materials complete in ground floor  R.C.C. plinth bend and footings
Details for 10.0 sqm.'''
        d1={'quantity':[0,0,0,12.6],'rate':[104,60,104,49]}
        d2={'quantity':[0,.267,.3284],'rate':[19650,19650,ls1.z['total cost'][6]]}
        d3={'quantity':[0.5,0.5],'rate':[220,240]}
        s=10
    elif x==4:
        t='''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling them after casting including cost of
materials complete in ground floor  R.C.C. lintel Details for 7.8 sqm.'''
        d1={'quantity':[0,21,0,0],'rate':[104,60,104,49]}
        d2={'quantity':[0,.413,0.689],'rate':[19650,19650,ls1.z['total cost'][6]]}
        d3={'quantity':[1.25],'rate':[220,240]}
        s=7.8
    elif x==5:
        t='''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling them after casting including cost of
materials complete in ground floor  R.C.C. stairs excluding landing but
including railing details for 5 Sqm'''
        d1={'quantity':[0,6.5,0,0],'rate':[104,60,104,49]}
        d2={'quantity':[0.039,.228,0.35],'rate':[19650,19650,ls1.z['total cost'][6]]}
        d3={'quantity':[2.75],'rate':[220,240]}
        s=5
    elif x==6:
        t='''Rigid and smooth centering and shuttering for R.C.C. works including
false works and dismantling them after casting including cost of
materials complete in ground floor R.C.C. walls and fins including attached
pillasters Data for 23.90 sqm'''
        d1={'quantity':[0,100.8,0,0],'rate':[104,60,104,49]}
        d2={'quantity':[.269,.954,2.461],'rate':[19650,19650,ls1.z['total cost'][6]]}
        d3={'quantity':[13.5],'rate':[220,240]}
        s=23.9
    else:
        return 0





    table1=pd.DataFrame(d1,index=['120mm dia sal bullah','120mm dia nonsal bullan','80mm dia sal bullan','70mm dia nonsal bullah'],columns=['quantity','rate'])
    table1=table1[table1.quantity!= 0]
    table2=pd.DataFrame(d2,index=['nonsal wood scantling','38mm/25mm nonsal planks','conveyance'],columns=['quantity','rate'])
    table2=table2[table2.quantity!= 0]

    table3=pd.DataFrame(d3,index=['semiskilled labour','mason II'],columns=['quantity','rate'])

    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate']
    table3['amount']=table3['quantity']*table3['rate']

    tamount1 = table3['amount'].sum()
    table1['quantity']=table1['quantity'].map('{:.3f}m'.format)
    table2['quantity']=table2['quantity'].map('{:.3f}cum'.format)
    table3['quantity']=table3['quantity'].map('{:.2f}no'.format)
    table4=table1.append(table2)
    tamount2 = table4['amount'].sum()
    table3['rate']=table3['rate'].map('Rs.{:.2f}'.format)
    table4['rate']=table4['rate'].map('Rs.{:.2f}'.format)
    table3['amount']=table3['amount'].map('Rs.{:.2f}'.format)
    table4['amount']=table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table4,'\n','Cost for ten time use of materials =','\t\t','Rs.{:.2f}'.format(tamount2),\
        '\nCost for one time use of materials =','\t\t','Rs.{:.2f}'.format(tamount2/10),'\n',table3,'\nLabour charges =','Rs.{:.2f}'.format(tamount1),\
        '\nGross cost for',s,' sqm of area = ','Rs.{:.2f}'.format(tamount2/10+tamount1),'\n','For one time use for 1.0 sqm of area cost =',color.BOLD+'Rs.{:.2f}'.format((tamount2/10+tamount1)/s)+color.END)
def earthwork_mechanical(t,d1,d2,i1,i2,c=['quantity','rate']):
    """

    :rtype: object
    """
    table1=pd.DataFrame(d1,index=i1,columns=c)
    table2=pd.DataFrame(d2,index=i2,columns=c)
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table1['quantity']=table1['quantity'].map('{:.0f}hr.'.format)
    table2['quantity']=table2['quantity'].map('{:.0f}cum'.format)

    table3=table1.append(table2)
    tamount1 = table3['amount'].sum()
    table3['rate']=table3['rate'].map('Rs.{:.2f}'.format)
    table3['amount']=table3['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table3,'\n','Cost for 1cum of earthwork = ',color.BOLD+'Rs.{:.2f}'.format(tamount1)+color.END)
def plaster(t):

    if t==1:
        t1= '''12mm thick plaster with c.m.(1:6) including cost, conveyance
and royalty etc. complete.'''
        d1={'quantity':[0.12,0.14],'rate':[200,240]}
        d2={'quantity':[.0358],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[.015],'rate':[ls1.z['total cost'][2]]}

    elif t == 2:
        t1='''16mm thick plaster with c.m.(1:6) including cost, conveyance
and royalty etc. complete. '''
        d1={'quantity':[0.24,0.16],'rate':[200,240]}
        d2={'quantity':[.043],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[.018],'rate':[ls1.z['total cost'][2]]}
    elif t==3:
        t1='''6mm thick plaster with c.m.(1:4) including cost, conveyance
and royalty etc. complete. '''
        d1={'quantity':[0.15,0.14],'rate':[200,240]}
        d2={'quantity':[.0372],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[.0075],'rate':[ls1.z['total cost'][2]]}
    elif t==4:
        t1='''20mm thick plaster with c.m.(1:4) on roof top as grading plaster including
cost, conveyance and royalty etc. complete. '''
        d1={'quantity':[.24,.16],'rate':[200,240]}
        d2={'quantity':[.0744],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[.021],'rate':[ls1.z['total cost'][2]]}
    elif t == 5:
        t1 = '''12mm thick plaster with c.m.(1:4) including cement punning
    cost, conveyance and royalty etc. complete. '''
        d1 = {'quantity': [0.15, 0.14], 'rate': [200, 240]}
        d2 = {'quantity': [.0644], 'rate': [ls1.z['total cost'][4]]}
        d3 = {'quantity': [.0075], 'rate': [ls1.z['total cost'][2]]}
    elif t == 6:
        t1='''20mm thick plaster with c.m.(1:6) on roof top as grading plaster including
cost, conveyance and royalty etc. complete. '''
        d1={'quantity':[.24,.16],'rate':[200,240]}
        d2={'quantity':[.057],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[.021],'rate':[ls1.z['total cost'][2]]}



    else:
        t1=''
        d1={'quantity':[0.0,0.0],'rate':[200,240]}
        d2={'quantity':[.0],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[.0],'rate':[ls1.z['total cost'][2]]}

    table1=pd.DataFrame(d1,index=['unskilled labour','mason II'],columns=['quantity','rate'])
    table2=pd.DataFrame(d2,index=['cement'],columns=['quantity','rate'])
    table3=pd.DataFrame(d3,index=['sand'],columns=['quantity','rate'])
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table3['amount']=table3['quantity']*table3['rate'].round(2)
    table4=table1.append(table2).append(table3)



    table1['quantity']=table1['quantity'].map('{:.4f}no'.format)
    table2['quantity']=table2['quantity'].map('{:.4f}qtl'.format)
    table3['quantity']=table3['quantity'].map('{:.4f}cum'.format)
    table4=table1.append(table2).append(table3)
    table4.tamount = (table4['amount'].sum())



    table4['rate']=table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount']=table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t1,'\n',table4,'\n\tCost for 1.00sqm of plaster area = ',color.BOLD+'Rs.{:.2f}'.format(table4.tamount)+color.END)
#Tile flooring
def Tile(x,c=['quantity','rate']):
    if x == 1:
        t = '''Fixing tiles in floors treads or steps and landing
on 25mm thick bed of cement mortar 1:1
(1cement : 1sand) jointed with neat cement
slury mixed with pigment to match the shades
of the tiles including rubbing and polishing
complete excluding cost of precast tiles'''
        d1 = {'quantity':1.857+0.44,'rate':ls1.z['total cost'][4]}
        d2 = {'quantity':0.13,'rate':ls1.z['total cost'][2]}
        d3 = {'quantity':[2.16,2.16],'rate':[260,200]}
        i1 = ['cement']
        i2 = ['sand']
        i3 = ['Mason I','Mulia']
    elif x ==2:
        t = '''Fixing tiles in dados skirting and risers of steps
on 12mm thick cement plaster (1:3) jointed
with neat cement slurry mixed with pigments to
match the shade of the tiles including rubbing
and polishing complete excluding cost of
precast tiles.'''
        d1 = {'quantity': 0.715+0.66, 'rate': ls1.z['total cost'][4]}
        d2 = {'quantity': 0.15, 'rate': ls1.z['total cost'][2]}
        d3 = {'quantity': [3.25, 3.25], 'rate': [260, 200]}
        i1 = ['cement']
        i2 = ['sand']
        i3 = ['Mason I', 'Mulia']
    else :
        pass
    table1=pd.DataFrame(d1,index=i1,columns=c)
    table2=pd.DataFrame(d2,index=i2,columns=c)
    table3=pd.DataFrame(d3,index=i3,columns=c)
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table3['amount']=table3['quantity']*table3['rate'].round(2)



    table1['quantity']=table1['quantity'].map('{:.3f}qtl'.format)
    table2['quantity']=table2['quantity'].map('{:.2f}cum'.format)
    table3['quantity']=table3['quantity'].map('{:.2f}no'.format)

    table4 = table1.append(table2).append(table3)
    table4.tamount = (table4['amount'].sum())



    table4['rate']=table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount']=table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table4,'\n\tCost for 1.00sqm of precast ceramic glazed tile flooring= ',color.BOLD+'Rs.{:.2f}'.format(table4.tamount/10)+color.END)
#Water proofing cement paint
def waterproofpaint():
    table1 = pd.DataFrame({'quantity': [.22,.32], 'rate': [200, 260]}, index=['unskilled labour', 'mason I'],
                          columns=['quantity', 'rate'])

    table1['amount'] = table1['quantity'] * table1['rate'].round(2)

    table1.tamount = (table1['amount'].sum())

    table1['quantity'] = table1['quantity'].map('{:.4f}no'.format)

    table1['rate'] = table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount'] = table1['amount'].map('Rs.{:.2f}'.format)
    print ('\n', 'Painting 2 coats over a coat of priming (only labour charges)', '\n', table1, '\n\tCost for 1.00sqm of water proofing cement paint over new plaster works= ', color.BOLD + 'Rs.{:.2f}'.format(
        table1.tamount / 10) + color.END)



def paint(t,d1,i1,c=['quantity','rate']):
    table1=pd.DataFrame(d1,index=i1,columns=c)
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table1.tamount = (table1['amount'].sum())


    table1['quantity']=table1['quantity'].map('{:.4f}no'.format)



    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table1,'\n\tCost for 1.00sqm of precast ceramic glazed tile flooring= ',color.BOLD+'Rs.{:.2f}'.format(table1.tamount/10)+color.END)
def painting():
    table1=pd.DataFrame({'quantity':[1.6,1.75],'rate':[200,260]},index=['unskilled labour','mason I'],columns=['quantity','rate'])

    table1['amount']=table1['quantity']*table1['rate'].round(2)

    table1.tamount = (table1['amount'].sum())


    table1['quantity']=table1['quantity'].map('{:.4f}no'.format)



    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    print ('\n','Painting 2 coats over a coat of priming (only labour charges)','\n',table1,'\n\tCost for 1.00sqm of painting over priming on new works= ',color.BOLD+'Rs.{:.2f}'.format(table1.tamount/9.3)+color.END)
def costMaterial(t,d1,i1,c=['quantity','rate']):
    table1=pd.DataFrame(d1,index=i1,columns=c)
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table1.tamount = (table1['amount'].sum())
    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table1,'\n\tCost of different materials= ',color.BOLD+'Rs.{:.2f}'.format(table1.tamount)+color.END)
def gradedconcrete(x):
    if x==1:
        t='''R.C.C. work of M-15 grade with 20mm and down grade black hard granite
(crusherbroken) stone chips including hoisting and laying Data for 1 cum'''
        m=2.8
    elif x==2:
        t='''R.C.C. work of M-20 grade with 20mm and down grade black hard granite
(crusherbroken) stone chips including hoisting and laying Data for 1 cum'''
        m=5.21*10/15
    elif x==3:
        t='''R.C.C. work of M-25 grade with 20mm and down grade black hard granite
(crusherbroken) stone chips including hoisting and laying Data for 1 cum'''
        m=6.05*10/15
    elif x==4:
        t='''R.C.C. work of M-30 grade with 20mm and down grade black hard granite
(crusherbroken) stone chips including hoisting and laying Data for 1 cum'''
        m=6.1*10/15

    else:
        t=''''''
        m=0


    table1=pd.DataFrame({'quantity':[20.0/15,0.86/15,1.5/15],'rate':[200.0,220.0,240.0]},index = ['unskilled labour','semiskilled labour','mason II'],columns=['quantity','rate'])
    table2=pd.DataFrame({'quantity':[m],'rate':[ls1.z['total cost'][4]]},index = ['cement'],columns=['quantity','rate'])
    table3=pd.DataFrame({'quantity':[0.54,0.36,0.45],'rate':[ls1.z['total cost'][10],ls1.z['total cost'][8],ls1.z['total cost'][2]]},index = ['20mm chips','10mm chips','sand'],columns=['quantity','rate'])
    table4=pd.DataFrame({'quantity':[0.4],'rate':[177,240]},index = ['concrete mixer','generator'],columns=['quantity','rate'])
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table3['amount']=table3['quantity']*table3['rate'].round(2)
    table4['amount']=table4['quantity']*table4['rate'].round(2)
    table1['quantity']=table1['quantity'].map('{:.2f}no'.format)
    table2['quantity']=table2['quantity'].map('{:.4f}qtl'.format)
    table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)
    table4['quantity']=table4['quantity'].map('{:.1f}hr'.format)

    table=table1.append(table2).append(table3).append(table4)
    tamount = table.amount.sum()
    table['rate']=table['rate'].map('Rs.{:.2f}'.format)
    table['amount']=table['amount'].map('Rs.{:.2f}'.format)
    print (t,'\n',table,'\nRate of 1 cum of M-20 graded concrete=',color.BOLD+'Rs.{:.2f}'.format(tamount)+color.END)
#Reinforcement works
def reinforcement():
    t='''Supplying ,fitting and placing uncoated HYSD bar reinforcement complete
as per drawing and technical specification.Unit - 1 qtl Taking Output = 1 qtl'''
    table1=pd.DataFrame({'quantity':[1.05],'rate':[4000+ls1.z['conveyance'][5]]},index = ['uncoated HYSD bars'],columns=['quantity','rate'])
    table2=pd.DataFrame({'quantity':[0.8],'rate':[75.0]},index = ['binding wire'],columns=['quantity','rate'])
    table3=pd.DataFrame({'quantity':[.8,.044,.3],'rate':[200,220,260]},index = ['unskilled labour','semiskilled labour','mason I'],columns=['quantity','rate'])

    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table3['amount']=table3['quantity']*table3['rate'].round(2)

    table1['quantity']=table1['quantity'].map('{:.2f}qtl'.format)
    table2['quantity']=table2['quantity'].map('{:.2f}kg'.format)
    table3['quantity']=table3['quantity'].map('{:.3f}no'.format)
    table=table1.append(table2).append(table3)
    tamount = table.amount.sum()
    table['rate']=table['rate'].map('Rs.{:.2f}'.format)
    table['amount']=table['amount'].map('Rs.{:.2f}'.format)
    print (t,'\n',table,'\nRate of 1 quintal of Reinforcement works=',color.BOLD+'Rs.{:.2f}'.format(tamount)+color.END)
#Dismantling
def dismantling(t):
    if t==1:
        t1='''Dismantling and removing cement concrete including stacking the
useful materials for reuse and removing the debris within 50m lead per 1 cum'''
        x=1
        d= {'quantity':[1.6],'rate':[200]}
    elif t==2:
        t1='''Dismantling and removing R.C.C. columns beams slab staircase
landing lintels including stacking the useful materials for reuse and
removing the debris within 50m lead per 1 cum'''
        x=1
        d= {'quantity':[1.5,1.5],'rate':[200,220]}
    elif t==3:
        t1='''Dismantling brick or stone masonry in lime or cement mortar above 3m.
height including stacking the useful materials for reuse and removing
the debris within 50m. Lead  per 1 cum Data for 2.83 cum'''
        x=2.83
        d= {'quantity':[9,0],'rate':[200,220]}
    else:
        t1=''
        x=1
        d= {'quantity':[0.0],'rate':[200]}

    table1=pd.DataFrame(d,index = ['unskilled labour','semiskilled mulia'],columns=['quantity','rate'])
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    tamount = table1['amount'].sum()
    table1['quantity']=table1['quantity'].map('{:.2f}no'.format)
    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    print (t1,'\n',table1,'\nRate of 1 cum  of dismantling works =',color.BOLD+'Rs.{:.2f}'.format(tamount/x)+color.END)
#Brick masonry
def brickmasonry(l):
    if l==1:
        t='''Brick masonry in foundation and plinth in c.m.(1:6) using c.b. bricks
including cost,conveyance and royalty etc. complete'''
        d1={'quantity':[2.96,1.41,0.35],'rate':[200,240,260]}
        d2={'quantity':[0.672],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[0.28],'rate':[ls1.z['total cost'][2]]}

        d4={'quantity':[350],'rate':[ls1.z['total cost'][1]]}
        i1=['unskilled labour','mason II','mason I']
        i2=['cement']
        i3=['fine sand']
        i4=['c.b. bricks']
    elif l==2:
        t = '''Brick masonry in foundation and plinth in c.m.(1:6) using fly ash bricks
including cost,conveyance and royalty etc. complete'''
        d1={'quantity':[2.96,1.41,0.35],'rate':[200,240,260]}
        d2={'quantity':[0.672],'rate':[ls1.z['total cost'][4]]}
        d3={'quantity':[0.28],'rate':[ls1.z['total cost'][2]]}

        d4={'quantity':[350],'rate':[ls1.z['total cost'][14]]}
        i1=['unskilled labour','mason II','mason I']
        i2=['cement']
        i3=['fine sand']
        i4=['c.b. bricks']
    elif l == 3:
        t = '''Brick masonry in foundation and plinth in c.m.(1:4) using fly ash bricks
    including cost,conveyance and royalty etc. complete'''
        d1 = {'quantity': [2.96, 1.41, 0.35], 'rate': [200, 240, 260]}
        d2 = {'quantity': [1.0], 'rate': [ls1.z['total cost'][4]]}
        d3 = {'quantity': [0.28], 'rate': [ls1.z['total cost'][2]]}

        d4 = {'quantity': [350], 'rate': [ls1.z['total cost'][13]]}
        i1 = ['unskilled labour', 'mason II', 'mason I']
        i2 = ['cement']
        i3 = ['fine sand']
        i4 = ['c.b. bricks']

    else:
        d1={'quantity':[0,0,0],'rate':[200,240,260]}
        d2={'quantity':[0],'rate':[ls1.z['total cost'][5]]}
        d3={'quantity':[0],'rate':[ls1.z['total cost'][8],ls1.z['total cost'][0]]}

        d4={'quantity':[0],'rate':[ls1.z['total cost'][13]]}
        i1=['unskilled labour','mason II','mason I']
        i2=['cement']
        i3=['fine sand']
        i4=['fly ash bricks']




    table1=pd.DataFrame(d1,index=i1,columns=['quantity','rate'])
    table2=pd.DataFrame(d2,index=i2,columns=['quantity','rate'])
    table3=pd.DataFrame(d3,index=i3,columns=['quantity','rate'])
    table4=pd.DataFrame(d4,index=i4,columns=['quantity','rate'])
    table1['amount']=table1['quantity']*table1['rate'].round(2)
    table2['amount']=table2['quantity']*table2['rate'].round(2)
    table3['amount']=table3['quantity']*table3['rate'].round(2)
    table4['amount']=table4['quantity']*table4['rate'].round(2)
    # table1['quantity']=table1['quantity'].map('{:.0f}no'.format)
    # table2['quantity']=table2['quantity'].map('{:.2f}qtl'.format)
    # table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)
    table1['quantity']=table1['quantity'].map('{:.2f}no'.format)
    table2['quantity']=table2['quantity'].map('{:.3f}qtl'.format)
    table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)
    table4['quantity']=table4['quantity'].map('{:.2f}no'.format)

    table5=table1.append(table2).append(table3).append(table4)
    table5.tamount = (table5)['amount'].sum()


    # table1['quantity']=table1['quantity'].map('{:.0f}no'.format)
    # table2['quantity']=table2['quantity'].map('{:.2f}qtl'.format)
    # table3['quantity']=table3['quantity'].map('{:.2f}cum'.format)



    table5['rate']=table5['rate'].map('Rs.{:.2f}'.format)
    table5['amount']=table5['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t,'\n',table5,'\n\tCost for 1.00cum of brick masonry= ',color.BOLD+'Rs.{:.2f}'.format(table5.tamount)+color.END,'\n\tCost for 1.00cum of brick masonry in super sturcture= ',color.BOLD+'Rs.{:.2f}'.format(table5.tamount+33.0)+color.END)

def sandfilling():


    t1= '''Filling sand in the foundation and plinth well watered and rammed
including cost, conveyance and royalty etc. complete. '''
    d1={'quantity':[0.1236],'rate':[200]}

    d3={'quantity':[1],'rate':[ls1.z['total cost'][3]]}


    table1=pd.DataFrame(d1,index=['unskilled labour'],columns=['quantity','rate'])

    table3=pd.DataFrame(d3,index=['sand'],columns=['quantity','rate'])
    table1['amount']=table1['quantity']*table1['rate'].round(2)

    table3['amount']=table3['quantity']*table3['rate'].round(2)
    table4=table1.append(table3)



    table1['quantity']=table1['quantity'].map('{:.4f}no'.format)

    table3['quantity']=table3['quantity'].map('{:.4f}cum'.format)
    table4=table1.append(table3)
    table4.tamount = (table4['amount'].sum())



    table4['rate']=table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount']=table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n',t1,'\n',table4,'\n\tCost for 1.00cum of sand filling = ',color.BOLD+'Rs.{:.2f}'.format(table4.tamount)+color.END)
#Signature
def signature(cost,text,x,gp):
    # type: (object, object, object) -> object
    if x == 1:
        print ('The estimate is technically sanctioned for',' Rs.{:.2f}'.format(
            cost),'\n',text,'\n\n\n\t\t\t\t\tJunior Engineer','\n\t\t\t\t\tBinka Block Office',\
            '\n\t\t\tCountersigned by','\n\n\n\t\t\t\t\tAssistant Engineer','\n\t\t\t\t\tBinka Block Office',\
            '\nThe estimate is administratively approved for',' Rs.{:.2f}'.format(cost),'\n',text,\
            '\n\n\n\t\t\t\t\tBlock Development officer','\n\t\t\t\t\t\tBinka ')
    elif x == 2:
        print ('The estimate is technically sanctioned for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tAssistant Engineer', \
            '\n\t\t\t\t\tBinka Block Office', '\n\t\t\tPrepared by', '\n\n\n\t\t\t\t\tJunior Engineer',\
            '\n\t\t\t\t\tBinka Block Office', '\nThe estimate is administratively approved for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tBlock Development officer', '\n\t\t\t\t\t\t\tBinka ')
    elif x == 3:
        print ('The estimate is technically sanctioned for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tJunior Engineer', \
            '\n\t\t\t\t\tBinka Block Office', '\n\t\t\tCountersigned by', '\n\n\n\t\t\t\t\tAssistant Engineer',\
            '\n\t\t\t\t\tBinka Block Office', '\nThe estimate is administratively approved for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tSarpanch', '\n\t\t\t\t\t',gp)

    elif x == 4 :
        print ('The estimate is technically sanctioned for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tAssistant Engineer', \
            '\n\t\t\t\t\tBinka Block Office', '\n\t\t\tPrepared by', '\n\n\n\t\t\t\t\tJunior Engineer',\
            '\n\t\t\t\t\tBinka Block Office', '\nThe estimate is administratively approved for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tSarpanch', '\n\t\t\t ',gp)
    elif x ==5:
        print ('The estimate is technically sanctioned for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tExecutive Engineer', \
            '\n\t\t\t\t\tD.R.D.A. Subarna pur', '\n\t\t\tPrepared by', '\n\n\n\t\t\t\t\tJunior Engineer', \
            '\n\t\t\t\t\tBinka Block Office','\n\t\t\tChecked by', '\n\n\n\t\t\t\t\tAssistant Engineer', \
            '\n\t\t\t\t\tBinka Block Office'\
            '\nThe estimate is administratively approved for', ' Rs.{:.2f}'.format(
            cost), '\n', text, '\n\n\n\t\t\t\t\tBlock Development Officer', '\n\t\t\t\t\tBinka Block Office' ,gp)
    else:
        print('\n\n\n  Junior Engineer','\t   Assistant Engineer','\tBlock Development Officer','\n','Binka Block Office','       Binka Block Office','\t\tBinka')



def volume1(m,i,r,c=['Description','no','length','width','height']):
    def volume(m):
        return round(m[1]*m[2]*m[3]*m[4],2)
    table1=pd.DataFrame(m,index=i,columns=c)
    table1['volume']=table1.apply(volume,axis=1)
    tvolume= table1['volume'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)
    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['volume']=table1['volume'].map('{:.2f}cum'.format)

    print  (table1,'\n\t\t\t\t\t','{:.2f}cum'.format(tvolume),'@ Rs.{:.2f}'.format(r),' = Rs.{:.2f}'.format(mt.ceil(r*tvolume)))
def reinforcement_detailed1(m,i,c=['Description','no','length','coefficient']):
    # type: (object, object, object) -> object
    def total_length(m):
        return round(m[1]*m[2],2)
    def weight(m):
        return round(m[1]*m[2]*m[3],2)
    table1=pd.DataFrame(m,index=i,columns=c)
    table1['total length']=table1.apply(total_length,axis=1)
    table1['weight']=table1.apply(weight,axis=1)
    tweight= table1['weight'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['coefficient']=table1['coefficient'].map('{:.3f}'.format)
    table1['total length']=table1['total length'].map('{:.2f}m'.format)
    table1['weight']=table1['weight'].map('{:.2f}kg'.format)

    print (table1,'{:.2f}kg'.format(tweight))
def harea(m,i,r,c=['Description','no','length','width']):
    def area(m):
        return round(m[1]*m[2]*m[3],2)
    table1= pd.DataFrame(m,index = i,columns =c)

    table1['area']=table1.apply(area,axis=1)
    tarea= table1['area'].sum()
    table1['no']=table1['no'].map('{:.2f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['width']=table1['width'].map('{:.2f}m'.format)
    table1['area']=table1['area'].map('{:.2f}sqm'.format)

    print (table1,'\n\t\t\t\t\t','{:.2f}sqm'.format(tarea),'@ Rs.{:.2f}'.format(r),' = Rs.{:.2f}'.format(mt.ceil(r*tarea)))
def varea(m,i,r,c=['Description','no','length','height']):
    def area(m):
        return round(m[1]*m[2]*m[3],2)
    table1= pd.DataFrame(m,index = i,columns =c)

    table1['area']=table1.apply(area,axis=1)
    tarea= table1['area'].sum()
    table1['no']=table1['no'].map('{:.2f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['area']=table1['area'].map('{:.2f}sqm'.format)

    print (table1,'\n\t\t\t\t\t','{:.2f}sqm'.format(tarea),'@ Rs.{:.2f}'.format(r),' = Rs.{:.2f}'.format(mt.ceil(r*tarea)))
def volumeTrapezoidal(m,i,r,c=['Description','no','length','top width','bottom width','height']):
    def volume(m):
        return round(m[1]*m[2]*(m[3]+m[4])/2*m[5],2)
    table1=pd.DataFrame(m,index=i,columns=c)
    table1['volume']=table1.apply(volume,axis=1)
    tvolume= table1['volume'].sum()
    table1['no']=table1['no'].map('{:.0f}no'.format)
    table1['length']=table1['length'].map('{:.2f}m'.format)
    table1['top width']=table1['top width'].map('{:.2f}m'.format)
    table1['bottom width'] = table1['bottom width'].map('{:.2f}m'.format)

    table1['height']=table1['height'].map('{:.2f}m'.format)
    table1['volume']=table1['volume'].map('{:.2f}cum'.format)

    print (table1,'\n','{:.2f}cum'.format(tvolume),'@ Rs.{:.2f}'.format(r),' = Rs.{:.2f}'.format(r*tvolume))

def moorum(x):
    if x == 1:
        table1 = pd.DataFrame({'quantity': [2.5/2.83], 'rate': [200]}, index=['unskilled labour'],
                              columns=['quantity', 'rate'])
    else:
        table1 = pd.DataFrame({'quantity': [1/2.83], 'rate': [200]}, index=['unskilled labour'],
                              columns=['quantity', 'rate'])

    table1['amount'] = table1['quantity'] * table1['rate'].round(2)
    table1['quantity'] = table1['quantity'].map('{:.2f}no'.format)
    table1['rate'] = table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount'] = table1['amount'].map('Rs.{:.2f}'.format)
    return table1
def flooring():
    t='''Artificial stone flooring with c.c.(1:2:4) using 12mm size c.b.g. chips
including cost,conveyance and royalty etc. complete'''
    d1={'quantity':[.36,0.13],'rate':[200,260]}
    d2={'quantity':[.0858],'rate':[ls1.z['total cost'][4]]}
    d3={'quantity':[0.023,0.012],'rate':[ls1.z['total cost'][9],ls1.z['total cost'][2]]}
    i1=['unskilled labour','mason I']
    i2=['cement']
    i3=['12mm h.g. chips','fine sand']


    table1 = pd.DataFrame(d1, index=i1, columns=['quantity', 'rate'])
    table2 = pd.DataFrame(d2, index=i2, columns=['quantity', 'rate'])
    table3 = pd.DataFrame(d3, index=i3, columns=['quantity', 'rate'])
    table1['amount'] = table1['quantity'] * table1['rate'].round(2)
    table2['amount'] = table2['quantity'] * table2['rate'].round(2)
    table3['amount'] = table3['quantity'] * table3['rate'].round(2)
    table1['quantity'] = table1['quantity'].map('{:.2f}no'.format)
    table2['quantity'] = table2['quantity'].map('{:.2f}qtl'.format)
    table3['quantity'] = table3['quantity'].map('{:.2f}cum'.format)

    table4 = table1.append(table2).append(table3)
    table4.tamount = (table4['amount'].sum())
    table4['rate'] = table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount'] = table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n', t, '\n', table4, '\n\tCost for 1.00cum of concrete= ', color.BOLD + 'Rs.{:.2f}'.format(
    table4.tamount) + color.END)
def tcl(m,i,c = ['Description','no','length']):
    def total(m):
        return round(m[1]*m[2],2)
    table1=pd.DataFrame(m,index = i, columns = c)
    table1['total']=table1.apply(total,axis=1)
    tcl = round(table1['total'].sum(),2)
    return table1,tcl
def opening(m,i,c = ['Description','no','dimension1','dimension2']):
    def area (m):
        return round(m[1]*m[2]*m[3],2)

    table1 = pd.DataFrame(m, index=i, columns=c)
    table1['area'] = table1.apply(area, axis=1)
    total_area = round(table1['area'].sum(), 2)
    return table1, total_area
def vitrifiedtile(x):
    t = '''Supplying, fitting and fixing vitrified tile in
floors of size 600mm x 600mm of approved
make with application of polymer modified
cement based water resistant adhesive bed
of required thickness of 10mm and filling
joints with epoxy grout of approved quality
including cost of all materials, labour T&P
etc required for the work.'''
    d1 = {'quantity': [2.16,5.5,2.16], 'rate': [200,220, 260]}
    d2 = {'quantity': [90], 'rate': 20}
    d3 = {'quantity': [10], 'rate': 665}
    d5 = {'quantity':1,'rate':322.8}
    i1 = ['unskilled labour','semi skilled labour', 'mason I']
    i2 = ['polymer modified adhesive']
    i3 = ['tile']
    i5 = ['epoxy grout']

    table1 = pd.DataFrame(d1, index=i1, columns=['quantity', 'rate'])
    table2 = pd.DataFrame(d2, index=i2, columns=['quantity', 'rate'])
    table3 = pd.DataFrame(d3, index=i3, columns=['quantity', 'rate'])
    table5 = pd.DataFrame(d5,index = i5,columns = ['quantity','rate'])
    table1['amount'] = table1['quantity'] * table1['rate'].round(2)
    table2['amount'] = table2['quantity'] * table2['rate'].round(2)
    table3['amount'] = table3['quantity'] * table3['rate'].round(2)
    table5['amount'] = table5['quantity'] * table5['rate'].round(2)
    table1['quantity'] = table1['quantity'].map('{:.2f}no'.format)
    table2['quantity'] = table2['quantity'].map('{:.2f}kg'.format)
    table3['quantity'] = table3['quantity'].map('{:.2f}sqm'.format)
    table5['quantity'] = table5['quantity'].map('{:.0f}L.S.'.format)

    table4 = table1.append(table2).append(table3).append(table5)
    table4.tamount = (table4['amount'].sum())
    table4['rate'] = table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount'] = table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n', t, '\n', table4, '\n\tCost for 1.00sqm of vitrified tile flooring = ', color.BOLD + 'Rs.{:.2f}'.format(
        table4.tamount/10) + color.END)

def vitrifiedtile1(x):
    t = '''Supplying, fitting and fixing vitrified tile in
    floors of size 600mm x 600mm of approved
    make with application of cement mortar bed
    of required thickness and filling
    joints with white cement of approved quality
    including cost of all materials, labour T&P
    etc required for the work.'''
    d1 = {'quantity': [2.16, 2.16], 'rate': [200, 260]}
    d2 = {'quantity': [1.074], 'rate': ls1.z['total cost'][4]}
    d3 = {'quantity': [10], 'rate': 665}
    d5 = {'quantity': [0.21], 'rate': ls1.z['total cost'][2]}
    d6 = {'quantity':0.075,'rate':17.25}
    i1 = ['unskilled labour', 'mason I']
    i2 = ['cement']
    i3 = ['tile']
    i5 = ['sand']
    i6 = ['white cement']

    table1 = pd.DataFrame(d1, index=i1, columns=['quantity', 'rate'])
    table2 = pd.DataFrame(d2, index=i2, columns=['quantity', 'rate'])
    table3 = pd.DataFrame(d3, index=i3, columns=['quantity', 'rate'])
    table5 = pd.DataFrame(d5, index=i5, columns=['quantity', 'rate'])
    table6 = pd.DataFrame(d6, index=i6, columns=['quantity', 'rate'])

    table1['amount'] = table1['quantity'] * table1['rate'].round(2)
    table2['amount'] = table2['quantity'] * table2['rate'].round(2)
    table3['amount'] = table3['quantity'] * table3['rate'].round(2)
    table5['amount'] = table5['quantity'] * table5['rate'].round(2)
    table6['amount'] = table6['quantity'] * table6['rate'].round(2)

    table1['quantity'] = table1['quantity'].map('{:.2f}no'.format)
    table2['quantity'] = table2['quantity'].map('{:.2f}qtl'.format)
    table3['quantity'] = table3['quantity'].map('{:.2f}sqm'.format)
    table5['quantity'] = table5['quantity'].map('{:.2f}cum'.format)
    table6['quantity'] = table6['quantity'].map('{:.2f}kg'.format)

    table4 = table1.append(table2).append(table3).append(table5).append(table6)
    table4.tamount = (table4['amount'].sum())
    table4['rate'] = table4['rate'].map('Rs.{:.2f}'.format)
    table4['amount'] = table4['amount'].map('Rs.{:.2f}'.format)
    print ('\n', t, '\n', table4, '\n\tCost for 1.00sqm of vitrified tile flooring = ', color.BOLD + 'Rs.{:.2f}'.format(
            table4.tamount / 10) + color.END)
def distempering():
    table1=pd.DataFrame({'quantity':[0.62,0.52],'rate':[200,260]},index=['unskilled labour','mason I'],columns=['quantity','rate'])

    table1['amount']=table1['quantity']*table1['rate'].round(2)

    table1.tamount = (table1['amount'].sum())


    table1['quantity']=table1['quantity'].map('{:.4f}no'.format)



    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    print ('\n','''Distempering two coats to walls with distemper of approved shade on new
work to give an even shade exculding cost of distemper.(only labour charges)''','\n',table1,'\n\tCost for 1.00sqm of painting over priming on new works= ',color.BOLD+'Rs.{:.2f}'.format(table1.tamount/9.3)+color.END)
def wallpainting():
    table1=pd.DataFrame({'quantity':[0.64,0.54],'rate':[200,260]},index=['unskilled labour','mason I'],columns=['quantity','rate'])

    table1['amount']=table1['quantity']*table1['rate'].round(2)

    table1.tamount = (table1['amount'].sum())


    table1['quantity']=table1['quantity'].map('{:.4f}no'.format)



    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['amount']=table1['amount'].map('Rs.{:.2f}'.format)
    print ('\n','''Wall painting 2 coats with weather coat of approved shade
on new work to give an even shade exculding cost of paint''','\n',table1,'\n\tCost for 1.00sqm of painting over priming on new works= ',color.BOLD+'Rs.{:.2f}'.format(table1.tamount/9.3)+color.END)







































