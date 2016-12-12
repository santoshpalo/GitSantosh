import FunctionLibrary as fl
EC = 'Rs.{:.2f}'.format(300000)
ECT = '(Three lakh only)'
NW ='''Construction opf C.C. road from Sankara Medical Road to Harijan Sahi
Road near Play Field, Sankara'''
HA = 'Maintenance of Road and Bridge'
text = '''\n\tThis road leading from Medical road to Harijan sahi near play ground
needs to be raised upto a height of 0.50m above N.G.L..Hence the cut-off wall
width and height has to be raised.An R.C.C. hume pipe culvert has to be
constructed as c.d. work.'''
middle = '''\n\tThis estimate has been prepared based on Analysis of Rates 2006.
Schedule of Rates - 2014 has been taken into Account.Prevailing Labour rates
have been taken into account at framing of the estimate.'''
conclusion = '''\n\tAll works will be executed as per guidance of engineer-in-charge.'''











if __name__ == "__main__":
    

    print('\n\tThis estimate amounting to',EC,ECT)
    print('has been framed to meet the probable expenditure towards')
    print(NW,HA)
    print (text)
    print(middle)
    print(conclusion)
    print(fl.signature(0,'',0,''))
    print('bcd')


