from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import CategoryForm
from app.models import db, Category
from app.routes.Admin.AdminCRUDRoutes import AdminCRUDRoutes


class AdminCategoryRoutes(AdminCRUDRoutes):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, "/admin/categories/", Category, CategoryForm)
