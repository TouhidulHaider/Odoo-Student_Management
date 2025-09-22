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

## Screenshots

### Apps page
<img width="1878" height="977" alt="apps_page" src="https://github.com/user-attachments/assets/c50f5a8a-4c95-4bb2-95a0-6c422d2bf429" />

### My custom Student Management Module
<img width="1904" height="1032" alt="custom_student_management_module" src="https://github.com/user-attachments/assets/119846be-4880-44ed-a923-b34663b9fd96" />

### Models (student, course)
<img width="1905" height="1035" alt="student course_model" src="https://github.com/user-attachments/assets/26a7bc2e-a4f2-42ae-b033-e41ef18d8bd3" />

### Tree/List and Form views
<img width="1912" height="987" alt="views" src="https://github.com/user-attachments/assets/2ea3dab4-55bf-4ac3-9c09-d1e8c8dc5269" />

### Menus
```
student_management/
├── Students
├── Courses
```
<img width="640" height="317" alt="menus" src="https://github.com/user-attachments/assets/6b0430cd-a63d-4fef-b8a8-5377308821e5" />
<br>

### Student Form View
<img width="1908" height="987" alt="student_form_view" src="https://github.com/user-attachments/assets/c929f930-5db9-4fd9-8bb8-f3b131916b51" />
<br>

### Course Form view
<img width="1909" height="985" alt="course_form_view" src="https://github.com/user-attachments/assets/d71328f4-89d9-4fbb-812e-822cdcf54180" />

### New Student Enrollment
<img width="1914" height="943" alt="new_student_enrollment" src="https://github.com/user-attachments/assets/f4a931a4-99d2-403a-a0d7-68e5ba9bd434" />

### Individual Student View
<img width="1909" height="983" alt="individual_student_view" src="https://github.com/user-attachments/assets/560f2bbf-92f3-42b9-b383-de83ac485c04" />

### Add New Course
<img width="1913" height="980" alt="new_course_create_view" src="https://github.com/user-attachments/assets/1927f908-7970-4aad-bf25-2459c207d78e" />
