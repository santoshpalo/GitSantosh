import ClassLibrary as cl
import items as it
import FunctionLibrary as fl














if __name__ == "__main__":
    print('Name of the work = Restoration and renovation of Bhabagat Tungi  at Kaudiamunda\n')
    print('Estimated Cost :- Rs. 1,00,000.00','\t','Head of Account:-M.L.A.L.A.D.(2013-14)')
    print('='*85)
    print('Calculation of total centre line length')
    building = cl.Quantity([['long walls',1,5.44+.25],
                            ['short wall 1',2,2.29+.25]])
    building.tcl()
    print(it.items['m20'])
    slab = cl.Quantity([['lintel',1,10.52,0.25,0.15],
                        ['chajja',1,5.94,0.45,0.06],
                        ['slab',1,6.4,2.82,0.1],
                        ['beam',1,2.29,0.25,0.15]])
    slab.rate= 4293.3
    slab.volume()
    print(it.items['bmsscb'])
    walls = cl.Quantity([['walls',2,2.13,0.25,2.13],
                         ['front wall',1,5.94,0.25,2.6],
                         ['deduct pillars',-3,0.35,0.25,2.1],
                         ['door',-1,1.57,.25,2.13],
                         ['windows',-2,1.8,0.25,1.2]])
    walls.rate=2997.9
    walls.volume()
    print(it.items['rscs_slab'])
    slab=cl.Quantity([['slab',1,6.4,2.820],
                      ['wall bearing',-1,10.52,.25],
                      ['beam',-1,2.29,0.25]])
    slab.rate=305.67
    slab.hArea()
    print(it.items['rscs_beam'])
    beam=cl.Quantity([['beam',1,2.29,0.55]])
    beam.rate = 462.1
    beam.vArea()
    print(it.items['20cp(1:4)'])
    slab = cl.Quantity([['slab top',1,6.4,2.75]])
    slab.rate=140.24
    slab.hArea()
    print(it.items['12cp(1:6)'])
    walls= cl.Quantity([['walls',1,10.77,2.75],
                        ['verandah door',-0.5,1.57,2.1],
                        ['verandah windows',-1,1.8,1.2],
                        ])
    walls.rate= 84.9
    walls.vArea()
    print(it.items['16cp(1:6)'])
    walls= cl.Quantity([['walls',1,10.77-1,2.75],
                        ['verandah door',-0.5,1.57,2.1],
                        ['verandah windows',-1,1.8,1.2]
                        ])
    walls.rate = 119.19
    walls.vArea()
    print(it.items['CC(1:4:8)'])
    subbase = cl.Quantity([['room',1,5.33,2.15,0.1],
                           ])
    subbase.rate = 3052.46
    subbase.volume()
    print(it.items['wpcp'])
    finish_walls=cl.Quantity([['12mm thick plaster',1,26.49],
                              ['16mm thick plaster',1,23.75]])
    finish_walls.rate=12.72
    finish_walls.tcl()
    print('Labour charges = 50.00 sqm @ Rs.12.72/sqm =','Rs.{:.2f}'.format(round(50*12.72)))
    print(it.items['msdoor'])
    opening=cl.Quantity([['verandah door',1,1.57,2.1],
                        ['verandah windows',2,1.8,1.2]
                        ])
    opening.rate=63
    opening.ms_door_window()
    print(it.items['paint'])
    openings = cl.Quantity([['verandah door',2.25,1.57,2.1],
                        ['verandah windows',2*2.75,1.8,1.2]
                        
                        ])
    openings.rate=83.33
    openings.vArea()
    print(it.items['vitrified'])
    floor = cl.Quantity([['room',1,5.44,2.29]
                         ])
    floor.rate=839.55
    floor.hArea()
    print(it.items['walltile'])
    dado = cl.Quantity([['total length',1,15.44,0.2]])
    dado.rate = 252.21
    dado.vArea()
    print('\nCost and conveyance of HYSD bar = 2.15q @ Rs. 4000.00 = Rs.8600.00\n')
    print('''Cost and conveyance glazed ceramic precast wall tile = 3.09sqm
    @ Rs. 387.00/sqm =Rs.1196.00 ''')
    print('Cost and conveyance of water proofing cement paint 12.5kg @ Rs.35.00 /kg = Rs.438.00 ' )
    print('\nCost and conveyance of paint = 2.41l @ Rs. 193.00/l = Rs.465.00 ')
    print('\nCost and conveyance of primer = 1.04kg @ Rs. 116.00/kg = Rs.121.00')
    print('Provisional cost for Electrification = Rs.15000.00')
    print('\nProvisional cost for display board and photograph = Rs. 1000.00')
    print('\nCess for welfare of ;labourers= Rs.1000.00')
    print('='*85)
    print('\nTotal Estimated cost limited to Rs. 1,00,000.00\n')
    print(fl.signature(100000,'Rupees one lakh only',1,''))
    print('-'*95)
    slab = cl.Quantity([['main bottom 1',14,3.04,0.395],
                        ['main bottom 2',14,3.19,0.395],
                        ['main top',11,4.56,0.395],
                        ['main top 2',11,4.21,0.395],
                        ['verandah main 1',12,3.52,0.395],
                        ['verandah main 2',12,3.27,.395],
                        ['verandah dist',8,5.84,.395],
                        ['beam main',5,3.83,0.89],
                        ['beam extra',2,1.1,0.89],
                        ['stirrups',25,0.87,0.395],
                        ['distribution long',10+18+16,5.84,0.395],
                        ['distribution short',10+10,6.48,.395],
                        ['distribution short 1',16,3.9,.395],
                        ['extra top on walls',16,0.9,0.395],
                        ['extra top',16,0.7,0.395],
                        ['extra top',12,1.4,0.395]])
    slab.reinforcement()
    print('-'*95)
    slab = cl.Quantity([['front wall',4,5.48,0.62],
                        ['side walls',8,2.62,.62],
                        ['stirrups',71,0.68,0.395],
                        ['chajja bars',40,0.65,0.395],
                        ['chajja distributions',3,5.86,.395]])
    slab.reinforcement()
    print('-'*95)
    slab = cl.Quantity([['main bottom',11,2.59+.5+.15+2.59/4,0.395],
                        ['main bottom',11,3.3,0.395],
                        ['main top',20,2.7,0.395],
                        ['distribution long',16,5.78,.395],
                        ['distribution short',32,3.02-.08,0.395],
                        ['extra top',10,0.6,0.394],
                        ['extra top2',20,0.75,0.395],
                        
                        ['beam main',5,2.56,.89],
                        ['beam extra top',2,1.0,0.89],
                        ['beam stirrups',18,0.87,0.395]
                        ])
    slab.reinforcement()
    
    
    
    
    
    
    


