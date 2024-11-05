def hackerlandRadioTransmitters(x, k):

    hazak = sorted(x)
    minimum = hazak[0]
    antennak = 1
    kozep = 0
    
    for i in range(1, len(x)):
        if (hazak[i] - minimum) <= k:
            kozep = hazak[i]
        if not hazak[i] - kozep <= k:
            antennak += 1
            minimum = hazak[i]
            
    return antennak