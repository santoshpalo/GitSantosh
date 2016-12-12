import pandas as pd
import math as mt
class Quantity(object):
    def __init__(self,data,rate = 0,volumeC= ['description','no','length','breadth','height'],
                 vAreaC = ['description','no','length','height'],hAreaC = ['description','no','length','breadth'],
                 tclC = ['description','no','length'],reinforcementC = ['description','no','length','coefficient']):
        self.data = data
        self.volumeC = volumeC
        self.vAreaC = vAreaC
        self.hAreaC = hAreaC
        self.tclC= tclC
        self.reinforcementC= reinforcementC
        self.rate = rate
        
    def volume(self):
        table = pd.DataFrame(self.data,columns=self.volumeC,index = range(1,len(self.data)+1))
        table['Volume']=(table['no']*table['length']*table['breadth']*table['height']).round(2)
        total_volume = table['Volume'].sum()
        table['length']=table['length'].map('{:.2f}m'.format)
        table['breadth']=table['breadth'].map('{:.2f}m'.format)
        table['height']=table['height'].map('{:.2f}m'.format)
        table['Volume']=table['Volume'].map('{:.2f}cum'.format)
        
        print (table,'\n\t\t\t\t\t',
                '{:.2f}cum'.format(total_volume),'@ \u20B9{:.2f}/cum'.format(self.rate),'= \u20B9{:.2f}'.format(round(total_volume*self.rate)))
    def vArea(self):
        table = pd.DataFrame(self.data,columns=self.vAreaC,index = range(1,len(self.data)+1))
        table['Area']=(table['no']*table['length']*table['height']).round(2)
        total_volume = table['Area'].sum()
        table['length']=table['length'].map('{:.2f}m'.format)
        
        table['height']=table['height'].map('{:.2f}m'.format)
        table['Area']=table['Area'].map('{:.2f}sqm'.format)
        
        print (table,'\n\t\t\t\t\t',
                '{:.2f}sqm'.format(total_volume),'@ \u20B9{:.2f}/sqm'.format(self.rate),'= \u20B9{:.2f}'.format(round(total_volume*self.rate)))
    def hArea(self):
        table = pd.DataFrame(self.data,columns=self.hAreaC,index = range(1,len(self.data)+1))
        table['Area']=(table['no']*table['length']*table['breadth']).round(2)
        total_volume = table['Area'].sum()
        table['length']=table['length'].map('{:.2f}m'.format)
        
        table['breadth']=table['breadth'].map('{:.2f}m'.format)
        table['Area']=table['Area'].map('{:.2f}sqm'.format)
        
        print (table,'\n\t\t\t\t\t',
                '{:.2f}sqm'.format(total_volume),'@ \u20B9{:.2f}/sqm'.format(self.rate),'= \u20B9{:.2f}'.format(round(total_volume*self.rate)))
    def tcl(self):
        table = pd.DataFrame(self.data,columns=self.tclC,index = range(1,len(self.data)+1))
        table['total']=(table['no']*table['length']).round(2)
        total_centre_line = table['total'].sum()
        table['length']=table['length'].map('{:.2f}m'.format)
        
        
        table['total']=table['total'].map('{:.2f}m'.format)
        
        print (table,'\nTotal cente line length of the building =',
                '{:.2f}m'.format(total_centre_line))
    def reinforcement(self):
        table = pd.DataFrame(self.data,columns=self.reinforcementC,index = range(1,len(self.data)+1))
        table['total']=(table['no']*table['length']).round(2)
        table['weight']=(table['no']*table['length']*table['coefficient']).round(2)    
        total_weight = table['weight'].sum()
        table['length']=table['length'].map('{:.2f}m'.format)
        table['weight']=table['weight'].map('{:.2f}kg'.format)        
        table['total']=table['total'].map('{:.2f}m'.format)        
        print (table,'\n\t\t\t\t\t',
                '{:.2f}kg'.format(round(total_weight)))
    def ms_door_window(self):
        table = pd.DataFrame(self.data,columns=self.vAreaC,index = range(1,len(self.data)+1))
        table['weight']=(table['no']*table['length']*table['height']*40.35).round(2)
        total_weight = table['weight'].sum()
        table['length']=table['length'].map('{:.2f}m'.format)
        
        table['height']=table['height'].map('{:.2f}m'.format)
        table['weight']=table['weight'].map('{:.2f}kg'.format)
        
        print (table,'\n\t\t\t\t\t',
                '{:.2f}kg'.format(total_weight),'@ \u20B9{:.2f}/kg'.format(self.rate),'= \u20B9{:.2f}'.format(round(total_weight*self.rate)))
    
        
    
        
class reinforcement(object):
    def __init__(self,span = [],end_support_condition = [],trans_span_length = [],spacing_of_bars=[]):
        self.span= span
        self.end_support_condition = end_support_condition
        self.trans_span_length = trans_span_length
        self.spacing_of_bars =spacing_of_bars
    def main_bottom_1(self):
        def coefficient(self):
            return list(0.25 if x == 1 else 0.143 for x in self.end_support_condition )
        def effective_span(self):
            return self.span[0]-sum([round(self.span[0]*a) for a in coefficient(self)[:2]]),self.span[1]-sum([round(self.span[1]*a) for a in coefficient(self)[2:4]])
        def no_of_bars(self):
            return list(mt.ceil(a/b) for a,b in zip(effective_span(self),self.spacing_of_bars))
        def length_of_bars(self):
            return list(round(self.span[0]+0.5+0.15+y/4) if z == 1 else round(self.span[0]+0.5+0.15+0.15)  for y,z in zip(self.trans_span_length[:2],self.end_support_condition[:2]))+(
                        list(round(self.span[1]+0.5+0.15+y/4) if z == 1 else round(self.span[1]+0.5+0.15+0.15)  for y,z in zip(self.trans_span_length[2:4],self.end_support_condition[2:4])))
            
        
        print (coefficient(self),effective_span(self),no_of_bars(self),length_of_bars(self))









if __name__ == "__main__":
    x = reinforcement()
    x.span =[5.2,3.5]
    x.end_support_condition=[0,1,1]
    x.spacing_of_bars=[0.15,0.18]
    x.trans_span_length = [0.5,0.5]
    x.main_bottom_1()
    
    
    
    
    