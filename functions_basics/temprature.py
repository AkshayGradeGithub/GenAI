def temprature(temp,unit):
    if unit =='C':
        return temp *9/5 + 32
    elif unit=='F':
        return(temp-32)*5/9
    else:
        return None


cal=temprature(77,"F")
print(cal)
