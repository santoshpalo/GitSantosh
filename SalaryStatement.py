import pandas as pd
pd.set_option('display.width',500)

C = ['Name of J.E.','Period','Pay','GP','DA','HRA']

data = [['N. Suryanarayan','Oct-2013 to 19-08-2015',339961,94974,458624,0],
        ['K.N. Choudhury','Feb-2015 to 19-08-2015',15270*2+15860*4+9721,4200*6+2574,22001*2+22668*3+23871+14631,974*2+1003*4+615],
        ['S.N.Bhattaray','Feb-2015 to 19-08-2015',15270*2+15860*4+9721,4200*6+2574,22001*2+22668*3+23871+14631,0.0],
        ['Santosh Palo','Feb-2015 to 19-08-2015',16020*2+16630*4+10193,4200*6+2574,22849*2+23538*3+24788+15193,0.00],
        ['Swadhin Dash','Feb-2015 to 19-08-2015',15650*3+16250*3+9960,4200*6+2574,22431*3+23109*2+24336+14915,993*3+1023*3+627],
        ['Kailash Meher','Feb-2015 to 19-08-2015',15270*3+16250*3+9960,4200*6+2574,22001*3+23109*2+24236+14915,974*3+1023*3+627],
        ['R.N. Panda','Feb-2015 to 19-08-2015',15650*6+9592,4200*6+2574,22431*5+23622+14478,993*7+608+9*964],
        ['D.K. Muni','Feb-2015 to 19-08-2015',16740*6+10260,4200*6+2574,23662*5+24919+15272,0],
        ['Bijay Purty','Feb-2015 to 19-08-2015',15270*4+15860*2+9721,4200*6+2574,22001*4+22668+23871+14631,0],
        ['Md. Ahmed Sariff','Feb-2015 to 19-08-2015',15270*2+15890*4+9721,4200*6+2574,22001*2+22668*3+23871+14631,0]]
table = pd.DataFrame(data,columns = C, index = range(1,len(data)+1,1))
table['TOTAL']=table['Pay']+table['GP']+table['DA']+table['HRA']
G_Total = table['TOTAL'].sum()
table['Pay']=table['Pay'].map('Rs.{:.2f}'.format)
table['GP']=table['GP'].map('Rs.{:.2f}'.format)
table['DA']=table['DA'].map('Rs.{:.2f}'.format)
table['HRA']=table['HRA'].map('Rs.{:.2f}'.format)

table['TOTAL']=table['TOTAL'].map('Rs.{:.2f}'.format)

print (table,'\n\n','Amount needed for arrear salary = Rs. 34,96,378.00','\n','Amount needed for E.P.F. payment = Rs. 2,42,018.00','\nGrand Total of Arrear Salary =','Rs.{:.2f}'.format(G_Total+242018),'\n','(Thirty seven lakh thirty eight thousand three hundred ninty six only)')
print('\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tProject Director')
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t      D.R.D.A. , Subarnapur')




