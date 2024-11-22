from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import LevelForm
from app.models import Level, db
from app.routes.Admin.AdminCRUDRoutes import AdminCRUDRoutes


class AdminLevelRoutes(AdminCRUDRoutes):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, "/admin/levels/", Level, LevelForm)