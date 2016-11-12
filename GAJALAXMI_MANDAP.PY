import ClassLibrary as cl
import items as it
import math as mt
import FunctionLibrary as fl








if __name__ == "__main__":
    print('Name of the work:-Completion of Gajalaxmi Puja Mandap at Baunsuni')
    print('Head of Account:-_______________\tEstimated Cost:-\u20B9__________')
    print('-'*80)
    print('Calculation of total centre line length :-')
    tcl = cl.Quantity([['long walls',2,6.6],
    ['short walls',2,5.35]])
    tcl.tcl()
    print(it.items['12cp(1:6)'])
    plaster12 = cl.Quantity([['total wall',1,23.9+1,3.9],
                             ['windows',-4,2.1,1.2],
                             ['door',-1,3.6,3.05]])
    plaster12.rate = 84.9
    plaster12.vArea()
    print(it.items['16cp(1:6)'])
    plaster16 = cl.Quantity([['total wall',1,23.9-1,3.3],
                             ['windows',-4,2.1,1.2],
                             ['door',-1,3.6,3.05]])
    plaster16.rate = 119.19
    plaster16.vArea()
    print(it.items['6cp(1:4)'])
    plaster6=cl.Quantity([['beam',1,5.1,.38*2+0.25],
                          ['chajja',4,2.4,0.5]])
    plaster6.rate = 89.66
    plaster6.hArea()
    print('''Supplying, fitting of stainless steel gate and window openings of 304
grade as per approved design and specification including buffing,
polishing and cost of T & P and all fixtures etc. complete.''')
    steel_gate=cl.Quantity([['front gate',1,3.6,3.05],
                            ['windows',4,2.1,1.2]])
    steel_gate.rate=2914.67
    steel_gate.vArea()
    
    print(it.items['vitrified'])
    floor=cl.Quantity([['hall',1,6.35,5.10],
                       ['steps',mt.pi,2.2,0.25]])
    floor.rate = 839.55
    floor.vArea()
    print(it.items['wall_tile'])
    wall_tile = cl.Quantity([['long walls',2,6.35,0.3],
                             ['short walls',2,5.1,0.9],
                             ['inside mandap',1,2.25,0.45],
                             ['inside mandap width',2,1.22,0.45],
                             ['steps1',mt.pi,2.18,0.15],
                             ['steps2',mt.pi,1.4,0.15],
                             ['steps3',mt.pi,0.8,0.15]])
    wall_tile.rate=242.21
    wall_tile.vArea()
    print(it.items['distemper'])
    print('\t\t\t\t81.40 sqm @ \u20B925.92 = \u20B9 2110.00')
    print(it.items['wall_paint'])
    print('\t\t\t\t\t76.05 sqm @ \u20B926.84= \u20B92041.00')
    print('\n\t\tCost of glazed ceramic tiles 17.17 sqm @\u20B9387.00 = \u20B96645')
    print('\n\t\t\tCost of distemper 81.40sqm \u20B966.00 = \u20B95372.00\n')
    print('\tCost of weather coat paint = 76.05 sqm @\u20B9192.00 = \u20B91824.00')
    print('\n\t\t\tProvisional cost for electirfication = \u20B920000.00')
    print('\n\t\t\tCess for welfare of labourers = \u20B91500.00')
    print('\n\t\t\tDepartmental contingency = \u20B91500.00')
    print('\n\t\t\tDisplay board and photograph = \u20B91500.00')
    print('-'*80)
    fl.signature(150000, 'one lakh fifty thousand only', 1, '')
    
    
    

    
    
    