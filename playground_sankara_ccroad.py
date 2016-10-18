import pandas as pd
import ClassLibrary as cl
import FunctionLibrary as fl
import items as it
t= '''Construction opf C.C. road from Sankara Medical Road to Harijan Sahi
Road near Play Field, Sankara'''
ec = 'Estimated Cost:-Rs.3,00,000.00'
l1=50.0 #length of cut-off wall
b1=3.65 #width of road
 






if __name__ == "__main__":
    print(t,'\n',ec,'    Head of Account:- Maintenance of Road and Bridge')
    print('-'*85)
    print(it.items['efhs'])
    foundation = cl.Quantity([['cut-off walls',2,l1,0.6,0.45],
                              ['cut-off walls at culvert',2,2.0,0.6,0.9],
                              ['bed of pipes',1,5.0,1.00,0.15]
                              ])
    foundation.rate=103.2
    foundation.volume()
    print(it.items['CC(1:3:6)'])
    metal_concrete=cl.Quantity([['cut-off walls',2,l1,0.25,0.6],
                                ['cut-off walls at culvert',2,2.0,0.45,1.3],
                                ['bed of pipes',1,5.0,1.0,0.15],
                                ['sub-base of concrete',1,l1,b1,0.1]])
    metal_concrete.rate=3647.57
    metal_concrete.volume()
    print(it.items['CC(1:2:4)'])
    metal_concrete=cl.Quantity([
                                ['crust of road',1,l1,b1,0.1]])
    metal_concrete.rate=4760.71
    metal_concrete.volume()
    print(it.items['rscs_walls'])
    centering=cl.Quantity([['external side of walls',2,l1,0.3+0.2],
                           ['internal side of walls',2,l1,0.3],
                           ['culvert walls',4,2.0,1.3]])
    centering.rate=387.08
    centering.vArea()
    print(it.items['sand_filling'])
    sand_filling = cl.Quantity([['inside cut-off walls',1,l1,3.65-.6,0.3]])
    sand_filling.rate=302.62
    sand_filling.volume()
    print(it.items['Earth_work_mechanical'])
    side_earth_work=cl.Quantity([['both side berm',2,l1,1.25,0.5]])
    side_earth_work.rate=118.9
    side_earth_work.volume()
    print('\nCost and conveyance of NP-3 R.C.C. hume pipes 2nos. @ Rs. 4710.00 = Rs. 9420.00 ')
    print('\n Conveyance and laying of R.C.C. hume pipes (provisional)  = Rs. 3000.00')
    print('\nCess for welfare of labourers = Rs. 3000.00')
    print('\nWork contingency = Rs. 3000.00')
    print('\nDisplay board and photograph = Rs. 2000.00')
    print('\nhire and running charges of plate vibrator = 7.3hr @ Rs.106..00/hr. = Rs.790.00')
    print('-'*85,'\n')
    fl.signature(300000,'Rupees three lakh only', 1, '')








