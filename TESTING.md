# Testing  <a id="top"></a>

> [!NOTE]  
> Return back to the [README.md](README.md) file.

---

## Code Validation

### Python (PEP8)

I used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all Python files in this Django project.  
No errors or warnings were found. Below are the results with screenshots stored in `documentation/pep_validation`.

| App/Folder         | File              | Screenshot                                                   |
|--------------------|-------------------|--------------------------------------------------------------|
| `comments`         | `models.py`       | ![models_comments](documentation/pep_validation/models_comments.png) |
|                    | `serializers.py`  | ![serializers_comments](documentation/pep_validation/serializers_comments.png) |
|                    | `urls.py`         | ![urls_comments](documentation/pep_validation/urls_comments.png) |
|                    | `views.py`        | ![views_comments](documentation/pep_validation/views_comments.png) |
| `followers`        | `models.py`       | ![models_followers](documentation/pep_validation/models_followers.png) |
|                    | `serializers.py`  | ![serializers_followers](documentation/pep_validation/serializers_followers.png) |
|                    | `urls.py`         | ![urls_followers](documentation/pep_validation/urls_followes.png) |
|                    | `views.py`        | ![views_followers](documentation/pep_validation/views_followers.png) |
| `likes`            | `models.py`       | ![models_likes](documentation/pep_validation/models_likes.png) |
|                    | `serializers.py`  | ![serializers_likes](documentation/pep_validation/serializers_likes.png) |
|                    | `urls.py`         | ![urls_likes](documentation/pep_validation/urls_likes.png) |
|                    | `views.py`        | ![views_likes](documentation/pep_validation/views_likes.png) |
| `posts`            | `models.py`       | ![models_posts](documentation/pep_validation/models_posts.png) |
|                    | `serializers.py`  | ![serializers_posts](documentation/pep_validation/serializers_posts.png) |
|                    | `urls.py`         | ![urls_posts](documentation/pep_validation/urls_posts.png) |
|                    | `views.py`        | ![views_posts](documentation/pep_validation/views_posts.png) |
| `profiles`         | `models.py`       | ![models_profiles](documentation/pep_validation/models_profiles.png) |
|                    | `serializers.py`  | ![serializers_profiles](documentation/pep_validation/serializers_profiles.png) |
|                    | `urls.py`         | ![urls_profiles](documentation/pep_validation/urls_profiles.png) |
|                    | `views.py`        | ![views_profiles](documentation/pep_validation/views_profiles.png) |
| `foodie_api` (project folder) | `permissions.py` | ![permissions_project](documentation/pep_validation/permissions_project.png) |
|                            | `serializers.py` | ![serializers_project](documentation/pep_validation/serializers_project.png) |
|                            | `settings.py`    | ![settings_project](documentation/pep_validation/settings_project.png) |
|                            | `urls.py`        | ![urls_project](documentation/pep_validation/urls_project.png) |
|                            | `views.py`       | ![views_project](documentation/pep_validation/views_project.png) |

---

## Defensive Programming

### 🧾 Registration

| Endpoint           | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
| `/dj-rest-auth/registration/` | Submit with missing `email` | 400 Bad Request | ✅ | Email is required | ![screenshot](documentation/manual_testing/registration_missing_email.png) |
| `/dj-rest-auth/registration/` | Submit with missing `username` | 400 Bad Request | ✅ | Username is required | ![screenshot](documentation/manual_testing/registration_missing_username.png) |
| `/dj-rest-auth/registration/` | Submit with missing `password1` | 400 Bad Request | ✅ | Password is required | ![screenshot](documentation/manual_testing/registration_missing_password.png) |
| `/dj-rest-auth/registration/` | Submit with invalid email format | 400 Bad Request | ✅ | Email format validation | ![screenshot](documentation/manual_testing/registration_invalid_email.png) |
| `/dj-rest-auth/registration/` | Submit with invalid username (e.g., symbols) | 400 Bad Request | ✅ | Username format validation | ![screenshot](documentation/manual_testing/registration_invalid_username.png) |
| `/dj-rest-auth/registration/` | Submit with short password | 400 Bad Request | ✅ | Password must be at least 8 characters | ![screenshot](documentation/manual_testing/registration_short_password.png) |
| `/dj-rest-auth/registration/` | Submit with common password (e.g., "password123") | 400 Bad Request | ✅ | Common passwords are rejected | ![screenshot](documentation/manual_testing/registration_common_password.png) |
| `/dj-rest-auth/registration/` | Passwords do not match (`password1` ≠ `password2`) | 400 Bad Request | ✅ | Mismatch warning shown | ![screenshot](documentation/manual_testing/registration_password_mismatch.png) |
| `/dj-rest-auth/registration/` | Submit valid form with all fields | 201 Created | ✅ | New user successfully registered | ![screenshot](documentation/manual_testing/registration_success.png) |

