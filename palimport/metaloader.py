class MetaLoader(type):
    def __new__(meta, name, bases, dct):
        print('-----------------------------------')
        print("Allocating memory for class", name)
        print(meta)
        print(bases)
        print(dct)

        # make sure we dont override attributes from existing bases (loader infra)
        # Maybe not a good idea...
        # all_attrs = [a for b in bases for a in dir(b)]
        # overrides = [a for a in dct if a in all_attrs]
        # for o in overrides:
        #     _verbose_message("Overriding attribute detected : {o}. Dropping.".format(**locals()))
        #     dct.pop(o)

        assert 'parser' in dct
        assert 'transformer' in dct

        return super(MetaLoader, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('-----------------------------------')
        print("Initializing class", name)
        print(cls)
        print(bases)
        print(dct)

        super(MetaLoader, cls).__init__(name, bases, dct)

        # todo add somerelated stuff to grammar

    def __call__(cls, *args, **kwds):
        print('__call__ of ', str(cls))
        print('__call__ *args=', str(args))
        print('__call__ **kwds=', str(kwds))
        return type.__call__(cls, *args, **kwds)

