# Hotel Management System 
# Object Relational Mapping

from django.db import models
import uuid

# Hotel class
class Hotel(models.Model):
    hotel_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel_name = models.CharField(max_length=255)
    hotel_address = models.TextField()
    hotel_phone = models.CharField(max_length=15) 
    hotel_email = models.CharField(max_length=255)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()

    def __str__(self):
        return self.hotel_name
    
    
 # Room Type For Room class
class RoomType(models.Model):
    type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_name = models.CharField(max_length=255)
    room_desc = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2) 
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.room_name
     


#Room Class
class Room(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.hotel_id.hotel_name} - {self.room_type.room_name}"
    
    
#Staff class
class Staff(models.Model):
    staff_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel_id = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    staff_name = models.CharField(max_length=255)
    staff_position = models.CharField(max_length=255)
    staff_phone = models.CharField(max_length=15)
    staff_email = models.CharField(max_length=255)
    staff_salary = models.DecimalField(max_digits=10, decimal_places=2) 
    hire_date = models.DateField()
    
    def __str__(self):
        return self.staff_name
    
    
# Guest class
class Guest(models.Model):
    guest_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest_name = models.CharField(max_length=255)
    guest_address = models.CharField(max_length=255)
    guest_phone = models.CharField(max_length=15)
    guest_email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.guest_name
    
    
#booking class
class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest_id = models.ForeignKey(Guest, on_delete = models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete = models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.room_id.room_type.room_name} - {self.guest_id.guest_name}"

    
    



  
