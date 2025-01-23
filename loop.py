list_of_clouds = ["aws", "azure", "gcp"]
print(list_of_clouds)

list_of_clouds.append("linode")
list_of_clouds.insert(0, "digital ocean")
print(list_of_clouds)
print(len(list_of_clouds))

for cloud in list_of_clouds:
    print(" ")
    print(cloud)

counter = 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1
print("Loop finished!")
 

