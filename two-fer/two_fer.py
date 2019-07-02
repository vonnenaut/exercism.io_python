def two_fer(name = "you"):
    if not isinstance(name, basestring):
        raise Exception(name + ' not a valid name.  Name must be a string.')
    return "One for " + name + ", one for me."
