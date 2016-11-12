import ClassLibrary as cl
import FunctionLibrary as fl
import items as it







if __name__ == "__main__":
    print("Name of the work:- Construction of Community Centre at Talipada, Baunsuni")
    print('Head of Account:-Biju K.B.K.(2016-17)\tEstimated Cost:-\u20B92,00,000.00')
    print('-'*80)
    print(it.items['efhs'])
    foundation = cl.Quantity([['larger columns',4,1.5,1.8,1.5]])
    foundation.rate = 103.20
    foundation.volume()  
    print(it.items['CC(1:4:8)'])     
    metal_concrete = cl.Quantity([['foundation trench',2,1.5,1.5,0.1]]) 
    metal_concrete.rate = 3280.94
    metal_concrete.volume()      
    print(it.items['m20']) 
    rcc = cl.Quantity([['R.C.C. columns footings',4,1.2,1.2,0.30],
                       ['R.C.C.pedestals',4,0.45,0.45,1.5],
                       ['R.C.C. columns',4,0.25,0.25,4.2],
                       ['R.C.C. lintel bend long wall',2,11,0.38,0.25],
                       ['R.C.C. lintel bend short wall',2,3.05,0.25,0.25],
                       ['R.C.C. lintel bend short wall',2,3.05,0.38,0.25],
                       ['R.C.C. roof bend long',2,11,0.38,0.15],
                       ['R.C.C. roof bend short',2,3.05,0.25,0.15],
                       ['R.C.C. roof bend short',2,3.05,0.38,0.15],
                       ['R.C.C. slab',1,11.3,3.95,0.12]])
    rcc.rate = 4277.30
    rcc.volume()
    print(it.items['hysd'])
    print('\t\t\t13.00quintalof HYSD bar @ \u20B94529.94 / qtl =  \u20B955,605.00')
    print(it.items['rscs_slab'])
    slab = cl.Quantity([['slab',1,11.3,3.95],
                        ['roof bend',2,11.00,-.38+2*0.15],
                        ['roof bend short1',2,2.89,-0.38+2*0.15],
                        ['roof bend short2',2,2.89,-0.25+2*0.15]])
    slab.rate = 305.67
    slab.hArea()
    print(it.items['rscs_lintel'])
    lintel = cl.Quantity([['verandah lintel',2*3,2.1,0.25],
                          ['verandah lintel front',3,3.15,0.25],
                          ['back side lintel',2*3,2.35,0.25],
                          ['back lintel',3,2.25,0.25],
                          ['hall lintel',2*2,6.1,0.15],
                          ['hall side lintel',2*2,2.89,0.15]])
    lintel.rate=195.11
    lintel.vArea()
    print(it.items['rscs_plinth'])
    footing = cl.Quantity([['footing sides',4*4,1.2,0.3]])
    footing.rate = 82.08
    footing.vArea()
    print(it.items['rscs_beam'])
    column= cl.Quantity([['columns',4*4,0.25,4.2]])
    column.rate=463.09
    column.vArea()
    print(it.items['bmss'])
    brick_ss = cl.Quantity([['hall walls long wall',2,6.1,0.38,1.5],
                            ['hall walls short walls',2,2.89,0.38,1.5],
                            ['verandah front wall',2,3.65-.5,1.5],
                            ['verandah side walls',2,2.1,0.25,1.5],
                            ['back side walls',4,2.35,0.25,1.5]])
    brick_ss.rate = 3274.35
    brick_ss.volume()
    print(it.items['bmfp'])
    brick_fp = cl.Quantity([['front verandah',1,3.65-0.5,0.25,1.10],
                            ['verandah sides',2,2.35,0.25,1.0],
                            ['hall entrnce',2,1.2,0.38,0.6]])
    brick_fp.rate=3241.35
    brick_fp.volume()
    print(it.items['20cp(1:4)'])
    grading = cl.Quantity([['roof slab top',1,11.3,3.95]])
    grading.rate = 140.20
    grading.hArea()
    print('\nCess for welfare of labourers = \u20B92,000.00')
    print('\nWork contingency = \u20B92,000.00')
    print('\nDisplay board and photograph = \u20B91,000.00')
    print('-'*80)
    print('Total estimated cost = \u20B92,14,063.00 limited to \u20B9 2,00,000.00')
    print('-'*80)
    fl.signature(200000, 'Two lakh rupees only', 1, '')
    
          
    
                              
    
    
    
    
    
              