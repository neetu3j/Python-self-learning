list_of_cloud= ['aws', 'azure', 'gcp', 'ibm', 'oracle']
cloud= "gcp"
print(list_of_cloud)


#add a new cloud to the list
#add a new cloud selesforce
list_of_cloud.append("salesforce")

#add a new cloud oracale
list_of_cloud.append("oracle")

print(list_of_cloud)

list_of_cloud.insert(2, "alibaba")
print(list_of_cloud)
print(len(list_of_cloud))

#insert "Hello cloud" to 0th index of list

list_of_cloud.insert(0,"Hello cloud")
print(list_of_cloud)

