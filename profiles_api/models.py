from django.db import models
# below import statements are required if we want to overrider any standard models
# here we want to use email addresaa in place of username
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):

    def create_user(self, email,name, password = None):
        if not email:
            raise ValueError('user must have non-empty email address')

        email = self.normalize_email(email)
        user = self.model(email = email , name = name)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email , name , password):
        user = self.create_user(email , name , password)
        # here we dont need to pass self as , any function which is present in same class dont need to pass self
        # is_superuser is provided by permission mixin
        user.is_superuser = True
        user.is_active = True
        user.save(using = self._db)

        return user



class UserProfile(AbstractBaseUser , PermissionsMixin):
    """Django model for user class """
    email = models.EmailField(max_length = 255 , unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)


    # Lets create model managers
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

"""
### What is `BaseUserManager`?

`BaseUserManager` is a class provided by Django's `auth` module, primarily used to manage user-related tasks which are essential for handling user authentication.
This class provides several helper methods to handle user creation and management, ensuring that user data is handled consistently and securely.

### Use Cases of `BaseUserManager`

- **User Creation**: `BaseUserManager` contains methods to create user instances, ensuring that all essential attributes like email and password are s
et and validated correctly.
- **Password Management**: It includes methods to handle password setting and hashing securely.
- **Normalization**: It offers normalization methods for fields like email, which help in maintaining the consistency and uniqueness of user data.

### Are `normalize_email()`, `set_password()`, `self.model()`, Default Methods Provided by `BaseUserManager`?

- **`normalize_email()`**: Yes, it is provided by `BaseUserManager` and is used to normalize the email address by lowercasing the domain part of the email.
- **`set_password()`**: This method is provided by the `AbstractBaseUser` class, which is often used together with `BaseUserManager` in custom user models.
It is used for setting and hashing the user password.
- **`self.model()`**: `self.model` isn't a method but a property that refers to the model class associated with the manager. This is not explicitly provided
 by `BaseUserManager`; rather, it is inherited from `Manager`, the base class for all Django model managers.
- **`self._db`**: This is an internal attribute used to specify which database should be used when multiple databases are configured in Django. It helps in
directing operations to the appropriate database.

### What is the Use of `self.model()`?

- `self.model()` is a way to refer to the model class that the manager is associated with. When you define a custom manager in a model, Django sets this
attribute to point to the model class.

### Why is `password=None` Written?

- Setting `password=None` as a default argument in the `create_user` method allows the creation of users without setting a password initially.
This can be useful in cases where users are created by an admin and are expected to set their password later or through another mechanism like an email confirmation process.

### Explanation of "where `self.model` refers to the model class associated with this manager."

- This phrase means that `self.model` in the context of a model manager points back to the Django model class that the manager is attached to.
For example, if you have a `User` model with a custom manager, inside that manager `self.model` will refer to the `User` class.

### Is This Written in a Different Class?

- `self.model` is usually set up by Django's internals when a manager is used within a model. It's not something typically written by a developer;
 rather, it is automatically handled by Django.

### Do We Pass Username and Mail in `UserProfileManager()`?

- The `UserProfileManager()` does not directly receive parameters like username or mail when it's instantiated. Instead, methods like `create_user`
 defined within the manager receive such parameters to handle specific data operations. The manager itself is instantiated without such parameters,
and it uses its methods to interact with model instances.

Overall, `BaseUserManager` plays a crucial role in abstracting and securing the user management processes, providing a robust foundation for
handling user authentication in Django applications.
"""



"""
whats the difference between models and model manager

Key Differences
Purpose:

Models define the structure of the database.
Model Managers define how to access and query the database.
Usage:

Models are used to create, update, delete, and manipulate the actual data instances (rows in the database).
Model Managers are used to query the database to return QuerySet instances which can be further filtered or manipulated.
Definition:

Models are defined by subclassing django.db.models.Model.
Model Managers are instances of django.db.models.Manager or subclasses thereof.
Customization:

Customizing a model typically involves adding fields or methods that represent behaviors or properties of the single data instance.
Customizing a manager typically involves defining methods that allow more complex querying of the database or provide shortcuts for frequent query patterns.


Why Use Model Managers?
Custom QuerySet Methods: Model managers allow you to add extra QuerySet methods, which can encapsulate common filters or ordering options.
This keeps your code DRY and focused, improving maintainability.

Code Reusability: You can reuse a manager by attaching it to multiple models or by adding it to an abstract base class that other models inherit from.

Enhancing Readability: Custom managers can make your code more descriptive and readable by providing methods with clear names related to business logic.

Encapsulation: Managers help encapsulate the database access logic within the model and keep your model methods higher-level,
dealing with operations on the model instance and non-query related logic.
"""


"""
Yes, `BaseUserManager` in Django includes the methods `create_user` and `create_superuser`. These are helper methods that simplify the creation of user and superuser instances, respectively. Here’s a brief explanation and typical syntax for each:

### 1. `create_user`
This method is used to create a regular user. When extending `BaseUserManager`, you usually override this method to handle the user creation process according to your application’s user model requirements.

**Syntax:**
```python
def create_user(self, username, email=None, password=None, **extra_fields):
    # Ensure that an email address is set
    if not email:
        raise ValueError('The given email must be set')
    email = self.normalize_email(email)
    user = self.model(username=username, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
```

### 2. `create_superuser`
This method is used for creating a superuser who has all permissions. This method also typically calls `create_user` internally but sets additional attributes such as `is_staff` and `is_superuser` to `True`.

**Syntax:**
```python
def create_superuser(self, username, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

    return self.create_user(username, email, password, **extra_fields)
```

### Important Points:
- **`normalize_email`**: This utility method is part of `BaseUserManager` and is used to normalize the email address by lowercasing the domain part of it.
- **`set_password`**: This is another method from Django’s user model that sets the user’s hashed password.
- **`save`**: This method saves the user instance to the database. The `using=self._db` ensures that the correct database alias is used, especially useful in multi-database setups.

When you define these methods in your custom user manager, you tailor the user creation logic to your specific needs, often modifying parameters and adding additional fields as necessary.
"""
