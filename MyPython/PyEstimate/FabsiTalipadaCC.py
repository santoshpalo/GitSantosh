import ClassLibrary as cl
import items as it
import FunctionLibrary as fl






if __name__ == "__main__":
    print('Name of the work:-Construction of community Mandap at Phabsi village\n')
    print('Head of Account :- M.P.L.A.D.(2015-16)','\t\t','Estimated Cost:-Rs.1,00,000.00\n')
    print('-'*80)
    
    
    print ('Calculation of total centre line length\n')
    building = cl.Quantity([['long walls',2,5.9],
                            ['short walls',2,2.45]])
    building.tcl()
    print(it.items['CC(1:4:8)'])
    metal_concrete = cl.Quantity([['mandap sub-base',1,5.65,2.18,0.1]])
    metal_concrete.rate =3280.94
    metal_concrete.volume()
    print (it.items['m20'])
    slab = cl.Quantity([['roof slab',1,7.32,3.15,0.1],
                        ['beam',1,2.2,0.25,0.15],
                        ['roof bends',1,17.2,0.25,.15]])
    slab.rate = 4277.3
    slab.volume()
    print(it.items['20cp(1:4)'])
    plaster20 = cl.Quantity([['slab top',1,7.32,3.15]])
    plaster20.rate =140.24
    plaster20.hArea()
    #------------------------------ print('\nCalculation of reinforcement bars')
    #---------------------------------------------------- v = cl.reinforcement()
    #--------------------------------------- v.end_support_condition = [0,0,0,1]
    #------------------------------------------- v.spacing_of_bars = [0.15,0.15]
    #------------------------------------------------------- v.span = [2.5,2.87]
    #--------------------------------------- v.trans_span_length=[0.15,0,0,2.87]
    #--------------------------------------------------------- v.main_bottom_1()
    #--------- slab_reinforcement = cl.Quantity([['main bottom 1',6,3.15,0.395],
                                      #---------- ['main bottom2',6,3.15,0.395],
                                      #------------ ['main top 1',6,3.67,0.395],
                                      #----------- ['main top 2',6,4.24,0.395]])
    #---------------------------------------- slab_reinforcement.reinforcement()
    #------- slab_reinforcement_1 = cl.Quantity([['main bottom 1',6,3.15,0.395],
                                      #---------- ['main bottom2',6,3.15,0.395],
                                      #------------ ['main top 1',6,3.67,0.395],
                                      #----------- ['main top 2',6,4.24,0.395]])
    #-------------------------------------- slab_reinforcement_1.reinforcement()
    print(it.items['12cp(1:6)'])
    plaster12 = cl.Quantity([['wall alround',1,16.7+1,3.3],
                             ['openings in long wall',-2,2.69,2.5],
                             ['openings in short walls',-1,2.2,2.5]])
    plaster12.rate = 84.9
    plaster12.vArea()
    print(it.items['16cp(1:6)'])
    plaster16= cl.Quantity([['wall alround',1,16.7-1,3.3],
                             ['openings in long wall',-2,2.69,2.5],
                             ['openings in short walls',-1,2.2,2.5]])
    plaster16.rate = 119.19
    plaster16.vArea()
    print(it.items['6cp(1:4)'])
    plaster6=cl.Quantity([['columns',4*2,0.25,2.5]])
    plaster6.rate = 93.66
    plaster6.vArea()
    print(it.items['vitrified'])
    floor_tile = cl.Quantity([['floor of mandap',1,5.9,2.45],
                              ['step 1&2',1,2.7,0.3],
                              ['step 3',1,2.7,0.45]])
    floor_tile.rate = 839.55
    floor_tile.hArea()
    print(it.items['wall_tile'])
    wall_tile=cl.Quantity([['long wall',1,5.9,0.9],
                           ['short wall',1,2.45,0.9],
                           ['steps',3,2.7,0.9]])
    wall_tile.rate = 242.21
    wall_tile.hArea()
    print(it.items['wpcp'])
    print('total plaster area = 100.43sqm @ ','\u20B9{:.2f} ='.format(20.87),'\u20B9{:.2f}'.format(round(100.43*20.87)))
    print(it.items['hysd'])
    print('\n2.60Q @ ','\u20B9{:.2f} ='.format(4529.94),'\u20B9{:.2f}'.format(round(2.6*4529.94)))
    print('\nCost and conveyance of M.S. doors and windows 2.60Q','\u20B9{:.2f} ='.format(6300),'\u20B9{:.2f}'.format(round(2.6*6300)))
    print(it.items['rscs_slab'])
    slab = cl.Quantity([['slab',1,7.32,3.15],
                        ['roof bend',1,16.7,.05]
                        ])
    slab.rate = 305.67
    slab.hArea()
    print(it.items['rscs_beam'])
    slab = cl.Quantity([['beam',1,2.2,0.55]
                        
                        ])
    slab.rate = 462.1
    slab.hArea()
    print(it.items['paint'])
    paint =cl.Quantity([['grills 1',2,2.69,2.5],
                        ['grills 2',1,2.2,2.5]])
    paint.rate = 106.74
    paint.vArea()
    print('\nProvisional cost for Electrification = ','\u20B9{:.2f}'.format(11500))
    print('\nCess for welfare of labourers  = \u20B9 1000.00')
    print('\nDepartmental contingency  = \u20B9 1000.00')
    print('\nDisplay board and photograph  = \u20B9 1000.00')
    print('-'*80)
    fl.signature(100000, 'Rupees one lakh only', 1, '')
    print('-'*80)
    slab = cl.Quantity([['beam main',5,2.2+.5-.08,0.89],
                        ['beam extra at top',2,1.5,0.89],
                        ['beam stirrups',18,0.87,0.395],
                        ['roof bend long',2*4,5.9+.25-.08,0.62],
                        ['roof bend short',2*4,2.2+.5-.08,0.62],
                        ['roof bend stirrups ',5.9/0.15*2-6+2.2/.15*2,0.87,0.395],
                        ['slab main1',6,2.7+.5+.3,0.395],
                        ['slab main2',6,2.7+0.5+.15+2.7/4,.395],
                        ['slab main3',6,2.7+.5+.45+2.7/4,0.395],
                        ['slab main4',6,2.7+.5+.15+0.9,0.395],
                        ['slab main top',24,2.2+.5+.15,.395],
                        ['distribution long',12,7.2,0.395],
                        ['distribution short',30
                         ,2.2+.5+.15,0.395],
                        ['extra bar at top',6,0.9*2+.25,0.395],
                        ['extra at top1',6,0.9,0.395],
                        ['extra at top2',6*2*2,.9,.395]
                        ])
    slab.reinforcement()
    
    
          
    
    
    
    
    
        

    