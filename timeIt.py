def timeIt(func):
    import functools
    @functools.wraps(func)
    def _timeIt(*args,**kw):
        import datetime
        start = datetime.datetime.now()
        result = func(*args,**kw)
        end = datetime.datetime.now()
        print "Execute time:" + str(end - start)
        return result
    return _timeIt
