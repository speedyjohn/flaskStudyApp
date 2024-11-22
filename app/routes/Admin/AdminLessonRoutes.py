from flask import Blueprint, render_template, request, redirect, jsonify

from app.forms.forms import LessonForm
from app.forms.utils import fill_lesson_form, fill_lesson_form_edit
from app.models import Lesson, db, Category, Level
from app.routes.Admin.AdminCRUDRoutes import AdminCRUDRoutes


class AdminLessonRoutes(AdminCRUDRoutes):
    def __init__(self, bp: Blueprint):
        super().__init__(bp, "/admin/lessons/", Lesson, LessonForm)

    def create(self):
        response = super().create(fill_lesson_form)
        return response

    def edit(self, id):
        response = super().edit(id, fill_lesson_form_edit)
        return response
