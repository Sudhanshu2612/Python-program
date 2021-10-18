# Free APi  which predicts the   nationality  from  the name we entered 
# Nationalize.io predicts the nationality of a person given their name. 
# THa Use of  the API is  for analytics, ad segmenting, demographic statistics etc.

#This is the link of the official website of the API https://nationalize.io/
#All responses are in "content-type: application/json; charset=utf-8".
# They have also provide us with some error handling methods which we can use in order to print the errors if we 
#receive any .

# The API is free until 1000 requests and require kay later if requests are more than 100
# In this APi we can check names upto 10 at a time by passing an array in the arguments 



#Here is the connection to the API and some test cases
import requests

print("Please enter name to find the country is belongs to ")
name = input()

try:
    response  = requests.get("https://api.nationalize.io?name={}".format(name))
except:
    print(error)
ans = response.json()
print("Name : {}\n".format(ans["name"]))
for country in ans["country"]:
    print("Country : {} , Probability : {}".format(country["country_id"],country["probability"]))