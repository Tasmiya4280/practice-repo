list_of_clouds= ["aws", "azure", "gcp"]
print(list_of_clouds)

list_of_clouds.append("linode")
list_of_clouds.insert(0 ,"digital ocean")
print(list_of_clouds)
print (len(list_of_clouds))

for cloud in list_of_clouds:
 print(" ")
 print(cloud)
for i in range(1,5):
 print(list_of_clouds)