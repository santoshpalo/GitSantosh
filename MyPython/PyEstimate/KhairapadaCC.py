import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it





if __name__ == "__main__":
    print('Name of the work :-Restoration & renovation of Bhagabat Mandir, Sankara Khairapada')
    print('\nHead of Account:-M.L.A.L.A.D (2013-14) \t Estimated Cost:-\u20B950,000.00 ')
    print('-'*80)
    tcl = cl.Quantity([['long wall',2,8.55],
                       ['short walls',3,3.65]])
    tcl.tcl()
    print(it.items['bmsscb'])
    brickmasonry = cl.Quantity([['alround wall',1,28.05,.38,1.3],
                                ['columns   ',-8,0.38,0.38,1.3]])
    brickmasonry.rate = 2967.79
    brickmasonry.volume()
    print(it.items['m20'])
    rcc = cl.Quantity([['R.C.C. plinth bend',1,28.05-.38,0.25,0.25],
                       ['R.C.C. columns',8,0.38,0.38,0.25]])
    rcc.rate = 4308.24
    rcc.volume()
    print(it.items['hysd'])
    reinf = cl.Quantity([['column bars',4*4,3.65,.89],
                         ['plinth bend long',2*4,8.55+.3,0.89],
                         ['plinth bend short',3*4,3.95,0.89],
                         ['stirrups',150,0.87,0.395]])
    reinf.reinforcement()
    print('\n\t\t\t\t\t1.75q @ \u20B9 4534.46 = \u20B9 7,935.00\n')
    print(it.items['rscs_plinth'])
    plinth_centering = cl.Quantity([['plinth bend',2,28.05-.25,.25]])
    plinth_centering.rate = 82.08
    plinth_centering.vArea()
    print('Cess for welfare of labourers = \u20B9500.00')
    print('Display board and photograph = \u20B9500.00')
    print('Work contingency = \u20B9 500.00')
    print('-'*80)
    fl.signature(50000, 'Fifty thousand only', 1, '')
   
    
    
    
    
    
    
    
    
    
    
    
    
    