from os import write
import requests
import time

url = "https://www.floatrates.com/daily/usd.json"

# 1. Create the file and write the "Headers" (Column Names)
# "w" mode = Write (Creates a new file or overwrites existing one)

with open ("fx_data.csv", 'w') as f:
  f.write ("rate,converstionprice\n")
print("File 'fx_data.csv' created successfully.")

while True:
  try:
    r = requests.get(url)
    data= r.json()
    gbprate = data["gbp"]["rate"] 
    converstion = data["gbp"]["inverseRate"]
    if converstion < 0.78:
      print (f"Convertion has reduced £ ",{converstion})
    else:
      print (f"Convertion more than 0.78. Current rate- ",{converstion})
      
    with open ("fx_data.csv", "a" ) as f:
    # We separate values with commas (CSV = Comma Separated Values)
      f.write (f"{rate},{converstion}\n" )

  except exception as e:
    print(f"Error: {e}")
  time.sleep (5)