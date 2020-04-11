from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    personal_info_complete = models.BooleanField(default=False)
    family_medical_history_complete = models.BooleanField(default=False)
    personal_medical_history_complete = models.BooleanField(default=False)
    associated_health_problems_complete = models.BooleanField(default=False)
    daily_routine_complete = models.BooleanField(default=False)
    payment_complete = models.BooleanField(default=False)
    on_boarding_complete = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.first_name + self.last_name


class PersonalInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='personal_information')
    profile_picture = models.ImageField(blank=True)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')),
                              blank=True)
    age = models.IntegerField(blank=True)
    address = models.CharField(max_length=500, blank=True)
    profession = models.CharField(max_length=100, choices=(('Retired', 'Retired'),
                                                           ('Homemaker', 'Homemaker'),
                                                           ('Service', 'Service'),
                                                           ('Self-employed', 'Self-employed')
                                                           ), blank=True)
    reason_for_visit = models.CharField(max_length=500, blank=True)
    diet_preference = models.CharField(max_length=15, choices=(
        ('Vegetarian', 'Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
        ('Eggiterian', 'Eggiterian'),
        ('Vegan', 'Vegan')
    ), blank=True)
    referral_source = models.CharField(max_length=20, choices=(
        ('Doctor', 'Doctor'),
        ('Friends', 'Friends'),
        ('Relatives', 'Relatives'),
        ('Newspapers', 'Newspapers'),
        ('Magazines', 'Magazines'),
        ('Facebook', 'Facebook'),
        ('Our Website', 'Our Website')
    ), blank=True)
    ref_name = models.CharField(max_length=50, blank=True)
    ref_number = PhoneNumberField(blank=True)
    ref_email = models.EmailField(blank=True)

    medications = models.CharField(max_length=100, blank=True)
    dosages = models.CharField(max_length=100, blank=True)


class FamilyMedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="family_medical_history")
    type = models.CharField(max_length=50, choices=(
        ('Obesity', 'Obesity'),
        ('Blood Pressure', 'Blood Pressure'),
        ('Heart Attack / Bypass / Stroke', 'Heart Attack / Bypass / Stroke'),
        ('Diabetes', 'Diabetes'),
        ('Cancer', 'Cancer'),
        ('Hypothyroid', 'Hypothyroid')
    ))
    member = models.CharField(max_length=50, choices=(
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Grand Mother', 'Grand Mother'),
        ('Grand Father', 'Grand Father'),
        ('Uncle', 'Uncle'),
        ('Aunt', 'Aunt'),
    ))


class PersonalMedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="personal_medical_history")
    type = models.CharField(max_length=50, choices=(
        ('Obesity', 'Obesity'),
        ('Blood Pressure', 'Blood Pressure'),
        ('Heart Attack / Bypass / Stroke', 'Heart Attack / Bypass / Stroke'),
        ('Diabetes', 'Diabetes'),
        ('Cancer', 'Cancer'),
        ('Hypothyroid', 'Hypothyroid'),
        ('Hyperthyroidism', 'Hyperthyroidism'),
        ('PCOD', 'PCOD'),
        ('Menopausal', 'Menopausal'),

    ), blank=True)
    blood_report = models.FileField(blank=True)


class AssociatedHealthProblems(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="associated_health_problems")
    acidity = models.BooleanField(blank=True)
    gout = models.BooleanField(blank=True)
    menstrual = models.CharField(max_length=20, choices=(
        ('Normal', 'Normal'),
        ('Disturbed', 'Disturbed'),
        ('Menopausal', 'Menopausal'),
        ('PCOD', 'PCOD'),
        ('Not Applicable', 'Not Applicable'),
    ), blank=True)
    pregnancies = models.IntegerField(blank=True)
    overweight_as_child = models.BooleanField(blank=True)
    weight_gain_since = models.DateField(blank=True)
    reason_for_gain = models.TextField(blank=True)
    lost_and_gained_times = models.IntegerField(blank=True)

    smoke = models.BooleanField(blank=True)
    smoke_level = models.CharField(max_length=100, choices=(
        ('Occasional', 'Occasional'),
        ('Regular', 'Regular'),
        ('Heavy', 'Heavy')
    ), blank=True)
    tobacco = models.BooleanField(blank=True)
    tobacco_level = models.CharField(max_length=100, choices=(
        ('Occasional', 'Occasional'),
        ('Regular', 'Regular'),
        ('Heavy', 'Heavy')
    ), blank=True)
    alcohol = models.BooleanField(blank=True)
    alcohol_level = models.CharField(max_length=100, choices=(
        ('Occasional', 'Occasional'),
        ('Regular', 'Regular'),
        ('Heavy', 'Heavy')
    ), blank=True)
    other_dietary_issues = models.TextField(blank=True)


class DailyRoutine(models.Model):
    wake_up_time = models.TimeField(blank=True)

    breakfast_time = models.TimeField(blank=True)

    mid_morning_time = models.TimeField(blank=True)

    lunch_time = models.TimeField(blank=True)
    lunch_location = models.CharField(max_length=100, blank=True, choices=(
        ('Home', 'Home'),
        ('Lunch Box', 'Lunch Box'),
        ('Office Canteen', 'Office Canteen'),
    ))

    tea_time = models.TimeField(blank=True)

    dinner_time = models.TimeField(blank=True)

    bed_time = models.TimeField(blank=True)

    office_start_time = models.TimeField(blank=True)
    office_end_time = models.TimeField(blank=True)

    exercise_routine = models.CharField(max_length=100, choices=(
        ('Regular', 'Regular'),
        ('Not Regular', 'Not Regular'),
    ))
    exercise_time = models.TimeField(blank=True)
    cardio = models.BooleanField(blank=True)
    strength_training = models.BooleanField(blank=True)
    yoga = models.BooleanField(blank=True)
    walk = models.BooleanField(blank=True)