---

### 🔐 Login

| Endpoint | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
|----------|-------------|-----------------|-----------|----------|------------|
| `/dj-rest-auth/login/` | Submit without `password` | 400 Bad Request | ✅ | Password is required | ![screenshot](documentation/manual_testing/login_missing_password.png) |
| `/dj-rest-auth/login/` | Submit without `username` or `email` | 400 Bad Request | ✅ | Username or email is required | ![screenshot](documentation/manual_testing/login_missing_username.png) |
| `/dj-rest-auth/login/` | Submit with non-existent user credentials | 400 Bad Request | ✅ | No user found | ![screenshot](documentation/manual_testing/login_nonexistent_user.png) |
| `/dj-rest-auth/login/` | Submit with invalid email format | 400 Bad Request | ✅ | Email format is invalid | ![screenshot](documentation/manual_testing/login_invalid_email_format.png) |
| `/dj-rest-auth/login/` | Submit valid credentials | 200 OK | ✅ | JWT token and user returned | ![screenshot](documentation/manual_testing/login_success.png) |


---

### ✏️ Profile

| Endpoint           | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
### 👤 Profile

| Endpoint | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
|----------|-------------|-----------------|-----------|----------|------------|
| `/profiles/?author=:id` | Search for existing user profile | 200 OK | ✅ | User profile details displayed correctly | ![screenshot](documentation/manual_testing/profile_display_existing_user.png) |
| `/profiles/:id/` | Upload invalid image format (e.g., PDF) | 400 Bad Request | ✅ | Only image files are accepted | ![screenshot](documentation/manual_testing/profile_invalid_image_format.png) |
| `/profiles/?author=9999` | Search non-existent user | 404 Not Found or Empty result | ✅ | “No profile matches the given query.” shown | ![screenshot](documentation/manual_testing/profile_non_existent_user.png) |
| `/profiles/:id/` | Edit own profile with valid data | 200 OK | ✅ | Profile updated successfully | ![screenshot](documentation/manual_testing/profile_edit_success.png) |
| `/profiles/:id/` | Try editing another user's profile | 403 Forbidden or fields hidden | ✅ | Form fields hidden, edit not allowed | ![screenshot](documentation/manual_testing/profile_edit_blocked.png) |


---

### 📝 Post

| Endpoint | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
|----------|-------------|-----------------|-----------|----------|------------|
| `/posts/` | View all posts | 200 OK | ✅ | Existing posts displayed successfully | ![screenshot](documentation/manual_testing/posts_display_all.png) |
| `/posts/:id/` | View another user's post | Edit fields hidden | ✅ | Edit form not shown, read-only display | ![screenshot](documentation/manual_testing/posts_edit_blocked_other_user.png) |
| `/posts/:id/` | Edit own post | 200 OK | ✅ | Edit form shown, post updated successfully | ![screenshot](documentation/manual_testing/posts_edit_success.png) |
| `/posts/` | Create post with blank title | 400 Bad Request | ✅ | Title field is required | ![screenshot](documentation/manual_testing/posts_blank_title.png) |
| `/posts/` | Create post with empty content | 400 Bad Request | ✅ | JSON fields (intro, ingredients, steps, etc.) required | ![screenshot](documentation/manual_testing/posts_empty_content.png) |
| `/posts/` | Submit invalid content format (e.g., plain text) | 400 Bad Request | ✅ | Must be a valid JSON object | ![screenshot](documentation/manual_testing/posts_invalid_content_format.png) |
| `/posts/` | Upload non-image file as image (e.g., PDF) | 400 Bad Request | ✅ | File must be a valid image | ![screenshot](documentation/manual_testing/posts_invalid_image.png) |
| `/posts/` | Submit valid post with all fields | 201 Created | ✅ | Post created successfully | ![screenshot](documentation/manual_testing/posts_create_success.png) |


