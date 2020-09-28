# -*- coding: utf-8 -*-


class RoomListRequestObject:
    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        return cls(filters=adict.get("filters", None))

    def __bool__(self):
        return True
