def returnSmallestPricedGPUs(gpuDict):
    itemsAvailable = []
    smallestPricedGPUs = []

    for priceAndAvailability in gpuDict.values():
        if (priceAndAvailability["availability"] == True):
            itemsAvailable.append(priceAndAvailability)

    if len(itemsAvailable) == 0:
        return []


    for priceAndAvailability in itemsAvailable:
        smallestPrice = priceAndAvailability["price"]
    
        if priceAndAvailability["price"] < smallestPrice:
            smallestPrice = priceAndAvailability["price"]
    
    print(list(gpuDict.keys())[list(gpuDict.values()).index(smallestPrice)])

        
    print("smallest = ", smallestPrice)