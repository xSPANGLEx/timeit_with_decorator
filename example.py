import timeIt

@timeIt.timeIt
def forLoop():
    x = []
    for i in range(100000):
        x.append("x:"+str(i))
    print len(x)
    return x

@timeIt.timeIt
def listComprehension():
    x = 0
    x = ["x:"+str(i) for i in range(100000)]
    print len(x)
    return x

forLoop()
listComprehension()
