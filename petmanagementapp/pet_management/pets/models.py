from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=20)
    medical_notes = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.species})"


class ServiceType(models.Model):
    service_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    vaccination_dates = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment for {self.pet.name} on {self.date}"


class Reminder(models.Model):
    reminder_id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    due_date = models.DateField()

    def __str__(self):
        return f"Reminder: {self.message}"