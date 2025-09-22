{
    'name': 'Student Management',
    'version': '1.0.0',
    'category': 'Education',
    'summary': 'Manage Students and Courses',
    'description': """
        Student Management Module
        =========================
        This module allows you to:
        * Manage students with their basic information
        * Manage courses with credits
        * Enroll students in multiple courses
        * View course enrollments
    """,
    'author': 'Your Name',
    'website': 'https://www.odoo-school.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/course_views.xml',
        'views/actions.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': 'static/description/icon.png',
}