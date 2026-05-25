from django.contrib import admin

from .models import (

    Car,

    Booking,

    Customer,

    Review,

    RentalLocation,

    CarCategory,

    Payment,

    Wishlist

)



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (

        'customer',

        'car',

        'status',

        'start_date',

        'end_date'

    )


    list_filter = (

        'status',

    )


    actions = [

        'approve_booking'

    ]


    def approve_booking(

        self,

        request,

        queryset

    ):


        for booking in queryset:


            booking.status = 'Approved'


            booking.car.available = False


            booking.car.save()


            booking.save()


        self.message_user(

            request,

            "Booking approved successfully ✅"

        )


    approve_booking.short_description = (

        "Approve selected bookings"

    )



admin.site.register(Car)

admin.site.register(Customer)

admin.site.register(Review)

admin.site.register(RentalLocation)

admin.site.register(CarCategory)

admin.site.register(Payment)

admin.site.register(Wishlist)