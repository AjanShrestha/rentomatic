# -*- coding: utf-8 -*-


class RoomListUseCase:
    def __init__(self, repo):
        self.repo = repo

    def execute(self):
        return self.repo.list()
