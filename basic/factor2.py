def printDivisors(n) : 
      
    # Note that this loop runs till square root 
    i = 1
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n / i == i) : 
                print i, 
            else : 
                # Otherwise print both 
                print i , n/i, 
        i = i + 1
        
