from odoo import models, fields


class Course(models.Model):
    _name = 'student.management.course'
    _description = 'Course'
    _rec_name = 'name'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    credit = fields.Integer(string='Credit', required=True)
    student_ids = fields.Many2many(
        'student.management.student',
        'student_course_rel',
        'course_id',
        'student_id',
        string='Enrolled Students'
    )