def chain_loop(args):
    def ii(args):
        for arg in args:
            yield iter(arg)

    iterators = ii(args)
    while iterators:
        my_list = []
        for elem in iterators:
            try:
                yield next(elem)
                my_list.append(elem)
            except StopIteration:
                pass
        iterators = my_list
