import ClassLibrary as cl
import items as it
import FunctionLibrary as fl














if __name__ == "__main__":
    print('Name of the work = Completion of C.C. building at Kaudiamunda Nuapada\n')
    print('Estimated Cost :- Rs. 1,60,000.00','\t','Head of Account:-fourth S.F.C.(2015-16)')
    print('='*85)
    print('Calculation of total centre line length')
    building = cl.Quantity([['long walls',3,5.28],
                            ['short wall 1',2,3.66],
                            ['short wall 2',2,2.26]])
    building.tcl()
    print(it.items['m20'])
    slab = cl.Quantity([['slab',1,7.00,5.8,0.1],
                        ['beam',1,3.4,0.25,0.25]])
    slab.rate= 4293.3
    slab.volume()
    print(it.items['bmsscb'])
    walls = cl.Quantity([['walls',1,27.68,0.25,0.08]])
    walls.rate=2997.9
    walls.volume()
    print(it.items['rscs_slab'])
    slab=cl.Quantity([['slab',1,7.00,5.80],
                      ['roof bend',-1,27.68,.25],
                      ['beam',-1,3.4,0.25]])
    slab.rate=305.67
    slab.hArea()
    print(it.items['rscs_beam'])
    beam=cl.Quantity([['beam',3,3.4,0.25]])
    beam.rate = 462.1
    beam.vArea()
    print(it.items['20cp(1:4)'])
    slab = cl.Quantity([['slab top',1,7.00,5.8]])
    slab.rate=140.24
    slab.hArea()
    print(it.items['12cp(1:6)'])
    walls= cl.Quantity([['walls',1,27.68+1-0.25,3.2],
                        ['verandah door',-0.5,2.21,1.98],
                        ['verandah windows',-1,0.6,1.35],
                        ['room door',-0.5,1.08,1.98],
                        ['room windows',-1,0.69,1.08],
                        ['room window 2',-0.5,0.8,0.85]])
    walls.rate= 84.9
    walls.vArea()
    print(it.items['16cp(1:6)'])
    walls= cl.Quantity([['walls',1,27.68-1-3*0.25,3.2],
                        ['verandah door',-0.5,2.21,1.98],
                        ['verandah windows',-1,0.6,1.35],
                        ['room door',-0.5,1.08,1.98],
                        ['room windows',-1,0.69,1.08],
                        ['room window 2',-0.5,0.8,0.85],
                        ['plinth plaster',1,5.28*2+3.66*2+2.26*2+1,0.45]])
    walls.rate = 119.19
    walls.vArea()
    print(it.items['CC(1:4:8)'])
    subbase = cl.Quantity([['room',1,4.9,3.23,0.1],
                           ['verandah',1,4.9,1.8,0.1]])
    subbase.rate = 3052.46
    subbase.volume()
    print(it.items['wpcp'])
    finish_walls=cl.Quantity([['12mm thick plaster',1,85.82],
                              ['16mm thick plaster',1,88.35]])
    finish_walls.rate=12.72
    finish_walls.tcl()
    print('Labour charges = 174.00 sqm @ Rs.12.72/sqm =','Rs.{:.2f}'.format(round(174.00*12.72)))
    print(it.items['msdoor'])
    opening=cl.Quantity([['verandah door',1,2.21,1.98],
                        ['verandah windows',2,0.6,1.35],
                        ['room door',1,1.08,1.98],
                        ['room windows',2,0.69,1.08],
                        ['room window 2',1,0.8,0.85]])
    opening.rate=63
    opening.ms_door_window()
    print(it.items['paint'])
    openings = cl.Quantity([['verandah door',2.25,2.21,1.98],
                        ['verandah windows',2*2.75,0.6,1.35],
                        ['room door',2.25,1.08,1.98],
                        ['room windows',2*2.75,0.69,1.08],
                        ['room window 2',2.75,0.8,0.85]
                        ])
    openings.rate=83.33
    openings.vArea()
    print(it.items['vitrified'])
    floor = cl.Quantity([['room',1,5.03,3.4],
                         ['verandah',1,5.03,2.01]])
    floor.rate=839.55
    floor.hArea()
    print(it.items['walltile'])
    dado = cl.Quantity([['total length',1,28-4*.25-3*.25,0.2]])
    dado.rate = 252.21
    dado.vArea()
    print('\nCost and conveyance of HYSD bar = 3.65q @ Rs. 4000.00 = Rs.14600.00\n')
    print('''Cost and conveyance glazed ceramic precast wall tile = 5.25sqm
    @ Rs. 387.00/sqm =Rs.2032.00 ''')
    print('Cost and conveyance of water proofing cement paint 43.5kg @ Rs.35.00 /kg = Rs.1523.00 ' )
    print('\nCost and conveyance of paint = 3.14l @ Rs. 193.00/l = Rs.606.00 ')
    print('\nCost and conveyance of primer = 1.35kg @ Rs. 116.00/kg = Rs.117.00')
    print('Provisional cost for Electrification = Rs.5000.00')
    print('\nProvisional cost for display board and photograph = Rs. 1000.00')
    print('\nCess for welfare of ;labourers= Rs.1600.00')
    print('='*85)
    print('\nTotal Estimated cost limited to Rs. 1,60,000.00\n')
    print(fl.signature(160000,'Rupees one lakh sixty thousand only',1,''))
    
    
    
    
    
    
    


