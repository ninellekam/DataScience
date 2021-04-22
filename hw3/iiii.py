from copy import deepcopy


class FragileDict:
    def __init__(self, d=None):
        if d is None:
            self._data = {}
        else:
            self._data = deepcopy(d)
        self._lock = True

    def __getitem__(self, key):
        if self._lock:
            return deepcopy(self._data[key])
        else:
            if key in self._new_data_:
                return self._new_data_[key]
            else:
                self._new_data_[key] = deepcopy(self._data[key])
                return self._new_data_[key]

    def __setitem__(self, key, val):
        if self._lock:
            raise RuntimeError("Protected state")
        self._new_data_[key] = val

    def __contains__(self, key):
        if self._lock:
            return key in self._data
        else:
            if key in self._new_data_:
                return key in self._new_data_
            if key in self._data:
                return key in self._new_data_

    def __enter__(self):
        self._lock = False
        self._new_data_ = {}
        return self

    def __exit__(self, exception_type, exception_val, trace):
        if exception_type is not None:
            del self._new_data_
            print("Exception has been suppressed.")
            return True
        for key, value in self._new_data_.items():
            self._data[key] = deepcopy(value)
        del self._new_data_
        self._lock = True


d = FragileDict({'key': 5})

with d:
    d['key'] = 6
    print(d['key'])
    d['ord'] = 7
    print('ord' in d and d['ord'] == 7)
    raise Exception()

print(d['key'])
print('ord' not in d)