#Aircraft Locating code
import csv
import math


#Aircraft location object. initialize with device location. Contains calc function.
class Aircraft_loc:
    def __init__(self,sys_alt,sys_lat,sys_lon):
        self.sys_alt = float(sys_alt)
        self.sys_lat = float(sys_lat)
        self.sys_lon = float(sys_lon)

    #calculates aircraft location vector.
    #Input: Aircraft_in object
    #Output: Aircraft_out object
    def calc_loc(self, craft):
        earth_R = 6371000 #radius of earth in meters

        #latitude in rads and difference
        sLat = math.radians(self.sys_lat)
        cLat = math.radians(craft.lat)
        dLat = cLat - sLat

        #longitude in rads and difference
        sLon = math.radians(self.sys_lon)
        cLon = math.radians(craft.lon)
        dLon = cLon - sLon

        #using haversine formula to calculate distance
        hav = math.sin(dLat/2)*math.sin(dLat/2)
        cchav = math.cos(sLat)*math.cos(cLat)*math.sin(dLon/2)*math.sin(dLon/2)
        dist = 2*earth_R*math.asin( math.sqrt(hav +cchav))

        #difference of altitude in meters
        dAlt = craft.alt - self.sys_alt 

        #vertical angle of aircraft in degrees
        v_angle = math.degrees(math.atan(dAlt/dist))

        #calculations for azimuth
        az_n = math.sin(dLon)
        az_d = math.cos(sLat)*math.tan(cLat) - math.sin(sLat)*math.cos(dLon)
        azimuth = math.degrees(math.atan(az_n/az_d))

        #returns both values in degrees
        out = Aircraft_out(craft.idn, v_angle, azimuth)
        return out


#object that contains Aircraft id number and alt,lat,long for calculations
class Aircraft_in:
    def __init__(self,idn,alt,lat,lon):
        self.idn  = int(idn)
        self.alt  = float(alt)
        self.lat  = float(lat)
        self.lon  = float(lon)

#object that contains calculated vertical angle and azimuth
class Aircraft_out:
    def __init__(self,idn,angle,azimuth):
        self.idn     = int(idn)
        self.angle   = float(angle)
        self.azimuth = float(azimuth)



#test code starts here
y = Aircraft_loc(40,44.565298,-123.276417)
x = Aircraft_in(1,5000,44.615678, -123.379140)
z = y.calc_loc(x)
print(z.azimuth)
print(z.angle)

'''with open('aircraft_data.csv', "r+") as data:
    reader = csv.reader(data)
    with open('aircraft_data.csv', "r+") as data:
        writer = csv.writer(data)
        for row in reader:
            if row[0] <> 'id':
                if row[4] <> '':
                    writer.writerow(row)
                else:
                    x = Aircraft_in(row[0],row[1],row[2],row[3])
                    z = calc_loc(x,y)
                    wrow = [row[0], row[1], row[2], row[3], z.angle, z.azimuth]
                    writer.writerow(wrow)
            else:
                writer.writerow(row)

'''



