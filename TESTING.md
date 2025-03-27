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

### 📝 Posts

| Endpoint           | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
| `/posts/`          | Create post while logged out                      | 401 Unauthorized             |           | Auth required                  | ![](documentation/manual_testing/post_unauthorized.png) |
| `/posts/`          | Create post with missing title                    | 400 Bad Request              |           | Title is required              | ![](documentation/manual_testing/post_missing_title.png) |
| `/posts/<id>/`     | Update/delete someone else’s post                 | 403 Forbidden                |           | Authenticated user check       | ![](documentation/manual_testing/post_forbidden_edit.png) |
| `/posts/<id>/`     | Post with invalid JSON content                    | 400 Bad Request              |           | Content field format checked   | ![](documentation/manual_testing/post_invalid_json.png) |

---

### 💬 Comments

| Endpoint           | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
| `/comments/`       | Submit empty comment                              | 400 Bad Request              |           | Text required                  | ![](documentation/manual_testing/comment_empty.png) |
| `/comments/`       | Comment on non-existent post                      | 404 Not Found                |           | Invalid post ID handled        | ![](documentation/manual_testing/comment_invalid_post.png) |
| `/comments/<id>/`  | Try to delete another user’s comment              | 403 Forbidden                |           | Ownership required             | ![](documentation/manual_testing/comment_forbidden_delete.png) |

---

### ❤️ Likes

| Endpoint           | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
| `/likes/`          | Like post twice                                   | 400 Bad Request or 204 OK    |           | Uniqueness constraint          | ![](documentation/manual_testing/like_duplicate.png) |
| `/likes/`          | Like a deleted post                               | 404 Not Found                |           | Post existence check           | ![](documentation/manual_testing/like_deleted_post.png) |

---

### 🔁 Follows

| Endpoint           | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
| `/followers/`      | Follow yourself                                   | 400 Bad Request              |           | Prevent self-follow            | ![](documentation/manual_testing/follow_self.png) |
| `/followers/`      | Follow same user twice                            | 400 Bad Request              |           | Unique constraint applied      | ![](documentation/manual_testing/follow_duplicate.png) |

---

### ⚠️ Error Handling & Data Validation

| Area               | User Action                                       | Expected Result             | Pass/Fail | Comments                       | Screenshot |
|--------------------|---------------------------------------------------|------------------------------|-----------|--------------------------------|------------|
| Any POST endpoint  | Send malformed JSON                               | 400 Bad Request              |           | JSON parsing handled           | ![](documentation/manual_testing/json_error.png) |
| Any endpoint       | Submit wrong data types (e.g. string for int)     | 400 Bad Request              |           | Type validation enforced       | ![](documentation/manual_testing/wrong_type.png) |
| ForeignKey fields  | Use non-existent related object IDs               | 404 Not Found                |           | Foreign key integrity checked  | ![](documentation/manual_testing/invalid_fk.png) |
| Cloudinary uploads | No cloud_name config                              | 500 Server Error             |           | Error shown for bad setup      | ![](documentation/manual_testing/cloudinary_error.png) |

---

You can paste this directly into your `TESTING.md` and begin filling in the results as you test!

Want me to generate a downloadable `.md` file or add this to your existing `TESTING.md` now?



> [!NOTE]  
> [Go to Testing](#top)
