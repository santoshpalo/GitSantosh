import FunctionLibrary as fl
import ClassLibrary as cl
import items as it














if __name__ == "__main__":
    tcl1 = cl.Quantity([['long wall 1',2,10.74],
             ['long wall 2',1,8.51],
             ['short wall 1',2,5.94],
             ['short wall 2',2,3.68],
             ['short wall 3',2,2.13]])
    tcl1.tcl()
    print(it.items['CC(1:5:10)'])
    metal_concrete = cl.Quantity([['class room',1,8.06,3.23,0.1],
                                  ['verandah,kitchen and store',3,2.49,1.68,0.1],
                                  ['toilets',1,3.23,1.8,0.1],
                                  ['steps entrance',1,1.5,1.0,0.1],
                                  ['kitchen exit',1,1.2,1.00,0.1],
                                  ['toilet steps',1,3,1.0,0.1]
                                  ])
    metal_concrete.rate=100
    metal_concrete.volume()
    print(it.items['m20'])
    rcc = cl.Quantity([['R.C.C. slab 1',1,11.29,4.23,0.1],
                       ['R.C.C. slab 2',1,9.06,2.13,0.1],
                       ['R.C.C. beams',2,.93,0.25,0.25],
                       ['R.C.C. roof bend',1,53.49-1,0.25,0.15],
                       ])
    rcc.rate=100
    rcc.volume()
    print(it.items['bmss'])
    brick_super_structure = cl.Quantity([['walls above lintel',1,53.49-2,0.25,0.6],
                                         ['toilet half brick walls',2,1.8,0.13,0.6]])
    brick_super_structure.rate = 100
    brick_super_structure.volume()
    brick_f_p = cl.Quantity([['entrance steps 1',1,1.5,1.00,0.25],
                             ['entrance steps 2',1,1.5,0.75,0.15],
                             ['entrance steps 3',1,1.5,0.50,0.15],
                             ['entrance steps 4',1,1.5,0.25,0.15],
                             ['kitchen steps 1',1,1.2,1.00,0.25],
                             ['kitchen steps 2',1,1.2,0.75,0.15],
                             ['kitchen steps 3',1,1.2,0.5,0.15],
                             ['kitchen steps 4',1,1.2,0.25,0.15],
                             ['toilet steps 1',1,3.00,1.00,0.25],
                             ['toilet steps 2',1,3.0,0.75,0.15],
                             ['toilet steps 3',1,3.0,0.5,0.15],
                             ['toilet steps 4',1,3.0,0.25,0.15]])
    brick_f_p.rate = 100
    brick_f_p.volume()
    print(it.items['rscs_slab'])
    centering_slab=cl.Quantity([['slab 1',1,11.29,4.23],
                                ['slab 2',1,9.06,2.13],
                                ['deduct beam',-2,3.93,0.25],
                                ['add roof bend',1,53.49-1,.05]])
    centering_slab.rate = 100
    centering_slab.hArea()
    print(it.items['rscs_beam'])
    centering_beam = cl.Quantity([['beams',2,3.93-.5,0.75]])
    centering_beam.rate = 100
    centering_beam.vArea()
    print(it.items['hysd'])
    print('\nProvisional Cost = 7.50q @ Rs.100.00/q = Rs. __________')
    print(it.items['12cp(1:6)'])
    12mmplaster = cl.Quantity([['alaround walls',1,53.49+1-2,3.15],
                               ['in the plinth',1,33.36+4*0.38,0.75],
                               ['add half brick thick walls',4,1.8,3.15],
                               ['ver openings',-1,2.5,2.1],
                               ['windows',-4*0.5,0.9,1.33],
                               ['Door-1',-0.5,1.2,2.1],
                               ['Door-2',-2*.5]])
    #===========================================================================
    # print(it.items.keys())
    #===========================================================================
    print("The area of your rectangle is {}cm\u00b2".format(5))
    
    
    
    
    