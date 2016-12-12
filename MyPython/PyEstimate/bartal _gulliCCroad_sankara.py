
import items as it
import ClassLibrary as cl
import FunctionLibrary as fl









if __name__ == "__main__":
    print ('Name of the Work:- Construction of cement concrete roadat Sankara Bartal Gully' )
    print('Estimated Cost:-Rs.1,00,000.00','\t\t','Head of Account:T.F.C.(15-16)' )
    print('-'*85)
    print(it.items['CC(1:2:4)'])
    road =cl.Quantity([['road',1,41.76,2.5,0.19]])
    road.rate=4760.71
    road.volume()
    print('Cess for labour welfare = Rs. 1,000.00\n')
    print('Work contingency = Rs. 1,000.00\n')
    print('Display Board and photograph = Rs.500.00\n')
    print('_'*85)
    print('Total estimated cost is limited to Rs.1,00,000.00\n')
    fl.signature(100000, 'Rupees one lakh only', 3, 'Sankara G.P.')
    
    
    