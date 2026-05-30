from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.models import User

from django.http import HttpResponse

from reportlab.pdfgen import canvas

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (
    Car,
    Booking,
    Customer,
    RentalLocation,
    Review,
    Payment,
    Wishlist
)

from django.db.models import Avg, Q

from datetime import datetime



# HOME PAGE
def home(request):

    cars = Car.objects.filter(

        available=True

    )


    search = request.GET.get(

        'search'

    )


    if search:

        cars = cars.filter(

            Q(name__icontains=search) |

            Q(brand__icontains=search) |

            Q(category__name__icontains=search) |

            Q(fuel_type__icontains=search) |

            Q(transmission__icontains=search) |

            Q(seats__icontains=search) |

            Q(price_per_day__icontains=search)

        )


    for car in cars:

        avg = Review.objects.filter(

            car=car

        ).aggregate(

            Avg(

                'rating'

            )

        )


        car.average_rating = avg[

            'rating__avg'

        ]



    return render(

        request,

        'home.html',

        {

            'cars': cars

        }

    )

# REGISTER

def register_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                'Username already exists'
            )

            return redirect(
                'register'
            )


        User.objects.create_user(
            username=username,
            password=password
        )


        messages.success(
            request,
            'Account created successfully ✅'
        )


        return redirect(
            'login'
        )


    return render(
        request,
        'register.html'
    )


# LOGIN

def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(

            request,

            username=username,

            password=password

        )


        if user is not None:

            login(
                request,
                user
            )


            messages.success(
                request,
                'Login successful ✅'
            )


            return redirect(
                'home'
            )


        else:

            messages.error(
                request,
                'Invalid username or password'
            )


            return redirect(
                'login'
            )


    return render(
        request,
        'login.html'
    )




# BOOK CAR

@login_required
def book_car(request, car_id):

    car = get_object_or_404(
        Car,
        id=car_id
    )

    customer, created = Customer.objects.get_or_create(
        user=request.user
    )

    locations = RentalLocation.objects.all()


    if request.method == 'POST':

        start_date = request.POST['start_date']
        end_date = request.POST['end_date']


        pickup_location = RentalLocation.objects.get(
            id=request.POST['pickup_location']
        )

        return_location = RentalLocation.objects.get(
            id=request.POST['return_location']
        )


        days = (
            datetime.strptime(end_date, "%Y-%m-%d")
            -
            datetime.strptime(start_date, "%Y-%m-%d")
        ).days


        total = days * car.price_per_day


        booking = Booking.objects.create(

            customer=customer,

            car=car,

            pickup_location=pickup_location,

            return_location=return_location,

            start_date=start_date,

            end_date=end_date,

            total_price=total,

            status='Pending'

        )


        return redirect(

            'payment',

            booking.id

        )


    return render(

        request,

        'book_car.html',

        {

            'car': car,

            'locations': locations

        }

    )


# DASHBOARD
@login_required
def dashboard(request):

    customer = Customer.objects.get(

        user=request.user

    )


    bookings = Booking.objects.filter(

        customer=customer

    ).order_by(

        '-id'

    )


    active_bookings = bookings.filter(

        status='Pending'

    ).count()


    approved = bookings.filter(

        status='Approved'

    ).count()


    cancelled = bookings.filter(

        status='Cancelled'

    ).count()


    total_spent = sum(

        booking.total_price

        for booking in bookings

    )


    reviews_count = Review.objects.filter(

        customer=customer

    ).count()



    context = {

        'customer': customer,

        'bookings': bookings,

        'active_bookings': active_bookings,

        'approved': approved,

        'cancelled': cancelled,

        'total_spent': total_spent,

        'reviews_count': reviews_count,

    }


    return render(

        request,

        'dashboard.html',

        context

    )

# CAR DETAIL

def car_detail(request, car_id):

    car = get_object_or_404(

        Car,

        id=car_id

    )


    return render(

        request,

        'car_detail.html',

        {

            'car': car

        }

    )



# CANCEL BOOKING

@login_required
def cancel_booking(

        request,

        booking_id

):


    booking = get_object_or_404(

        Booking,

        id=booking_id

    )


    booking.status = (

        'Cancelled'

    )


    booking.car.available = True

    booking.car.save()


    booking.save()


    messages.success(

        request,

        'Booking cancelled successfully ❌'

    )


    return redirect(

        'dashboard'

    )
    
