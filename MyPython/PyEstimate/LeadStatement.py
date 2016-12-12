'''
Created on Sep 23, 2016

@author: spalo
'''
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
data = [['cement','Binka',15,0,622],
        ['hysd bar','Binka',15,0,3900],
        ['c.b. bricks 25cmx12cmx8cm','Local',15,0,3.381],
        ['fly ash bricks 25cmx12cmx8cm','Binka',15,0,4.2],
        ['wood','Local',5,0,0],
        ['sand for masonry works','Mahanadi',5,27.5,55],
        ['sand for filiing','Local Nallah',5,27.5,48],
        ['40mm h.g. metal','SingiJuba',20,98.9,634],
        ['40mm c.b.g. metal','singijuba',30,98.9,780],
        ['20mm c.b.g. chips','SingiJuba',30,98.9,1030],
        ['12mm c.b.g. chips','SingiJuba',30,98.9,1050],
        ['10mm c.b.g. chips','SingiJuba',30,98.9,1050],
        ['laterite moorum','Local',5,27.5,50]]
table = pd.DataFrame(data,index = range(1,len(data)+1,1),columns= ['Description','Quarry','Lead','Royalty','Basic Cost'] )   
table['Lead'] = table['Lead'].astype(int)
#===============================================================================
# table['Remarks'] = table['Remarks'].astype(int)
#===============================================================================
table1 = table[:2]
table1.is_copy = False
table2 = table[2:4]
table2.is_copy = False
table3 = table[4:5]
table3.is_copy = False
table4 = table[5:len(table)]
table4.is_copy = False
table1['Conveyance']= [x *0 + 16.9 if x <= 5 else 16.9+(x-5)*.86 if x >= 50 else 156.4+45*9.3+(x-50)*0.73  for x in table1['Lead'] ]    
table2['Conveyance']= [x *0 + 1010.8/2000 if x <= 5 else 1010.8/2000+(x-5)*41.4/2000 if 5 < x <= 50 else 1010.8/2000+(x-50)*33.3/2000+45*41.4/2000  for x in table2['Lead'] ]    
table3['Conveyance']= [x *0 + 156.4/1.25  for x in table3['Lead'] ]
table4['Conveyance']= [x *0 + 156.4 if x <= 5 else 156.4+(x-5)*9.3 if x >= 50 else 156.4+45*9.3+(x-50)*6.5  for x in table4['Lead'] ]   
table5 = table1.append(table2).append(table3).append(table4)
table5['Total Cost']=table5['Royalty']+table5['Conveyance']+table5['Basic Cost']
table5['Lead']=table5['Lead'].map('{:.2f}km'.format)
table5['Royalty']=table5['Royalty'].map('Rs.{:.2f}'.format)
table5['Basic Cost']=table5['Basic Cost'].map('Rs.{:.2f}'.format)


table5['Conveyance']=table5['Conveyance'].map('Rs.{:.2f}'.format)
table5['Total Cost']=table5['Total Cost'].map('Rs.{:.2f}'.format)

            
        
        
        
if __name__ == "__main__":
    print('\t\t\t\t\t\tLEAD STATEMENT\n')
    print(table5)
    print('''\n\n\t\tThe lead of the materials as stated above is least and economical\n\n\n''')
    print('\t\t\tJunior Engineer','\tAssistant Engineer','\tBlock Development Officer')
    print('\t\t\tBinka Block Office','Binka Block Office','\t\t\tBinka')
    
    
