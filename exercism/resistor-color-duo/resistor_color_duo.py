def value(colors):
    default = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    # first = default.index(colors[0])
    # second = default.index(colors[1])
    
    # if (first == 0):
    #     numerical_value = str(second)
    # else:
    #     numerical_value = str(first)+str(second)

    # return int(numerical_value)
    return default.index(colors[0])*10 + default.index(colors[1])

l = ["brown","green"]
print (value(l))