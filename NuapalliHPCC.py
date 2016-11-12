import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it
l = 4.5






if __name__ == "__main__":
    print('Construction of Community centre at Nuapalli H.P. of Binka N.A.C. ward no12')
    print('Estimated cost:-\u20B950,000.00\tHead of Account:-M.L.A.L.A.D.(2013-14)')
    print('-'*80)
    print(it.items['efhs'])
    foundation = cl.Quantity([['columns',2,1.5,1.5,1.2],
                              ['verandah long wall',1,l+.3,0.6,0.3],
                              ['verandah short walls',2,2.25-.125-1.5-.3,0.6,0.3]])
    foundation.rate =103.2
    foundation.volume()
    print(it.items['sand_fill'])
    sandfill = cl.Quantity([['footings',2,1.5,1.5,0.1],
                            ['verandah long wall',1,l+.3,0.6,0.1],
                            ['verandah short walls',2,2.25-.125-1.5-.3,0.6,0.1],
                            ['verandah sub base',1,4.8-.5,1.8-.25,0.45]])
    sandfill.rate=302.62
    sandfill.volume()
    print(it.items['CC(1:4:8)'])
    concrete = cl.Quantity([['footings',2,1.5,1.5,0.1],
                            ['verandah long wall',1,l+.3,0.6,0.1],
                            ['verandah short walls',2,2.25-.125-1.5-.3,0.6,0.1],
                            ['verandah sub base',1,4.8-.5,1.8-.25,0.1]])
    concrete.rate = 3059.86
    concrete.volume()
    print(it.items['bmfp'])
    brickwall=cl.Quantity([['longwall',1,4.8,0.25,1.00],
                           ['short walls',2,1.8,0.25,1.00]])
    brickwall.rate=3254.79
    brickwall.volume()
    print(it.items['m20'])
    rcc = cl.Quantity([['footings',2,1.2,1.2,0.3],
                       ['columns',2,0.25,0.25,4.5],
                       ['long beam',1,l+.25,0.25,0.25],
                       ['short beams',2,2.00,0.25,0.2],
                       ['slab',1,l+.25+.3,2.25,0.1]])
    rcc.rate = 4308.24
    rcc.volume()
    print(it.items['hysd'])
    print('\t\t\t\t\t   2.60q @ \u20B94534.45.00/qtl = \u20B9 11790')
    print(it.items['rscs_plinth'])
    footing=cl.Quantity([['footings',2*4,1.2,0.3],
                         ])
    footing.rate = 82.08
    footing.vArea()
    print(it.items['rscs_beam'])
    column = cl.Quantity([['columns',2*4,0.25,4.5],
                          ['beam',1,l-0.25,0.75],
                          ['short beams',2,2.0,0.65]])
    column.rate=462.1
    column.vArea()
    print(it.items['20cp(1:4)'])
    grading=cl.Quantity([['roof slab top',1,l+0.25+.3,2.25]])
    grading.rate=140.56
    grading.hArea()
    print(it.items['asfloor'])
    floor = cl.Quantity([['floor of verandah',1,4.5,2.18]])
    floor.rate=202.39
    floor.hArea()
    print(it.items['12cp(1:6)'])
    wallplaster=cl.Quantity([['long wall',1,4.5,0.6],
                             ['short walls',2,1.8,0.6]])
    wallplaster.rate=85.05
    wallplaster.vArea()
    print('\nCess for welfare of labourers = \u20B9500.00')
    print('\nDisplay board and photograph = \u20B9500.00')
    print('-'*80)
    fl.signature(50000, 'fifty thousan only', 1, '')
    
    
    
    
    
    
    
    
    
    
    