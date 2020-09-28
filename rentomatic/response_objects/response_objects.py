# -*- coding: utf-8 -*-


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = message

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    SUCCESS = "Success"

    def __init__(self, value=None):
        self.type = self.SUCCESS
        self.value = value

    def __bool__(self):
        return True
