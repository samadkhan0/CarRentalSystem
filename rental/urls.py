from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'register/',
        views.register_user,
        name='register'
    ),

    path(
        'login/',
        views.login_user,
        name='login'
    ),

    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),
    
    path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
),

path(
    'book/<int:car_id>/',
    views.book_car,
    name='book_car'
),

path(

    'cancel/<int:booking_id>/',

    views.cancel_booking,

    name='cancel_booking'

),

path(

'review/<int:car_id>/',

views.add_review,

name='review'

),

path(
    
    'payment/<int:booking_id>/',
    
    views.payment,
    
    name='payment',
),

path(
    
    'invoice/<int:booking_id>/',
    
    views.invoice,
    
    name='invoice'
),

path(
    
    'car/<int:car_id>/',
    
    views.car_detail,
    
    name='car_detail'
),

path(
    
    'profile/',
    
    views.profile,
    
    name='profile'
),

path(

    'payment-success/<int:booking_id>/',

    views.payment_success,

    name='payment_success'

),

path(

    'wishlist/',

    views.wishlist,

    name='wishlist'

),


path(

    'wishlist/<int:car_id>/',

    views.add_to_wishlist,

    name='add_to_wishlist'

),

]