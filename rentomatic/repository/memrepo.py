# -*- coding: utf-8 -*-

from rentomatic.domain import room as r


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters=None):
        result = [r.Room.from_dict(i) for i in self.data]

        if filters is None:
            return result
        elif "code__eq" in filters:
            result = [r for r in result if r.code == filters["code__eq"]]
        elif "price__eq" in filters:
            result = [
                r for r in result if r.price == int(filters["price__eq"])
            ]

        return result
