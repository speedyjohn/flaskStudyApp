from flask import Blueprint


class AdminRoutes:
    def __init__(self, bp: Blueprint):
        self.bp = bp