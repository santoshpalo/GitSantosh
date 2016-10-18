import ClassLibrary as cl
print ('Calculation of total centre line length')
building = cl.Quantity([['long walls',2,6.2],
                        ['short walls',2,2.5]])
building.tcl()
print ("R.c.c. work")
slab = cl.Quantity([['roof slab',1,7.32,3.15,0.1],
                    ['beam',1,2.5,0.25,0.15],
                    ['roof bends']])
slab.data = [['roof slab',1,7.32,3.15,0.1]]
slab.volume()
print("20 mm thick grading plaster")
slab.data =[['slab top',1,7.32,3.15]]
slab.hArea()
print('\nCalculation of reinforcement bars')
v = cl.reinforcement()
v.end_support_condition = [0,0,0,1]
v.spacing_of_bars = [0.15,0.15]
v.span = [2.5,2.87]
v.trans_span_length=[0.15,0,0,2.87]
v.main_bottom_1()
slab_reinforcement = cl.Quantity([['main bottom 1',6,3.15,0.395],
                                  ['main bottom2',6,3.15,0.395],
                                  ['main top 1',6,3.67,0.395],
                                  ['main top 2',6,4.24,0.395]])
slab_reinforcement.reinforcement()
slab_reinforcement_1 = cl.Quantity([['main bottom 1',6,3.15,0.395],
                                  ['main bottom2',6,3.15,0.395],
                                  ['main top 1',6,3.67,0.395],
                                  ['main top 2',6,4.24,0.395]])
slab_reinforcement_1.reinforcement()

    