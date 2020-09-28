# -*- coding: utf-8 -*-


class RoomListRequestObject:
    def __init__(self):
        self.filters = None

    @classmethod
    def from_dict(cls, adict):
        return cls()

    def __bool__(self):
        return True
