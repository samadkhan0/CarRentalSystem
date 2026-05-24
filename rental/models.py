from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE

    )


    phone = models.CharField(

        max_length=20,

        blank=True,

        null=True

    )


    city = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )


    license_number = models.CharField(

        max_length=100,

        blank=True,

        null=True

    )


    profile_picture = models.ImageField(

        upload_to='profiles/',

        blank=True,

        null=True

    )


    def __str__(self):

        return self.user.username

        

class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class RentalLocation(models.Model):
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.city} - {self.address}"

class Car(models.Model):

    name = models.CharField(
        max_length=100
    )

    brand = models.CharField(
        max_length=100
    )
    
    category = models.ForeignKey(

    CarCategory,

    on_delete=models.CASCADE,

    null=True,

    blank=True

)

    model_year = models.IntegerField()

    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    location = models.ForeignKey(

        RentalLocation,

        on_delete=models.CASCADE,

        null=True,

        blank=True

    )

    image = models.ImageField(

        upload_to='cars/',

        blank=True,

        null=True

    )

    available = models.BooleanField(
        default=True

    )

    seats = models.PositiveIntegerField(
    default=5
)


    fuel_type = models.CharField(

    max_length=20,

    choices=[

        ('Petrol','Petrol'),

        ('Diesel','Diesel'),

        ('Electric','Electric'),

        ('Hybrid','Hybrid')

    ],

    default='Petrol'

)


    transmission = models.CharField(

    max_length=20,

    choices=[

        ('Manual','Manual'),

        ('Automatic','Automatic')

    ],

    default='Automatic'

)


    mileage = models.PositiveIntegerField(
    default=15
)


    color = models.CharField(
    max_length=30,
    default='Black'
)


    luggage = models.PositiveIntegerField(
    default=2
)


    air_conditioning = models.BooleanField(
    default=True
)

    def __str__(self):

        return self.name

class Booking(models.Model):

    customer = models.ForeignKey(

        Customer,

        on_delete=models.CASCADE

    )

    car = models.ForeignKey(

        Car,

        on_delete=models.CASCADE

    )

    pickup_location = models.ForeignKey(

        'RentalLocation',

        on_delete=models.CASCADE,

        related_name='pickup_bookings',

        null=True,

        blank=True

    )

    return_location = models.ForeignKey(

        'RentalLocation',

        on_delete=models.CASCADE,

        related_name='return_bookings',

        null=True,

        blank=True

    )

    start_date = models.DateField()

    end_date = models.DateField()

    total_price = models.DecimalField(

        max_digits=10,

        decimal_places=2,
        
        null=True,
        
        blank=True,
        

    )

    status = models.CharField(

        max_length=50,

        default='Pending'

    )


    def _str_(self):

        return f"{self.customer} - {self.car}"
    
class Payment(models.Model):

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    payment_method = models.CharField(
        max_length=50,
        default='Card',
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='Paid',
        blank=True
    )
    
class Review(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField()

    comment = models.TextField()
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        
        return self.name
    
        return self.car.name