import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it









if __name__ == "__main__":
    print('Name of the Work:- Construction of C.C. road from P.M.G.S.Y to Hospital road')
    print('Head of Account:-B.R.G.F. (2014-15)\tEstimated Cost:-\u20B93,00,000.00')
    print('-'*80)
    print(it.items['efhs'])
    foundation = cl.Quantity([['cut-off walls',2,82.5,0.2,0.2]])
    foundation.rate = 103.2
    foundation.volume()
    print(it.items['sand_fill'])
    sand_fill = cl.Quantity([['road subgrade',1,82.5,3.65-.4,.05]])
    sand_fill.rate = 302.62
    sand_fill.volume()
    print(it.items['CC(1:3:6)'])
    metal_concrete = cl.Quantity([['cut-off walls',2,82.5,0.2,0.25],
                                  ['sub-base concrete',1,82.5,3.65,0.1]
                                  ])
    metal_concrete.rate = 3647.57
    metal_concrete.volume()
    print(it.items['CC(1:2:4)'])
    chips_concrete = cl.Quantity([['crust of the road',1,82.5,3.65,0.1]])
    chips_concrete.rate =4760.71
    chips_concrete.volume()
    print(it.items['rscs_plinth'])
    cut_off = cl.Quantity([['outside cut-off',2,82.5,0.05+.2],
                           ['inside cut-off',2,82.5,0.05]])
    cut_off.rate = 82.08
    cut_off.vArea()
    print('\nCost towards hire and running of plate vibrator')
    print('\n\t\t\t12.04 hour @ \u20B9 106.00/ hour = \u20B9 1276.00')
    print('\n\t\t\tCess for welfare of labourers = \u20B9 3000.00')
    print('\n\t\t\tDepartmental contingency \u20B9 3000.00')
    print('\n\t\t\tDisplay board and photograph = \u20B9 2000.00')
    print('-'*80)
    fl.signature(3000,'Rupees three lakh only', 1, '')
    
    
    
    
    
    
    
     