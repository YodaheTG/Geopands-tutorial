from sys import exit
from math import sqrt
from rtree import index
from geopandas import read_file
from matplotlib.pyplot import subplots, savefig

eth_regions  = read_file("......./ethiopiaregion/Eth_Region_2013.shp")
#print (eth_regions)



idx = index.Index()

for id,idb in eth_regions.iterrows():
	idx.insert(id, idb.geometry.bounds)
    

for i in range (0,10):
	#print (regionb.geometry.iloc[i])    
	a = eth_regions.geometry.iloc[i]
	for x in range (0,10):
    	if a != eth_regions.geometry[x]:
       	possible_matches = eth_regions.iloc[list(idx.intersection(a.bounds))]
       	print (possible_matches)