---

### 💬 Comment

| Endpoint | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
|----------|-------------|-----------------|-----------|----------|------------|
| `/comments/?post=:id` | View all comments for a post | 200 OK | ✅ | All related comments are displayed | ![screenshot](documentation/manual_testing/comments_display_all.png) |
| `/comments/` | Submit empty comment | 400 Bad Request | ✅ | "This field may not be blank" shown | ![screenshot](documentation/manual_testing/comments_empty_comment.png) |
| `/comments/` | Submit valid comment | 201 Created | ✅ | Comment posted successfully | ![screenshot](documentation/manual_testing/comments_post_success.png) |
| `/comments/:id/` | Edit newly created comment | 200 OK | ✅ | Comment updated successfully | ![screenshot](documentation/manual_testing/comments_edit_own_comment.png) |
| `/comments/:id/` | Edit existing comment created by user | 200 OK | ✅ | Comment editable and updated | ![screenshot](documentation/manual_testing/comments_edit_existing_comment.png) |
| `/comments/:id/` | Try editing another user's comment | Edit form not shown | ✅ | Edit option not visible, access blocked | ![screenshot](documentation/manual_testing/comments_edit_blocked.png) |


---

### ❤️ Likes

| Endpoint | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
|----------|-------------|-----------------|-----------|----------|------------|
| `/likes/` | View all likes | 200 OK | ✅ | Successfully displays all likes | ![screenshot](documentation/manual_testing/likes_display_all.png) |
| `/likes/:id/` | Visitor (not logged in) tries to delete a like | 401 Unauthorized | ✅ | "Authentication credentials were not provided." shown | ![screenshot](documentation/manual_testing/likes_delete_unauth.png) |
| `/likes/:id/` | Logged-in user views like they created | Edit (delete) option visible | ✅ | Correct delete option displayed for own like | ![screenshot](documentation/manual_testing/likes_editable.png) |
| `/likes/:id/` | Logged-in user unlikes a post | 204 No Content | ✅ | Like successfully deleted | ![screenshot](documentation/manual_testing/likes_delete_success.png) |
| `/likes/` | Logged-in user likes a post | 201 Created | ✅ | Post successfully liked | ![screenshot](documentation/manual_testing/likes_post_success.png) |
| `/likes/:id/` | Access non-existent like ID (e.g. `/likes/999/`) | 404 Not Found | ✅ | "Not found" or "No like matches the given query" shown | ![screenshot](documentation/manual_testing/likes_nonexistent_like.png) |


---


> **Note:** Due to time constraints and with the project submission deadline approaching, I did not implement the followers functionality in the frontend. As a result, I was only able to manually test two basic backend scenarios: ensuring unauthenticated users cannot follow, and verifying that authenticated users can successfully follow another user. Both tests passed as expected and are documented below.


### 🤝 Followers

| Endpoint | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
|----------|-------------|-----------------|-----------|----------|------------|
| `/followers/` | Visitor (not logged in) tries to follow | No follow option shown | ✅ | Auth required, follow option hidden in UI | ![screenshot](documentation/manual_testing/followers_no_follow_option_for_visitor.png) |
| `/followers/` | Logged-in user follows another user | 201 Created | ✅ | Follow created successfully | ![screenshot](documentation/manual_testing/followers_follow_success.png) |


---

## ⚠️ Error Handling & Data Validation

Throughout the manual testing process, both error handling and data validation were successfully verified across multiple features of the application.

**Data validation** was tested by submitting forms with missing or invalid fields. This included:
- Registration with missing email, password, or username
- Common and short passwords
- Invalid email formats
- Empty or non-JSON content in posts
- Uploading non-image files for image fields (e.g., PDF)

**Error handling** was tested by triggering:
- Unauthorized actions (e.g., liking or commenting while logged out)
- Forbidden actions (e.g., trying to edit another user's profile or post)
- Accessing non-existent data (e.g., invalid like ID, user profile, or comment)

The backend consistently responded with appropriate status codes (e.g., 400, 401, 403, 404, 204) and helpful error messages, confirming that both validation and error handling are properly implemented and functioning as expected.

---


> [!NOTE]  
> [Go to Testing](#top)
