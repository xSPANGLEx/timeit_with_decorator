def timeIt(func):
    import functools
    @functools.wraps(func)
    def _timeIt(*args,**kw):
        print "#Function:" + func.__name__
        import datetime
        start = datetime.datetime.now()
        result = func(*args,**kw)
        end = datetime.datetime.now()
        print "#Execute time:" + str(end - start)
        return result
    return _timeIt
