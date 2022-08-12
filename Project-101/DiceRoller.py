import random 
  
response = "y"
   
while response == "y": 
    no = random.randint(1,6) 
 
    if no == 1: 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 

    if no == 2: 
        print("[    0]") 
        print("[     ]") 
        print("[0    ]") 
        
    if no == 3: 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 

    if no == 4:  
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 

    if no == 5: 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 

    if no == 6: 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
          
    response = input("Press Y to roll again and N to exit:") 
    print("\n")