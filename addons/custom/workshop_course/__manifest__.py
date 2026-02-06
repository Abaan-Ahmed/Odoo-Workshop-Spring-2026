{
    "name": "Workshop Course",
    "version": "1.0",
    "category": "Education",
    "summary": "Course management module for Odoo workshop",
    "author": "Workshop Instructor",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/course_views.xml",
        "views/student_views.xml",
        "views/menus.xml",
        "views/website_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "workshop_course/static/src/css/workshop.css",
        ],
    },
    "installable": True,
    "application": True,
}
