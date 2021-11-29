import pandas as pd
import random


addr = ['212 Sunnyslope St. Lockport, NY 14094',
'7 Big Rock Cove St. Staten Island, NY 10314',
'290 Fairfield St. Patchogue, NY 11772',
'7075 Young Ave. Brooklyn, NY 11220',
'7674 Colonial Street New York, NY 10128',
'56 Brickyard Ave. New York, NY 10023',
'10 East Canterbury St. Levittown, NY 11756',
'552 Birchwood Ave. Lindenhurst, NY 11757',
'408 Ocean Ave. Bronx, NY 10451',
'36 Prospect Ave. Astoria, NY 11106',
'582 Woodside St. Bronx, NY 10457',
'437 Prince Avenue Spring Valley, NY 10977',
'7450 Cobblestone Road Far Rockaway, NY 11691',
'7732 East Plymouth Street Brooklyn, NY 11201',
'61 Fairview Street Flushing, NY 11355',
'741 Stonybrook Ave. Endicott, NY 13760',
'80 Rockaway St. Brooklyn, NY 11203',
'9285 Gainsway St. Bronx, NY 10453',
'7887 Border Avenue Brooklyn, NY 11234',
'489 W. Ocean Dr. Yonkers, NY 10701',
'319 River Ave. Fairport, NY 14450',
'9057 Thompson Avenue Astoria, NY 11105',
'147 2nd Lane New York, NY 10028',
'5 Queen Ave. Brooklyn, NY 11215',
'934 Henry Smith Street Elmont, NY 11003',
'28 Dogwood Lane Hempstead, NY 11550',
'7924 Garfield Street New York, NY 10024',
'41 Honey Creek Court West Babylon, NY 11704',
'332C Peninsula Ave. Brooklyn, NY 11235',
'701 Berkshire Lane Buffalo, NY 14215',
'9212 Hartford Ave. Bronx, NY 10473',
'764 Plymouth St. Brooklyn, NY 11224',
'2 Vernon Drive Brooklyn, NY 11208',
'64 Constitution Street New York, NY 10029',
'757 Bayberry Ave. Brooklyn, NY 11207',
'2 E. Inverness Lane Astoria, NY 11103',
'9474 NW. Delaware St. Brooklyn, NY 11236',
'84 Bishop Drive Brooklyn, NY 11211',
'98 Middle River St. Brentwood, NY 11717',
'455 Walt Whitman Dr. Bronx, NY 10456',
'7153 Leeton Ridge Street Brooklyn, NY 11225',
'8150 53rd Rd. Ithaca, NY 14850',
'33 Bear Hill St. East Elmhurst, NY 11370',
'152 Richardson Circle Huntington Station, NY 11746',
'611 Liberty Ave. Bronx, NY 10461',
'7982 Somerset Street Brooklyn, NY 11210',
'8922 Vine St. New York, NY 10040',
'40 Myers Rd. Brooklyn, NY 11219',
'49 Hilltop Drive Staten Island, NY 10312',
'8579 Johnson Lane Bronx, NY 10460',
'75 South Wentworth Rd. Rochester, NY 14609',
'7243 Trout Street Flushing, NY 11354',
'5 South Ave. New York, NY 10027',
'946 Manchester Lane Bronx, NY 10467',
'885 Cooper Drive Jamestown, NY 14701',
'8063 Lincoln Ave. New York, NY 10034',
'36 North Thompson Rd. Brooklyn, NY 11206',
'881 8th Ave. New York, NY 10016',
'7 New Saddle Rd. Brooklyn, NY 11209',
'7793 Edgewater Drive Brooklyn, NY 11216',
'7658 Newport Road Huntington, NY 11743',
'8823 Fairway St. South Richmond Hill, NY 11419',
'8813 Briarwood Dr. North Tonawanda, NY 14120',
'473 Trusel Drive Jamaica, NY 11435',
'24 Randall Mill Street Brooklyn, NY 11233',
'93 Trusel St. Webster, NY 14580',
'47 East Linden Court Brooklyn, NY 11238',
'23 North Bowman Dr. Jamaica, NY 11432',
'92 Alderwood Ave. Bronx, NY 10472',
'237 Cedarwood St. South Ozone Park, NY 11420',
'295 Beach St. Bronx, NY 10452',
'481 E. High Ridge Court Bay Shore, NY 11706',
'82 N. Brookside Rd. Bronx, NY 10462',
'76 Wagon Road Jamaica, NY 11434',
'34 Ann Avenue New York, NY 10033',
'39 Maiden Drive Brooklyn, NY 11221',
'896 Church Ave. New York, NY 10003',
'410 Buckingham Street Jackson Heights, NY 11372',
'123 Ridgewood St. Bronx, NY 10468',
'698 Lakewood Dr. Brooklyn, NY 11229',
'792 Del Monte Ave. Bronx, NY 10466',
'8489 New Saddle St. Brooklyn, NY 11230',
'7831 Tallwood St. Tonawanda, NY 14150',
'7609 Annadale St. New York, NY 10011',
'78 Bellevue Ave. Buffalo, NY 14224',
'395 W. Beaver Ridge Ave. Bronx, NY 10458',
'8448 North Strawberry St. Fresh Meadows, NY 11365',
'9315 Oklahoma Court Buffalo, NY 14221',
'7488 Forest St. Poughkeepsie, NY 12603',
'292 Edgemont Street Brooklyn, NY 11212',
'66 N. Homewood Dr. New York, NY 10002',
'7581 State Dr. Massapequa, NY 11758',
'702 Old Rocky River Dr. Brooklyn, NY 11228',
'7 Randall Mill Ave. New York, NY 10025',
'278 Warren St. Brooklyn, NY 11223',
'9066 Wild Horse St. Woodside, NY 11377',
'434 Glenridge Road Westbury, NY 11590',
'7873 Goldfield St. Staten Island, NY 10306',
'7038 Buckingham Dr. Forest Hills, NY 11375',
'10 Pilgrim Ave. Brooklyn, NY 11204',
'35 West Lane New York, NY 10009',
'8872 Prospect Lane Bronx, NY 10469',
'66 SE. Amerige Street Troy, NY 12180',
'9939 Amerige Court Brooklyn, NY 11214',
'863 S. Hall Court Rego Park, NY 11374',
'884 W. Cherry Ave. Bronx, NY 10463',
'7400 South Lakeview Lane Bronx, NY 10465',
'78 Briarwood Court Freeport, NY 11520',
'736 Winding Way Drive Poughkeepsie, NY 12601',
'251 Wrangler St. Hamburg, NY 14075',
'16 Galvin St. Brooklyn, NY 11218',
'220 Linda St. Brooklyn, NY 11213',
'5 Hickory St. Corona, NY 11368',
'86 Water Drive Newburgh, NY 12550',
'8510 South Lane Auburn, NY 13021',
'8691 W. Harvey Rd. Rome, NY 13440',
'54 Wakehurst Lane Middletown, NY 10940',
'51 Lafayette Drive New York, NY 10031',
'406 Cottage Drive New York, NY 10032',
'349 Sycamore Dr. Ridgewood, NY 11385',
'84 Pine Road Brooklyn, NY 11237']


gender = ['Male', 'Female', 'Non-binary']

df = pd.read_csv('user_data.csv')
df = df.sample(100)
df['address'] = [' '.join(i.split()[:-2])[:-1] for i in addr[:100]]
df['zip_code'] = [i.split()[-1] for i in addr[:100]]
df['gender'] = [random.choice(gender) for i in range(100)]
df['age'] = [random.randint(18,50) for i in range(100)]
print(df)

df = df.rename(columns={'id': 'USER_ID'})
df.reset_index(drop=True, inplace=True)
df.to_csv('user_data_personalize.csv', index = True)