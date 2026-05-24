from django.contrib import admin

from .models import (

    Car,

    Booking,

    Customer,

    Review,

    RentalLocation,

    CarCategory,

    Payment

)



# ------------------
# CAR ADMIN
# ------------------

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = (

        'name',

        'brand',

        'price_per_day',

        'fuel_type',

        'seats',

        'transmission',

        'available'

    )


    list_filter = (

        'fuel_type',

        'available',

        'transmission'

    )


    search_fields = (

        'name',

        'brand'

    )




# ------------------
# BOOKING ADMIN
# ------------------

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (

        'customer',

        'car',

        'status',

        'start_date',

        'end_date'

    )


    actions = [

        'approve_booking'

    ]


    def approve_booking(

        self,

        request,

        queryset

    ):


        queryset.update(

            status='Approved'

        )


        for booking in queryset:

            booking.car.available = False

            booking.car.save()


    approve_booking.short_description = (

        "Approve selected bookings"

    )


                    
admin.site.register(Customer)

admin.site.register(Review)

admin.site.register(RentalLocation)

admin.site.register(CarCategory)

admin.site.register(Payment)