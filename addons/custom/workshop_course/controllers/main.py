from odoo import http
from odoo.http import request

class WorkshopWebsite(http.Controller):

    @http.route("/courses", auth="public", website=True)
    def course_page(self):
        courses = request.env["workshop.course"].sudo().search([])
        return request.render(
            "workshop_course.course_page",
            {"courses": courses}
        )
