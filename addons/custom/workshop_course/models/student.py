from odoo import models, fields

class WorkshopStudent(models.Model):
    _name = "workshop.student"
    _description = "Workshop Student"

    name = fields.Char(required=True)
    email = fields.Char()
    course_ids = fields.Many2many(
        "workshop.course",
        string="Enrolled Courses"
    )
