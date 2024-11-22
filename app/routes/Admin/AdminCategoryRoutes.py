from flask import Blueprint

from app.forms.forms import CategoryForm
from app.models import Category
from app.routes.Admin.AdminCRUDRoutes import AdminCRUDRoutes


class AdminCategoryRoutes(AdminCRUDRoutes):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, "/admin/categories/", Category, CategoryForm)
