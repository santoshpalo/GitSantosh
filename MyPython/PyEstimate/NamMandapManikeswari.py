import ClassLibrary as cl
import FunctionLibrary as fl
import items as it










if __name__ == "__main__":
    print(it.items['efhs'])
    foundation_excavation = cl.Quantity([['foundation trenches',16,1.5,1.5,1.2],
                                         ['walls',1,32.8-12*1.5+.94,0.6,0.6],
                                         ['inside mandap',4,2.7-1.5,0.6,.6]])
    foundation_excavation.rate =100
    foundation_excavation.volume()
    print(it.items['CC(1:4:8)'])
    metal_concrete = cl.Quantity([['columns',16,1.5,1.5,0.1],
                                  ['walls',1,32.8-12*.38+.94,0.6,0.09],
                                  ['inside mandap',4,2.7-0.38-.19,0.6,0.09]])
    metal_concrete.rate = 100
    metal_concrete.volume()
    print(it.items['rcc'])
    rcc_work = cl.Quantity([['footings',16,1.2,1.2,0.23],
                             ['columns1',12,0.38,0.38,1.40],
                             ['columns2',4,0.38,0.38,1.95]])
    rcc_work.rate
    rcc_work.volume()
    
    print(it.items['bmfp'])
    brick_foundation = cl.Quantity([['circular mandap',1,32.8-12*0.38+.94,0.38,0.55],
                                    ['inside mandap',4,2.7-.38,0.38,0.57]])
    brick_foundation.rate = 100
    brick_foundation.volume()
    reinforcement1=cl.Quantity([['column footings',16*2*9,1.12,0.62],
                                ['outside columns',12*5,4.5,0.89],
                                ['internal columns',4*4,5.7,1.58],
                                ['stirrups',181+64-46,0.87,0.395]])
    reinforcement1.rate = 100
    reinforcement1.reinforcement()
    print(it.items['rscs_plinth'])
    plinth_centering=cl.Quantity([['footing sides',16*4,1.2,0.23]])
    plinth_centering.rate = 100
    plinth_centering.vArea()
    column_centering = cl.Quantity([['columns',16*4,0.38,0.85]])
    column_centering.rate = 100
    column_centering.vArea()
    
    
    
    
    
    