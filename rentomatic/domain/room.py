# -*- coding: utf-8 -*-


class Room:
    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, adict):
        return cls(
            code=adict["code"],
            size=adict["size"],
            price=adict["price"],
            longitude=adict["longitude"],
            latitude=adict["latitude"],
        )
