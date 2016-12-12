import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it







if __name__ == "__main__":
    print('Name of the Woprk:- Grade I metalling of the road from Bhikabahali to Sakma')
    print('Estimated Cost:-\u20B94,00,000.00\tHead of Account:- Biju K.B.K.(2014-15)')
    print('-'*80)
    print(it.items['subbase'])
    subbasemoorum = cl.Quantity([['sub-base of the road',1,100,3.65,0.15]])
    subbasemoorum.rate = 177.48
    subbasemoorum.volume()
    print(it.items['gradeI'])
    gradeImetalling = cl.Quantity([['GradeI metalling',1,100,3.65,0.1]])
    gradeImetalling.rate =290.76
    gradeImetalling.volume()
    print(it.items['moorumcollection'])
    subbasemoorum = cl.Quantity([['sub-base of the road',1,100,3.65,0.15]])
    subbasemoorum.rate = 233.9
    subbasemoorum.volume()
    print(it.items['metalcollection'])
    gradeImetalling = cl.Quantity([['GradeI metalling',1,100,3.65,0.1]])
    gradeImetalling.rate =936.3
    gradeImetalling.volume()
    
    