@login_required
def add_review(request, car_id):

    car = get_object_or_404(

        Car,

        id=car_id

    )


    customer, created = Customer.objects.get_or_create(

        user=request.user

    )


    if request.method == 'POST':

        rating = request.POST[

            'rating'

        ]


        comment = request.POST[

            'comment'

        ]


        Review.objects.create(

            customer=customer,

            car=car,

            rating=rating,

            comment=comment

        )


        messages.success(

            request,

            'Review submitted successfully ⭐'

        )


        return redirect(

            'home'

        )


    return render(

        request,

        'add_review.html',

        {

            'car': car

        }

    )
    
def logout_user(request):

    logout(
        request
    )


    messages.success(

        request,

        'Logged out successfully 👋'

    )


    return redirect(

        'login'

    )
    
@login_required
def payment(request, booking_id):

    booking = get_object_or_404(

        Booking,

        id=booking_id

    )


    if request.method == 'POST':


        Payment.objects.create(

            booking=booking,

            amount=booking.total_price,

            payment_method='Card',

            status='Paid'

        )


        booking.status = 'Pending'

        booking.save()

        return redirect(

            'payment_success',

            booking.id

        )


    return render(

        request,

        'payment.html',

        {

            'booking': booking

        }


    )

@login_required
def payment_success(

    request,

    booking_id

):


    booking = get_object_or_404(

        Booking,

        id=booking_id

    )


    return render(

        request,

        'payment_success.html',

        {

            'booking': booking

        }

    )
    
@login_required
def invoice(
    
    request, 
    
    booking_id):

    booking = get_object_or_404(

        Booking,

        id=booking_id

    )


    response = HttpResponse(

        content_type='application/pdf'

    )

    response['Content-Disposition'] = (

        f'attachment; filename="invoice_{booking.id}.pdf"'

    )


    pdf = canvas.Canvas(

        response

    )


    pdf.setFont(

        "Helvetica-Bold",

        24

    )

    pdf.drawString(

        180,

        800,

        "Car Rental Invoice"

    )


    pdf.setFont(

        "Helvetica",

        14

    )

    pdf.drawString(

        70,

        740,

        f"Customer: {booking.customer.user.username}"

    )

    pdf.drawString(

        70,

        710,

        f"Car: {booking.car.name}"

    )

    pdf.drawString(

        70,

        680,

        f"Booking ID: {booking.id}"

    )

    pdf.drawString(

        70,

        650,

        f"Start Date: {booking.start_date}"

    )

    pdf.drawString(

        70,

        620,

        f"End Date: {booking.end_date}"

    )

    pdf.drawString(

        70,

        590,

        f"Total Paid: Rs {booking.total_price}"

    )


    pdf.line(

        50,

        560,

        550,

        560

    )


    pdf.drawString(

        70,

        520,

        "Thank you for choosing our rental service."

    )


    pdf.save()


    return response

@login_required
def profile(request):


    customer, created = Customer.objects.get_or_create(

        user=request.user

    )


    if request.method == 'POST':

        customer.phone = request.POST.get(

            'phone'

        )


        customer.city = request.POST.get(

            'city'

        )


        customer.license_number = request.POST.get(

            'license'

        )


        if 'image' in request.FILES:

            customer.profile_picture = request.FILES[

                'image'

            ]


        customer.save()


        messages.success(

            request,

            'Profile updated ✅'

        )


        return redirect(

            'profile'

        )


    bookings = Booking.objects.filter(

        customer=customer

    ).count()



    return render(

        request,

        'profile.html',

        {

            'customer': customer,

            'bookings': bookings

        }

    )


@login_required
def add_to_wishlist(

    request,

    car_id

):

    car = get_object_or_404(

        Car,

        id=car_id

    )


    item, created = Wishlist.objects.get_or_create(

        user=request.user,

        car=car

    )


    if not created:

        item.delete()


    return redirect(

        'home'

    )



@login_required
def wishlist(

    request

):

    items = Wishlist.objects.filter(

        user=request.user

    )


    return render(

        request,

        'wishlist.html',

        {

            'items': items

        }

    )