# StrideSync

StrideSync is a full-stack web-based step challenge and daily step-tracking application built with **Django** and **PostgreSQL / Supabase**. It enables users to manage accounts, track daily step counts against personal step goals, and view progress through role-based dashboards.

## Technology Stack

- **Backend & Frontend:** Full-Stack Django (Python, Django Templates, Django Authentication)
- **Database:** PostgreSQL / Supabase (SQLite is not used for the final setup)
- **Environment & Dependencies:** `python-dotenv`, `psycopg`, `Pillow`

## Features Implemented

### Project Development 1 — Account Feature
- **Account Registration:** User registration form with required field validation, email format checks, unique username/email validation, password confirmation matching, and hashed password storage via Django's authentication system.
- **Login / Logout:** Session-based login with credential validation and clear error messages, logout session termination, and `@login_required` protection redirecting unauthenticated users to the login page.
- **Role-Based User Dashboard:** Role-specific dashboards and navigation for `MEMBER` and `ADMIN` roles, with route/role enforcement preventing users from accessing another role's dashboard directly by URL.
- **User Profile:** Logged-in users can view and update their own profile information (such as name, email, contact number, daily step goal, and profile photo), scoped strictly to the authenticated user.

### Project Development 2 — Core Feature (Vertical Slice): Daily Step Tracking
- **Database Layer:** `StepLog` model in PostgreSQL/Supabase linked via `ForeignKey` to `User` (`user`), with `date`, `step_count`, `notes`, timestamps, and a unique constraint per user and date.
- **Backend Layer:** Django views, forms, and URL routes supporting full Create, Read, Update, and Delete (CRUD) operations on step entries, protected by `@login_required`, record ownership checks, and server-side validation with success/error feedback.
- **Frontend Layer:** Django templates integrated with the role-based dashboards allowing members to log daily steps, inspect step history and daily goal progress, edit existing step entries, and delete step records end-to-end.

## Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Jsaph227/StrideSync-Cantillas-Bryce-G06.git](https://github.com/Jsaph227/StrideSync-Cantillas-Bryce-G06.git)
   cd StrideSync-Cantillas-Bryce-G06
