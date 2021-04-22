from copy import deepcopy


class FragileDict:
    def __init__(self, dic=None):
        if (dic is not None):
            self._data = deepcopy(dic)
        else:
            self._data = dict()
        self._lock = True

    def __enter__(self):
        self._lock = False
        self._old = deepcopy(self._data)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print("Exception has been suppressed.")
            self._data = deepcopy(self._old)
        else:
            self._data = deepcopy(self._data)
        delattr(self, "_old")
        self._lock = True
        return True

    def __setitem__(self, key, value):
        if not self._lock:
            if self._old is None:
                self._old = deepcopy(self._data)
            self._data.update({key: value})
            # self._old[key] = value
        else:
            raise RuntimeError("Protected state")

    def __getitem__(self, key):
        if not self._lock:
            if self._old is None:
                self._old = deepcopy(self._data)
            return self._data[key]
        else:
            return deepcopy(self._data[key])

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False
