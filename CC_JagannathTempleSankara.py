import ClassLibrary as cl
import items as it










if __name__ == "__main__":
    print('Name of the work :-Construction of community centre at Jagannath Temple Sankara')
    print('\nEstimated Cost:-','\u20B9{:.2f}'.format(500000),'\t','Head of Account:-W.O.D.C.(2015-16)')
    centre_line=cl.Quantity([['long walls',2,9],
                             ['short walls',2,4.25]])
    centre_line.tcl()
    print(it.items['efhs'])
    foundation_trench=cl.Quantity([['column trenches',6,1.5,1.5,1.5],
                                   ['walls foundation',1,26.5-6*1.5,0.6,0.75]])
    foundation_trench.rate=103.2
    foundation_trench.volume()
    print(it.items['CC(1:4:8)'])
    metal_concrete=cl.Quantity([['column trenches',6,1.5,1.5,0.1],
                                ['walls',1,2.65-6*0.38,0.1],
                                ['room',2,4.25-.06,4.25-.38,0.1],
                                ['steps',4,1.2,1.25,0.1]])
    metal_concrete.rate = 3280.94
    metal_concrete.volume()
    print(it.items['m20'])
    m20rcc=cl.Quantity([['column footings',6,1.2,1.2,0.25],
                        ['pedestals',6,0.45,0.45,1.5],
                        ['columns',6,0.25,0.25,3.15],
                        ['plinth beam',1,26.5+4.25,0.25,0.38],
                        ['lintel bend',1,26.5+4.25,0.25,0.15],
                        ['partition wall',1,4,0.13,0.15],
                        ['store racks',3,4.25,0.45,0.06],
                        ['window chajjas',2,1.2,0.06],
                        ['wall beams',1,26.5+4,0.25,0.15],
                        ['slab',1,9.00,4.25+.25+.15+1.2,0.1]
                        ])
    m20rcc.rate = 4277.3
    m20rcc.volume()
    print(it.items['bmfp'])
    brick_masonry_fp = cl.Quantity([['wall in F &P',1,26.5-6*0.45,0.38,0.85]])
    brick_masonry_fp.rate=3241.35
    brick_masonry_fp.volume()
    print(it.items['bmss'])
    bm_ss = cl.Quantity([['walls above plinth',1,26.5+4-6*0.25,0.25,3.0],
                         ['deduct door1',-1,1.2,0.25,2.1],
                         ['deduct door2',-2,0.9,0.25,2.1],
                         ['deduct windows',-2,0.9,0.25,1.2]])
    bm_ss.rate = 3241.35+33
    bm_ss.volume()
    print(it.items['hysd'])
    print('\n\t\t\t\t\t    15.00qtl @ ','\u20B9{:.2f}'.format(4529.94),'=','\u20B9{:.2f}'.format(4529.94*15))
    print(it.items[''])
    
    
    
    