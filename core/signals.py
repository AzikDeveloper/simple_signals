class Signal:
    _signals = None

    def __init__(self):
        self._signals = {}

    def connect(self, receiver, sender):
        self._signals.setdefault(sender, [])
        self._signals[sender].append(receiver)

    def send(self, sender, *args, **kwargs):
        for func in self._signals.get(sender, []):
            func(sender, *args, **kwargs)


pre_init = Signal()
post_init = Signal()
