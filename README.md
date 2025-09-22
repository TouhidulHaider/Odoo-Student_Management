
# Student Management Odoo Module

## Installation Steps

1. **Download and Install Odoo:**
   - Download Odoo from the [official website](https://www.odoo.com/page/download).
   - Extract and configure Odoo in VS Code for development.

2. **Configure PostgreSQL Database:**
   - Install PostgreSQL and create a database user for Odoo.
   - Update your `odoo.conf` file with the correct database connection parameters.
   - If you face connection issues, ensure PostgreSQL is running and the user/password are correct.

3. **Add the Module:**
   - Place the `student_management` folder inside your Odoo `addons` directory (or keep it in `server/addons` if using this repo structure).

4. **Update Odoo Apps List:**
   - Log in to your Odoo backend as admin.
   - Go to Apps > Update Apps List > Click 'Update'.

5. **Upgrade the Module:**
   - Made changes and upgraded the module

## Testing the Module

1. Go to the "Student Management" menu in Odoo.
2. Add students and courses using the provided forms.
3. Use the "Show Enrolled Courses" button on a student form to view their enrollments.
4. Test course and student listings, and try enrolling students in courses.

## Challenges Faced & Solutions

- **PostgreSQL Database Connection:**
  - *Problem:* Difficulty connecting Odoo to PostgreSQL.
  - *Solution:* Ensured PostgreSQL was running, user credentials were correct, and `odoo.conf` was properly configured.

- **View/Action Errors:**
  - *Problem:* Odoo errors about missing tree views or view types not defined.
  - *Solution:* Ensured all actions referenced valid view types (`list,form`) and that all required views were defined in XML.

- **Button Action TypeError:**
  - *Problem:* TypeError when clicking the "Show Enrolled Courses" button (wrong method signature).
  - *Tried Solution:* Updated the method to accept `*args, **kwargs` still it's not working as an Odoo button action.

- **Module Icon Not Showing:**
  - *Problem:* The module icon was not visible in the Apps list.
  - *Solution:* Added the `icon` key to the `__manifest__.py`.

