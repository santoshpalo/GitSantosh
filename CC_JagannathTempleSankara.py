import ClassLibrary as cl
import items as it
import FunctionLibrary as fl










if __name__ == "__main__":
    print('Name of the work :-Construction of community centre at Jagannath Temple Sankara')
    print('\nEstimated Cost:-','\u20B9{:.2f}'.format(500000),'\t','Head of Account:-W.O.D.C.(2015-16)')
    centre_line=cl.Quantity([['walls',6,9]
                             ])
    
    centre_line.tcl()
    print(it.items['efhs'])
    foundation_trench=cl.Quantity([['column trenches',9,1.5,1.5,1.5],
                                   ['walls foundation',1,54-9*1.5,0.6,0.75]])
    foundation_trench.rate=103.2
    foundation_trench.volume()
    print(it.items['CC(1:4:8)'])
    metal_concrete=cl.Quantity([['column trenches',9,1.5,1.5,0.1],
                                ['walls',1,54-9*1.5,0.1],
                                ['room',4,4.19,4.19,0.1],
                                ['steps',4,1.2,1.25,0.1]])
    metal_concrete.rate = 3280.94
    metal_concrete.volume()
    print(it.items['m20'])
    m20rcc=cl.Quantity([['column footings',9,1.2,1.2,0.25],
                        ['pedestals',9,0.45,0.45,1.5],
                        ['columns',9,0.25,0.25,3.15],
                        ['plinth beam',1,54-3*0.25,0.25,0.38],
                        ['lintel bend',1,2*9+3*4.25,0.25,0.15],
                        ['lintel beams',1,9+.25+4.25*2,0.25,0.25],
                        ['partition wall',1,4.25,0.13,0.15],
                        ['store racks',3,4.25,0.45,0.06],
                        ['window chajjas',2,1.2,0.06],
                        ['verandah long chajjas',1,9+0.25,0.45,0.06],
                        ['wall beams',1,54.0-3*0.25,0.25,0.15],
                        ['slab',1,9.25,9.55,0.1]
                        ])
    m20rcc.rate = 4277.3
    m20rcc.volume()
    print(it.items['bmfp'])
    brick_masonry_fp = cl.Quantity([['wall in F &P',1,36.0-8*0.38,0.38,0.85]])
    brick_masonry_fp.rate=3241.35
    brick_masonry_fp.volume()
    print(it.items['bmss'])
    bm_ss = cl.Quantity([['walls above plinth',1,54.0-12*0.25,0.25,3.0],
                         ['half brick partition',1,4.25,0.13,3.0],
                         ['deduct door1',-1,1.2,0.25,2.1],
                         ['deduct door2',-2,0.9,0.25,2.1],
                         ['deduct windows',-2,0.9,0.25,1.2],
                         ['deduction for verandah opg.',-5,4.25,0.25,2.1],
                         ])
    bm_ss.rate = 3241.35+33
    bm_ss.volume()
    print(it.items['hysd'])
    print('\n\t\t\t\t\t    24.00qtl @ ','\u20B9{:.2f}'.format(4529.94),'=','\u20B9{:.2f}'.format(4529.94*24))
    print(it.items['12cp(1:6)'])
    plaster12 = cl.Quantity([['walls alround',1,54+1-3*0.25,3.0],
                              ['half brick partition',2,4.25,3.0],
                              ['deduct door1',-1.0/2,1.2,2.1],
                              ['deduct door2',-2.0/2,0.9,2.1],
                              ['deduct windows',-2.0/2,0.9,1.2],
                              ['deduction for verandah opg.',-5,4.25,2.1]]
                             
                              )
    plaster12.rate =84.9
    plaster12.vArea()
    print(it.items['16cp(1:6)'])
    plaster16 = cl.Quantity([['walls alround',1,54-1-3*0.25,3.0],
                              ['plinth plaster',1,9.38*4,0.75],
                              ['deduct door1',-1.0/2,1.2,2.1],
                              ['deduct door2',-2.0/2,0.9,2.1],
                              ['deduct windows',-2.0/2,0.9,1.2],
                              ['deduction for verandah opg.',-5,4.25,2.1]]
                             
                              )
    plaster16.rate =119.19
    plaster16.vArea()
    print(it.items['20cp(1:4)'])
    plaster20=cl.Quantity([['roof slab top',1,9.55,9.25]])
    plaster20.rate = 140.24
    plaster20.hArea()
    print(it.items['6cp(1:4)'])
    plaster6 = cl.Quantity([['store racks',3,4.25,0.5],
                        ['window chajjas',2,1.2,0.5],
                        ['verandah long chajjas',1,9+0.25,0.5],
                        ['beams',1,4.25,0.25+2*0.15],
                        ['slab',2,(9.25+9.55),0.1],
                        ['columns',3*4,0.25,2.1]
                        ])
    plaster6.rate = 93.66
    plaster6.vArea()
    
    print(it.items['asfloor'])
    
    floor=cl.Quantity([['total plinth area',1,9.38,9.38],
                       ['wall area',-1,9.25*2+3*4.25+4.25*0.13,0.25],
                       ['add for steps',4,1.2,1.5]])
    floor.rate=202.02
    floor.hArea()
    print(it.items['msdoor'])
    print('\t\t\t\t3.00Qtl','@ \u20B9{:.2f}/quintal = '.format(6300),'\u20B9{:.2f} '.format(18900))
    print(it.items['paint'])
    paintp = cl.Quantity([['door1',2.25,1.2,2.1],
                          ['door2',2*2.25,0.9,2.1],
                          ['windows',2*2.75,0.9,1.2]])
    paintp.rate=106.74
    paintp.vArea()
    print(it.items['wpcp'])
    print('\t\t\t\t\t387.27 sqm ','@ \u20B9{:.2f}/ sqm ='.format(20.87),'\u20B9{:.2f}'.format(round(20.87*387.27)))
    print('\n',it.items['rscs_plinth'])
    plinth_centering = cl.Quantity([['footings of columns',9,1.2,0.25]
                                    ])
    plinth_centering.rate =82.08
    plinth_centering.vArea()
    print(it.items['rscs_slab'])
    slab_centering = cl.Quantity([['slab',1,9.55,9.25],
                                   ['roof bend',1,54.0-3*0.25-4.25,.05],
                                   ['chajjas',1,9.25,0.45],
                                   ['store room shelves',3,4.25,0.45],
                                   ['window chajjas',2,1.2,0.45]])
    slab_centering.rate = 305.67
    slab_centering.vArea()
    beam_centering = cl.Quantity([['columns',9*4,0.25,3.0+1.0],
                                  ['beam',1,4.25,.55]])
    beam_centering.rate=463.09
    beam_centering.vArea()
    print(it.items['rscs_lintel'])
    lintel_centering = cl.Quantity([['sides of lintel bend',1,(9.25*2+4*4.25),0.15],
                                    ['bottoms of door1',1,1.2,0.25],
                                    ['bottoms of door2',2,0.9,0.25],
                                    ['windows',2,0.9,0.25],
                                    ['lintel beam',1*9+4.25*2,0.75]])
    lintel_centering.rate =195.11
    lintel_centering.vArea()
    print('\n\tProvisional cost towards Display Board and photograph = ','\u20B9{:.2f}'.format(5000),'\n')
    print('\t\t\t\tCess for welfare of labourers','= \u20B9{:.2f}'.format(5000),'\n')
    print('-'*80)
    fl.signature(500000, 'Five lakh only ', 2, '')
    
    
    
    
    
    
    