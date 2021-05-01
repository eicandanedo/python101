import csv
#open the csv file. Ensure it is saved in same location as py file
census = csv.reader(open("census.csv"))

#creating empty dictionary (d)
d={}

#adding each country to dictionary. Country is key, Continent is value pair
for country in census:
    d[country[0]]=country[2]

req_name = None


while req_name != 'quit':
    # Ask user to enter country name and output the value pair 
    req_name = input("\nEnter a country or type 'quit': ")
    if req_name in d.keys():
        print(d.get(req_name))
    else:
        # Handle misspellings, and words not yet stored.
        print("\n  Sorry, this country was not in the 2007 census file.")
