from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    roll_no = fields.Char(string='Roll Number', required=True)
    department = fields.Char(string='Department', required=True)
    course_ids = fields.Many2many(
        'student.management.course',
        'student_course_rel',
        'student_id',
        'course_id',
        string='Enrolled Courses'
    )

    def show_enrolled_courses(self, *args, **kwargs):
        """Method to show enrolled courses for bonus feature"""
        self.ensure_one()
        return {
            'name': 'Enrolled Courses',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'student.management.course',
            'domain': [('student_ids', 'in', [self.id])],
            'context': {'default_student_ids': [(4, self.id)]},
        }