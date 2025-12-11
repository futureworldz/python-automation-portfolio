import requests
url="https://jsonplaceholder.typicode.com/todos/1"
print ("Attemptiong to connect to "+ url )
r = requests.get(url)
print ("just to see whats in the response : "+ str(r.text))

#str is required to convert the data to a string so that it can be printed
print("Status:"+str(r.status_code))

#to convert data to json dictionary
data = r.json()
print ("You grabbed a specific value by its name. This is how you will eventually map 'Source Data' to 'Target Data' in your real job." + str (data))

#important dictonary should be in square brackets
task_titles = data["title"]
task_completed = data ["completed"]

print ("Title: " + str(task_titles))
print ("completed: " + str(task_completed))



