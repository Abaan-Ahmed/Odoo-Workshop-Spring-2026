from odoo import models, fields

class WorkshopCourse(models.Model):
    _name = "workshop.course"
    _description = "Workshop Course"

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text()
    price = fields.Float()
    active = fields.Boolean(default=True)
