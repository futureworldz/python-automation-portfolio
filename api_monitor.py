
# 1. IMPORTING TOOLS
import requests  # For talking to the internet
import time      # For waiting/sleeping
from datetime import datetime # For timestamps

# 2. THE INFINITE LOOP (The Robot Brain)
while True:
    # Code inside here runs forever
    print("I am running...")
    
    # 3. GETTING DATA FROM AN API
    # 'r' is the box (Response Object)
    # 'r.status_code' is the number (200 = Good, 404 = Missing, 500 = Broken)
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        
        # 4. MAKING DECISIONS (Logic)
        if r.status_code == 200:
            print("Success!")
        else:
            print("Failed!")
            
    # 5. CATCHING CRASHES (Safety Net)
    except Exception as e:
        print(f"Internet is down: {e}")

    # 6. WAITING
    time.sleep(5) # Wait 5 seconds