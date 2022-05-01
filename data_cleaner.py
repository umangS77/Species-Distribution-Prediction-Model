import pandas as pd
import numpy as np
import json
import csv


gridList = []

class Single_Grid:
    def __init__(
        self,
        latitude,
        longitude,
        # species_count,
        # lifeForm_count,
        # vegetation_count,
        number_of_species,
        number_of_lifeForms,
        number_of_vegetations,
    ):
        self.latitude = latitude
        self.longitude = longitude
        # self.species_count = species_count
        # self.lifeForm_count = lifeForm_count
        # self.vegetation_count = vegetation_count
        self.number_of_species = number_of_species
        self.number_of_lifeForms = number_of_lifeForms
        self.number_of_vegetations = number_of_vegetations


def grid_details(
    lat,
    lon,
    # species_count,
    # lifeForm_count,
    # vegetation_count,
    number_of_species,
    number_of_lifeForms,
    number_of_vegetations,
):
    # print(number_of_vegetations, number_of_species, number_of_lifeForms)
    gg = Single_Grid(
        latitude=lat,
        longitude=lon,
        # species_count=species_count,
        # lifeForm_count=lifeForm_count,
        # vegetation_count=vegetation_count,
        number_of_species=number_of_species,
        number_of_lifeForms=number_of_lifeForms,
        number_of_vegetations=number_of_vegetations,
    )
    gridList.append(gg)

    # print(gg.latitude)


df = pd.read_csv(r"sheet3.csv")
df = df.drop(["ID", "False_ID", "No_of_Indi"], axis=1)
df = df.round({"LAT": 7, "LON": 7}) # set number of decimal digits 
df = df.sort_values(by=["LAT", "LON"], ascending=True)


################################

# get all unique longitues and longitudes

unique_longitudes = df.LON.unique()
unique_latitudes = df.LAT.unique()


final_output = []

for lon in unique_longitudes:
    for lat in unique_latitudes:
        try:
        # for i in range(1):
            grouped1 = df.groupby("LON")
            grouped1 = grouped1.get_group(lon)
            grouped2 = grouped1.groupby("LAT")
            grouped2 = grouped2.get_group(lat)

            single_grid = grouped2

            # print(single_grid)

            #####################

            # Life form

            types_of_lifeForm = single_grid.Life_Form.unique()
            lifeForm_count = {}

            for item in types_of_lifeForm:
                lifeForm_count[item] = 0

            for index, row in single_grid.iterrows():
                n = row["Life_Form"]
                lifeForm_count[n] += 1

            # print(lifeForm_count)

            #######################################

            # Vegetation

            types_of_vegetation = single_grid.Vegetation.unique()

            vegetation_count = {}

            for item in types_of_vegetation:
                vegetation_count[item] = 0

            for index, row in single_grid.iterrows():
                n = row["Vegetation"]
                vegetation_count[n] += 1

            # print(vegetation_count)

            #############################################

            # Species

            types_of_species = single_grid.Species_Na.unique()

            species_count = {}

            for item in types_of_species:
                species_count[item] = 0

            for index, row in single_grid.iterrows():
                n = row["Species_Na"]
                species_count[n] += 1

            # print(species_count)

            ############################################

            species_size = len(species_count)
            lifeForm_size = len(lifeForm_count)
            vegetation_size = len(vegetation_count)

            # print(species_size)

            grid_details(
                lat,
                lon,
                # species_count,
                # lifeForm_count,
                # vegetation_count,
                species_size,
                lifeForm_size,
                vegetation_size,
            )

            tempout = []

            tempout.append(lat)
            tempout.append(lon)
            tempout.append(species_size)
            tempout.append(lifeForm_size)
            tempout.append(vegetation_size)


            # print(lat, lon, species_size, lifeForm_size, vegetation)
            final_output.append(tempout)
            



        except:
            pass


def obj_dict(obj):
    return obj.__dict__


# json_string = json.dumps(gridList, default=obj_dict, indent=2)

# print(json_string)

# with open("json_data.json", "w") as outfile:
#     outfile.write(json_string)

# print('final output = ')
# print(final_output)

with open('finalData.csv', 'w') as csvfile: 
    write = csv.writer(csvfile) 
    write.writerow(['latitude', 'longitude', 'count of species', 'count of life form', 'count of vegetation'])
    for row in final_output:
        write.writerow(row)

# with open('finalData.csv', 'w') as f:
#     for key in gridList.keys():
#         f.write("%s,%s\n"%(key,gridList[key]))

