def DictTemplate(base, required=(), optional=()):
    """Utility for creating dictionary templates. Usage:
    >>> template = DictTemplate(base={a:1})
    >>> template()
    {a:1}
    >>> template_2 = DictTemplate(base={a:1}, required=("b"))
    >>> template_2(b=2)
    {a:1, b:2}
    """
    def function(**kwargs):
        complete = dict(base)
        try:
            complete.update({key: kwargs[key] for key in required})
        except KeyError:
            raise KeyError("Requires each of the following keys: {0}"\
                           .format(required)) 
        complete.update({key: kwargs[key] for key in optional 
                         if kwargs.has_key(key)})
        return complete
    return function