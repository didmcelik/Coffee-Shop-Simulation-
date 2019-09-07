"""
E.Didem ÇELİK
250201032

"""
coffee_list = ["Espresso", "Cappuccino", "Americano", "Macchiato", "Mocha", "Filter", "Turkish"]
price_list = [5.50, 7.75, 7.25, 9.50, 9.25, 5.75, 6]
coffee_type=input("Enter the coffee type ").title()

total_cup = 0
total=float(0.0)
customer=int(0)
i=0

while(coffee_type!="X"):
    customer += 1
    #Checking if coffee_type is in the list
    while not(coffee_type in coffee_list): 
        coffee_type=input("Please enter reasonable coffee type ").title()
    # Checking the type because Turkish coffe has fixed size
    if(coffee_type != 'Turkish'): 
        cup_size=input("Enter the cup size of coffee : Tall, Grande, Venti ").title() 
        
        #Checking validation of size
        while not (cup_size == 'Tall' or cup_size == 'Grande' or cup_size =='Venti'): 
            cup_size=input("Please enter one of these sizes: Tall, Grande, Venti ").title()
        
        number_of_cups=float(input("Enter the number of cups "))
        #Checking validation of number of cups
        while not(type(number_of_cups)==int or type(number_of_cups)==float ):
            number_of_cups=input("Pelase enter valid number for number of cups ")
        
       #Checking if customer has free coffe or not   
        if(customer % 10 == 0):
            print ("CONGURATS !! You don't have to pay for today. It is on us!!!")
        else:      
           #Calculating the price for the customer
            for i in range(len(coffee_list)):
                if coffee_list[i]==coffee_type:
                    if(cup_size=="Tall"):
                        price=number_of_cups*price_list[i]
                    elif(cup_size=="Grande"):
                        price=number_of_cups*(price_list[i] +1)
                    else:
                        price=number_of_cups* (price_list[i] + 1.5)
    #For price of Turkish Coffee(has no size)   
    else:   
        number_of_cups=float(input("Enter the number of cups "))
        #Checking validation of number of cups
        while not(type(number_of_cups)==int or type(number_of_cups)==float):
            
            number_of_cups=input("Pelase enter valid number for number of cups ")
        
       #Checking if customer has free coffe or not   
        if(customer % 10 == 0):
            print ("CONGRATS !! You don't have to pay for today. It is on us!!!")
        else:      
           #Calculating the price for the customer
           price=number_of_cups * 6
    
    #Checking if price>20 it will be %10 discount.
    if(price > 20):
        price =  price - (price * 0.1)
        print("You order " ,number_of_cups, " " ,coffee_type, " and your price with %10 discount : ", price)
    else:
        print("You order " ,number_of_cups, " " ,coffee_type, " and your price : ", price)
    
    total= total + price          
    total_cup += 1  
    #Checking end of the day total gain and total customer.         
    coffee_type=input("Hello again. If you want more coffee please enter the coffee type, or for exit enter X ").title()
    

print("End of the day total gain : ", total, " total cup: ",total_cup, " and total customer: ", customer)





    
                    
                
                
            
        
        
        
        
        

        
        
        
    












 


