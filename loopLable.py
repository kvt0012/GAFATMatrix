class LoopLabel(object):
    def __init__(self):
        super(LoopLabel, self).__init__()

        class MyLoopLabel(Exception): pass

        self._label_exception = MyLoopLabel

    def __enter__(self):
        return self._label_exception

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self._label_exception:
            return True

        return False


