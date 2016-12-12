import ClassLibrary as cl 
import items as it
import FunctionLibrary as fl







if __name__ == "__main__":
    print(it.items['rcc'])
    slab = cl.Quantity([['slab ',1,6.8,4.85,0.1],
                        ['beam',1,4.52,0.25,0.25],
                        ['roof bend',1,20.98-.5,0.25,0.15]])
    slab.rate = 5156.18
    slab.volume()
    print(it.items['rscs_slab'])
    centering_slab = cl.Quantity([['slab ',1,6.8,4.85],
                        ['beam',-1,4.52,0.25],
                        ['roof bend',1,20.98-.5,0.05]])
    centering_slab.rate = 261.08
    centering_slab.hArea()
    print(it.items['rscs_beam'])
    centering_beam = cl.Quantity([
                        ['beam',3,4.5,0.25],
                        ])
    centering_beam.rate = 383.34
    centering_beam.vArea()
    print(it.items['hysd'])
    reinforcement = cl.Quantity([['main bottom1',20,2.9+.5+.3,0.395],
                                 ['main bottom2',20,2.9+2.9/4+.5+.15,.395],
                                 ['main top',2*13,4.05+.5+.3-.08,.395],
                                 ['distribution1',18,6.7,.395],
                                 ['distribution2',28,4.82-.08,.395],
                                 ['extra bar at top',26,0.95,0.395],
                                 ['extra bar at top2',20,0.8,0.395],
                                 ['stirrups',26,1.07,0.395],
                                 ['beam main bar',5,4.52-.08,0.89],
                                 ['beam extra top',2,1.5,0.89],
                                 ['roof bend long',8,6.4,0.62],
                                 ['roof bend short',8,4.45,0.62],
                                 ['roof bend stirrups',132,0.87,0.395]])
    reinforcement.reinforcement()
    print(it.items['20cp(1:4)'])
    grading = cl.Quantity([['slab',1,6.8,4.85]])
    grading.rate = 122.2
    grading.hArea()
    
    
    