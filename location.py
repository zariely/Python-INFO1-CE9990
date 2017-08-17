"""
location.py
creates module Location
"""

import sys, urllib.request, json

class Location(object):

    def __init__(self, lat, lng):
        if not isinstance(lat, int) or isinstance(lat, float):
            raise TypeError('Latitude must be an integer, not {}.'.format(str(type(lat))))
        if not isinstance(lng, int) or isinstance(lng, float):
            raise TypeError('Longitude must be an integer, not {}.'.format(str(type(lng))))

        if lat > 90 or lat < -90:
            raise ValueError('Latitude must be between -90 and 90.')
        if lng > 180 or lng < -180:
            raise ValueError('Longitude must be between -180 and 180.')

        self.lat = lat
        self.lng = lng


    def __str__(self):
        """Return a string that looks like the contents of myself"""
        dg = '\u00b0'
        print(dg)

        ns = ('N' if self.lat >= 0 else 'S')
        ew = ('E' if self.lng >=0 else 'W')

        return "{}{} {}, {}{} {}".format(self.lat, dg, ns, self.lng, dg, ew)


    def getLatitude(self):
        """Returns latitude"""
        return self.lat

    def getLongitude(self):
        """Returns longitude"""
        return self.lng

    def setLatitude(self):
        """Sets the latitude"""
        self.lat = lat
        return self.lat

    def setLongitude(self):
        """Sets longitude"""
        self.lng = lng
        return self.lng



    def getZipcode(self):
        """returns zip based on given latitude & longitude"""
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(lat,lng)

        file = urllib.request.urlopen(url).read()
        data = json.loads(file)

        results = data['results']
        if len(results) == 0:
            return 0

        firstResult = results[0]
        adxCmpnt = firstResult['address_components']

        for cmpnt in adxCmpnt:
            if 'postal_code' in cmpnt['types']:
                return int(cmpnt['long_name'])
        return 0


if __name__ == '__main__':
    import sys, urllib.request, json

    #latitude and longitude of brooklyn ny
    lat = 40.6782
    lng = 73.9442

    loc = Location(lat, lng)

    print("The coordinates of {} are {}, {}.".format(loc, loc.getLatitude, loc.getLongitude))
    print("The ZIPcode of {} is {}.".format(loc, loc.getZipcode))
