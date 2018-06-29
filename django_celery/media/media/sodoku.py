b = [6, 2, 3, 8]

import operator

def makeArrayConsecutive2(statues):
    return   len(list(range(sorted(statues)[0] , sorted(statues)[-1] +1 ))) - len(statues)



print(makeArrayConsecutive2(b))