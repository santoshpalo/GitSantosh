import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it






if __name__ == "__main__":
    print(it.items['rcc'])
    slab = cl.Quantity([['slab ',1,8.53,4.25,0.1],
                        ['beam',1,4.05,0.25,0.15],
                        ['roof bend long',2,8.35,0.25,0.15],
                        ['oof bend short',3,3.55,0.25,0.15]])
    slab.rate = 4872.24
    slab.volume()
    print(it.items['rscs_slab'])
    centering_slab = cl.Quantity([['slab ',1,8.53,4.25],
                        ['beam',-1,4.05,0.25],
                        ['roof bend',1,27.35,0.05]])
    centering_slab.rate = 258.88
    centering_slab.hArea()
    print(it.items['rscs_beam'])
    centering_beam = cl.Quantity([
                        ['beam',1,3.55,0.55],
                        ])
    centering_beam.rate = 391.57
    centering_beam.vArea()
    reinforcement = cl.Quantity([['beam main',5,4.05,0.89],
                                ['roof bend long',2*4,8.35,0.62],
                                ['roof bend short',3*4,3.55+.5,0.62],
                                ['stirrups ',208,0.87,0.395],
                                ['main bottom1',9,2.84,0.395],
                                ['main bar bottom2',9,3.33,0.395],
                                ['main bar bottom 3',9,3.78,.395],
                                ['main bar bottom 4',9*2,3.88,0.395],
                                ['main bar bottom ',9,3.39,0.395],
                                ['main bar top',3*10,4.19,0.395],
                                ['distribution long',12,8.45,.395],
                                ['distribution short',34,4.2,0.395],
                                ['extra top',30,0.9,.395],
                                ['extra top',9,0.65,0.395]
                                ])
    reinforcement.reinforcement()
    
    
    