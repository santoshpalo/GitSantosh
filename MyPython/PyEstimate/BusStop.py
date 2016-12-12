import ClassLibrary as cl
import items as it











if __name__ == "__main__":
    print(it.items['m20'])
    bus_stop = cl.Quantity([['long bench',1,5.92,0.45,.08],
                     ['short benches',2,2.97+0.25,0.45,0.08],
                     ['back side lintel',1,5.92+0.5,0.25,0.15],
                     ['both side lintels',2,2.97,0.25,0.15],
                     ['front side lintel',1,5.92+0.5,0.25,0.25],
                     ['front chajja',1,5.92+0.5,0.6,0.07],
                     ['chajja on windows',2,1.5,0.6,0.07],
                     ['columns',6,0.25,0.25,0.9]
                     ])
    bus_stop.rate=5137.08
    bus_stop.volume()
    print(it.items['hysd'])
    
    bus_stop=cl.Quantity([['long bench main',4,5.92-.08,.395],
                         ['short benches',2*4,2.97+.25-.08,.395],
                         ['distributions',80,.45-.08,0.395]])
    bus_stop.reinforcement()
    bus_stop=cl.Quantity([['front wall lintel reinforcement',5,5.84,0.89],
                          ['front wall extra top',2,1.2,0.89],
                          ['front wall extra top',1,0.95*2+.25,0.89],
                          ['back side walls main',4,5.92+.5-.08,0.62],
                          ['both side walls main bars',8,2.97+.5-.08,0.92],
                          ['extra on window openings openings',2,1.7,0.62],
                          ['front lintel stirrups',40,0.85,0.395],
                          ['stirrups on normal walls',74,0.65,0.395],
                          ['front and window chajja bars',65,0.6+.25-.08,0.395],
                          ['front chajja distributions',4,5.92+.5-.08],
                          ['window chajja distribution',2*4,1.42,0.395],
                          ['column stirrups',36,0.87,0.395]]
                         )
    bus_stop.reinforcement()
    bus_stop=cl.Quantity([['back side walls',1,5.92-0.25,0.25,0.9],
                          ['front side walls',1,5.92-0.25,0.25,0.8],
                          ['both side walls',2,2.97,0.25,0.9]])
    bus_stop.rate=2692.93
    bus_stop.volume()
    bus_stop=cl.Quantity([['lintel front 1',3,3.3,0.25],
                          ['lintel front2',2,2.37,0.25],
                          ['lintel over walls',1,5.92,0.15],
                          ['shrt walls ',2*2,2.97,0.15],
                          ['window bottoms',2,1.2,0.25],
                          ['bench bottoms',1,5.92-.45*3,0.45],
                          ['bench bottoms',2,2*2.97-.9,0.45]])
    bus_stop.rate= 179.08
    bus_stop.vArea()
    bus_stop=cl.Quantity([['front chajja',1,5.92+.5,0.6],
                          ['window chajjas',2,1.5,0.6]])
    bus_stop.rate = 264.11
    bus_stop.hArea()
    bus_stop=cl.Quantity([['columns',6*4,0.25,0.9]])
    bus_stop.rate = 396.62
    bus_stop.vArea()
    print('='*75)
    print (it.items['m20'])
    bus_stop= cl.Quantity([['slab',1,6.76,3.78,0.1],
                           ['roof bends long',2,6.42,0.25,0.15],
                           ['roof bend and beam',3,2.97,0.25,0.15]])
    bus_stop.volume()
    bus_stop = cl.Quantity([['']])
    print (it.items['hysd'])
    bus_stop=cl.Quantity([['beam main bars',5,3.39,0.89],
                          ['beam extra top',2,1.2,0.89],
                          ['roof bend long',2*4,6.42-.08,0.62],
                          ['roof bend short',2*4,3.47-.08,0.62],
                          ['beam and roof bend stirrups',140,0.87,0.395],
                          ['main bars bottom 1',15,4.19,.395],
                          ['main bar bottom 2',15,3.63,.395],
                          ['main bars at top',24,3.77,.395],
                          ['extra top on roof bends',24+15,0.8,.395],
                          ['Distributions long',16,6.73,.395],
                          ['Dstributions short',30,3.77,0.395]])
    bus_stop.reinforcement()
    print ('='*75)
    bus_stop=cl.reinforcement([2.83,2.97],[1,0,0,0],[2.83,0,0,0],[0.15,0.15])
    bus_stop.main_bottom_1()
    print ('='*75)
    print(it.items['rscs_slab'])
    bus_stop=cl.Quantity([['slab',1,6.76,3.78],
                          ['roof bends long',-2,6.42,0.25],
                          ['roof bends short',-3,2.97,0.25],
                          ['roof bends sides',4,6.42,0.15],
                          ['roof bends short',4,2.97,0.15]])
    bus_stop.hArea()
    print(it.items['rscs_beam'])
    bus_stop=cl.Quantity([['beams bottom',1,2.97,0.25+2*0.15]])
    bus_stop.hArea()
    print(it.items['20cp(1:4)'])
    bus_stop = cl.Quantity([['slab top',1,6.76,3.78]])
    bus_stop.hArea()
    
    
    
    
    
    
    