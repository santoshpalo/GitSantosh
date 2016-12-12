import ClassLibrary as cl
import items as it
import FunctionLibrary as fl










if __name__ == "__main__":
    print('''Name of the work :-Construction of Additional class room at
+3 degree college at Baunsuni''')
    print('\nEstimated Cost:-','\u20B9{:.2f}'.format(500000),'\t','Head of Account:-W.O.D.C.(2015-16)')
    print('-'*80)
    centre_line=cl.Quantity([['long walls',3,10.25],
                             ['short walls1',2,5.25],
                             ['short walls2',2,2.05]
                             ])
    
    centre_line.tcl()
    print(it.items['efhs'])
    foundation_trench=cl.Quantity([['column trenches',11,1.5,1.5,1.5],
                                   ['walls foundation',1,45.35-11*1.5,0.6,0.75]])
    foundation_trench.rate=103.2
    foundation_trench.volume()
    print(it.items['CC(1:4:8)'])
    metal_concrete=cl.Quantity([['column trenches',11,1.5,1.5,0.1],
                                ['walls',1,45.35-11*1.5,0.1],
                                ['room',4,10.25-.38,10.25-.38,0.1],
                                ['steps',2,1.2,1.25,0.1]])
    metal_concrete.rate = 3280.94
    metal_concrete.volume()
    print(it.items['m20'])
    m20rcc=cl.Quantity([['column footings',11,1.2,1.2,0.25],
                        ['pedestals',11,0.45,0.45,1.5],
                        ['columns',11,0.25,0.25,3.15],
                        ['plinth beam',1,45.35-0.25,0.25,0.38],
                        ['lintel bend',1,45.35-0.25,0.25,0.15],
                        ['extra thick lintel beams',1,10.5+2*1.8,0.25,0.1],
                        
                        
                        ['window chajjas',3,1.2,0.06],
                        ['verandah long chajjas',1,10.5,0.45,0.06],
                        ['wall beams',1,45.35-0.25,0.25,0.15],
                        ['slab',1,10.8,6.8+.75+.3,0.1],
                        ['beams',2,5.5,0.25,0.25]
                        ])
    m20rcc.rate = 4277.3
    m20rcc.volume()
    print(it.items['bmfp'])
    brick_masonry_fp = cl.Quantity([['wall in F &P',1,35.1-9*0.45,0.38,0.85]])
    brick_masonry_fp.rate=3241.35
    brick_masonry_fp.volume()
    print(it.items['bmss'])
    bm_ss = cl.Quantity([['walls above plinth',1,45.35-11*0.25,0.25,3.0],
                         
                         ['deduct door1',-2,1.2,0.25,2.1],
                         
                         ['deduct windows',-4,0.9,0.25,1.2],
                         ['deduction for verandah opg.',-2,4.88,0.25,2.1],
                         ['deduction of verandah openings2',-2,1.8,0.25,2.1]
                         ])
    bm_ss.rate = 3241.35+33
    bm_ss.volume()
    print(it.items['hysd'])
    print('\n\t\t\t\t\t    24.00qtl @ ','\u20B9{:.2f}'.format(4529.94),'=','\u20B9{:.2f}'.format(4529.94*24))
    print(it.items['12cp(1:6)'])
    plaster12 = cl.Quantity([['walls alround',1,45.35+1-0.25,3.0],
                              
                              ['deduct door1',-2.0/2,1.2,2.1],
                              
                              ['deduct windows',-4.0/2,0.9,1.2],
                              ['deduction for verandah opg.',-2,4.88,2.1],
                              ['deduction of verandah openings2',-2,1.8,2.1]]
                             
                              )
    plaster12.rate =84.9
    plaster12.vArea()
    print(it.items['16cp(1:6)'])
    plaster16 = cl.Quantity([['walls alround',1,45.35-1-0.25,3.0],
                              ['plinth plaster',1,9.38*4,0.75],
                              ['deduct door1',-2.0/2,1.2,2.1],
                              ['deduct windows',-4.0/2,0.9,1.2],
                              ['deduction for verandah opg.',-2,4.88,2.1],
                              ['deduction of verandah openings2',-2,1.8,2.1]]
                              )
    plaster16.rate =119.19
    plaster16.vArea()
    print(it.items['20cp(1:4)'])
    plaster20=cl.Quantity([['roof slab top',1,10.8,5.5+1.8+.25+.3]])
    plaster20.rate = 140.24
    plaster20.hArea()
    print(it.items['6cp(1:4)'])
    plaster6 = cl.Quantity([
                        ['window chajjas',3,1.2,0.5],
                        ['verandah long chajjas',1,10.5,0.5],
                        ['beams',2,5.0,0.25*3],
                        ['slab',2,(10.5+6.8+.75+.3),0.1],
                        ['columns',3*4,0.25,2.1]
                        ])
    plaster6.rate = 93.66
    plaster6.vArea()
    
    print(it.items['asfloor'])
    
    floor=cl.Quantity([['total plinth area',1,10.5,5+1.8+.75],
                       ['wall area',-1,45.35-.25,0.25],
                       ['add for steps',4,1.2,1.5]])
    floor.rate=202.02
    floor.hArea()
    print(it.items['msdoor'])
    print('\t\t\t\t3.00Qtl','@ \u20B9{:.2f}/quintal = '.format(6300),'\u20B9{:.2f} '.format(18900))
    print(it.items['paint'])
    paintp = cl.Quantity([['door1',2.25*2,1.2,2.1],
                          
                          ['windows',4*2.75,0.9,1.2]])
    paintp.rate=106.74
    paintp.vArea()
    print(it.items['wpcp'])
    print('\t\t\t\t\t332.97 sqm ','@ \u20B9{:.2f}/ sqm ='.format(20.87),'\u20B9{:.2f}'.format(round(20.87*332.97)))
    print('\n',it.items['rscs_plinth'])
    plinth_centering = cl.Quantity([['footings of columns',11,1.2,0.25]
                                    ])
    plinth_centering.rate =82.08
    plinth_centering.vArea()
    print(it.items['rscs_slab'])
    slab_centering = cl.Quantity([['slab',1,10.8,5+1.8+.75+.3],
                                   ['roof bend',1,45.35-0.25,.05],
                                   ['chajjas',1,10.5+2*2.2,0.45],
                                   
                                   ['window chajjas',3,1.2,0.45]])
    slab_centering.rate = 305.67
    slab_centering.vArea()
    beam_centering = cl.Quantity([['columns',11*4,0.25,3.0+1.0],
                                  ['beam',1,5.0,.75]])
    beam_centering.rate=463.09
    beam_centering.vArea()
    print(it.items['rscs_lintel'])
    lintel_centering = cl.Quantity([['sides of lintel bend',1,45.35-0.25,0.15],
                                    ['extra thickness in lintel beam',2,10.5+1.8*2+.5,0.1],
                                    ['bottoms of door1',2,1.2,0.25],
                                   
                                    ['windows',4,0.9,0.25]
                                    ])
    lintel_centering.rate =195.11
    lintel_centering.vArea()
    print('\n\tProvisional cost towards Display Board and photograph = ','\u20B9{:.2f}'.format(5000),'\n')
    print('\t\t\t\tCess for welfare of labourers','= \u20B9{:.2f}'.format(5000),'\n')
    print('-'*80)
    print('Total estimated cost = \u20B9618168.00\nLimited to \u20B9500000.00')
    
    print('-'*80)
    fl.signature(500000, 'Five lakh only ', 2, '')
    
    
    
    
    
    
    