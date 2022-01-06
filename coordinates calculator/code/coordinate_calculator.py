import pandas as pd
from haversine import haversine, Unit

#import list 1 data
list_1 = pd.read_csv('list_1.csv')

#import list 2 data
list_2 = pd.read_csv('list_2.csv')

#combine Lat and Long data into one column 
list_1['Lat/Long'] = [(row['Lat'], row['Long']) for _, row in list_1.iterrows()]
list_2['Lat/Long'] = [(row['Lat'], row['Long']) for _, row in list_2.iterrows()]

#create dataframe of list_1 and list_2 data
df = pd.merge(list_1, list_2, left_index=True, right_index=True, suffixes=('_list_1', '_list_2')).drop(['Lat_list_1', 'Long_list_1', 'Lat_list_2','Long_list_2'], axis=1)

#calculates the distance between each location in list_1 to every location in list_2 and returns the shortest distance
closest_location =  pd.DataFrame(columns=['distance_miles', 'location_1', 'location_2'])                    #creates dataframe for coordinate pairs to be appended to
for location_1 in list_1['Lat/Long']:                                                                       #loops to interate through list_1
    both_locations = pd.DataFrame(columns=['distance_miles', 'location_1', 'location_2'])                   #creates dataframe for one list_1 coordinate to be compared against every coordinate in list_2
    for location_2 in list_2['Lat/Long']:                                                                   #loops to interate through list_2
        distance = haversine(location_1, location_2, unit=Unit.MILES)                                       #uses haversine library to calculate distance between a list_1 coordinate and a list_2 coordinate
        dic = {'distance_miles': distance, 'location_1': location_1, 'location_2': location_2}              #creates dictionary of distance between list_1 and list_2 coordinates, the list_1 coordinate and the list_2 coordinate
        both_locations = both_locations.append(dic, ignore_index=True).sort_values(by='distance_miles')     #appends dictionary to both_locations dataframe as a row, then sorts values by the shortest to longest distance
        continue
    closest_location =  closest_location.append(both_locations.iloc[0]).reset_index(drop=True)              #appends first row of both_locations dataframe (the one with the shortest distance) to closest_location dataframe
