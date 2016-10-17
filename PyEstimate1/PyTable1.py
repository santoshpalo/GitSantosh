from tables  import *
class Particle(IsDescription):
    name = StringCol(16)
    idnumber = Int64Col()
    ADCcount = UInt16Col()
    TDCcount = UInt8Col()
    grid_i = Int32Col()
    grid_j = Int32Col()
    pressure = Float32Col()
    energy = Float32Col()
h5file = open_file("tutorial1.h5", mode = "w", title = "Test file")
group = h5file.create_group("/", 'detector', 'Detector information')
table = h5file.create_table(group, 'readout', Particle, "Readout example")
print(h5file)
h5file
particle = table.row
for i in range(10):
    particle['name'] = 'Particle:%6d' % (i)
    particle['TDCcount'] = i % 256
    particle['ADCcount'] = (i*256) % (1<<16)
    particle['grid_i'] = i
    particle['grid_j'] = 10-i
    particle['pressure'] = float(i*i)
    particle['energy']= float(particle['pressure']**4)
    particle['idnumber']= i*(2**34)
    particle.append()
table.flush()
table = h5file.root.detector.readout
pressure = [x['pressure'] for x in table.iterrows() if x['TDCcount'] > 3 and 20 <= x['pressure'] < 50]
print(pressure)
names = [ x['name'] for x in table.where("""(TDCcount > 3) & (20 <= pressure) & (pressure < 50)""") ]
print(names)
condition = '(name == b"Particle:      5") | (name == b"Particle:      7")'
for record in table.where(condition): 
    gcolumns = h5file.create_group(h5file.root, "columns", "Pressure and Name")
    h5file.create_array(gcolumns, 'pressure', array(pressure), "Pressure column selection")
print(h5file)
h5file.close()


    
    
