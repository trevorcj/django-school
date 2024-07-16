from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import *
from .forms import  *
import logging
logger = logging.getLogger(__name__)
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, get_object_or_404
from django.db.models import Count


# def index(request):
#     if request.method == 'POST':
#         form = CourseRegistrationForm(request.POST)
#         if form.is_valid():
#             # Get cleaned data from the form
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             course = form.cleaned_data['course']

#             # Check if a Participant with the same name already exists
#             if Participant.objects.filter(name=name).exists():
#                 messages.error(request, 'A participant with this name already exists.')
#             else:
#                 # Create a new Participant object and save it
#                 participant = Participant(name=name, email=email, course=course)
#                 participant.save()
#                 messages.success(request, 'You have successful registered for the course')
#                 return redirect('index')
#         else:
#             messages.error(request, 'There was an error with yobur form submission. Please correct the errors in your Resgistraction form')
#     else:
#         form = CourseRegistrationForm()
    
#     aboutcontent = AboutContent.objects.first()
#     festurecontent = FeatureContent.objects.first()
#     intructor = Instructors.objects.all()
#     course = ReleaseCoure.objects.all()
#     testslider = testimonialSlider.objects.all()
#     testimonial = Testimonial.objects.first()
#     location = OurLocation.objects.first()
    
#     context = {
#         'aboutcontent': aboutcontent,
#         'festurecontent': festurecontent,
#         'intructor': intructor,
#         'course': course,
#         'form': form,
#         'testimonial': testimonial,
#         'location': location,
#         'testslider': testslider,
#     }
#     return render(request, 'index.html', context)


def index(request):
    course_form = CourseRegistrationForm()
    contact_form = ContactForm()

    if request.method == 'POST':
        if 'register_course' in request.POST:
            course_form = CourseRegistrationForm(request.POST)
            if course_form.is_valid():
                name = course_form.cleaned_data['name']
                email = course_form.cleaned_data['email']
                course = course_form.cleaned_data['course']
                
                if Participant.objects.filter(email=email).exists():
                    messages.error(request, 'A participant with this email already exists.')
                else:
                    participant = Participant(name=name, email=email, course=course)
                    participant.save()
                    messages.success(request, 'You have successfully registered for the course.')
                    return redirect('index')
            else:
                messages.error(request, 'A participant with this email already exists.')

        elif 'send_message' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                subject = contact_form.cleaned_data['subject']
                message = contact_form.cleaned_data['message']

                contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
                contact_message.save()
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('index')
            else:
                messages.error(request, 'There was an error with your contact form submission.')

        elif 'newsletter_subscribe' in request.POST:
            email = request.POST.get('email', '').strip()
            try:
                validate_email(email)
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already subscribed.')
                else:
                    NewsletterSubscription.objects.create(email=email)
                    messages.success(request, 'You have successfully subscribed to the newsletter!')
                return redirect('index')
            except ValidationError:
                messages.error(request, 'Please enter a valid email address.')

    aboutcontent = AboutContent.objects.first()
    festurecontent = FeatureContent.objects.first()
    intructor = Instructors.objects.all()
    course = ReleaseCoure.objects.all()
    testslider = testimonialSlider.objects.all()
    testimonial = Testimonial.objects.first()
    location = OurLocation.objects.first()

    context = {
        'aboutcontent': aboutcontent,
        'festurecontent': festurecontent,
        'intructor': intructor,
        'course': course,
        'course_form': course_form,
        'contact_form': contact_form,
        'testimonial': testimonial,
        'location': location,
        'testslider': testslider,
    }
    return render(request, 'index.html', context)



def about(request):
    aboutcontent = AboutContent.objects.first()
    festurecontent = FeatureContent.objects.first()
    context = {
        'aboutcontent': aboutcontent,
        'festurecontent': festurecontent,
    }
    return render(request, 'about.html', context )

def courses(request):
    course = ReleaseCoure.objects.all()
    context = {
        'course':course,
    }
    return render(request, 'courses.html', context )


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save to database
            contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
            contact_message.save()

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            # Add an error message
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()
    
    location = OurLocation.objects.first()
    
    context = {
        'form': form,
        'location': location,
    }

    return render(request, 'contact.html', context)


def detail(request):
    context = {}
    return render(request, 'detail.html', context )

def feature(request):
    festurecontent = FeatureContent.objects.first()
    context = {
        'festurecontent': festurecontent,
    }
    return render(request, 'feature.html', context )

def joinus(request):
    course = ReleaseCoure.objects.all()
    context = {
        'course': course,
    }
    return render(request, 'joinus.html', context )

def team(request):
    intructor = Instructors.objects.all()
    context = {
        'intructor': intructor,
    }
    return render(request, 'team.html', context )

def testimonial(request):
    testslider = testimonialSlider.objects.all()
    testimonial = Testimonial.objects.first()
    context = {
        'testslider': testslider,
        'testimonial': testimonial,
    }
    return render(request, 'testimonial.html', context )


def detail(request, course_id):
    categories_with_count = (
        ReleaseCoure.objects
        .values('name')
        .annotate(participant_count=Count('participant'))
    )
    related = ReleaseCoure.objects.all()
    course = get_object_or_404(ReleaseCoure, pk=course_id) 
    context = {
        'course': course,
        'related': related,
        'categories_with_count': categories_with_count,
        }
    return render(request, 'detail.html', context)


def search(request):

    categories_with_count = (
        ReleaseCoure.objects
        .values('name')
        .annotate(participant_count=Count('participant'))
    )
    related = ReleaseCoure.objects.all()
    query = request.GET.get('query', '')
    results = ReleaseCoure.objects.filter(name__icontains=query) if query else []
    context = {
        'query': query,
        'results': results,
        'related': related,
        'categories_with_count': categories_with_count,
    }
    return render(request, 'search.html', context)


def joinus(request):
    course_form = CourseRegistrationForm()
    contact_form = ContactForm()

    if request.method == 'POST':
        if 'register_course' in request.POST:
            course_form = CourseRegistrationForm(request.POST)
            if course_form.is_valid():
                name = course_form.cleaned_data['name']
                email = course_form.cleaned_data['email']
                course = course_form.cleaned_data['course']
                
                if Participant.objects.filter(email=email).exists():
                    messages.error(request, 'A participant with this email already exists.')
                else:
                    participant = Participant(name=name, email=email, course=course)
                    participant.save()
                    messages.success(request, 'You have successfully registered for the course.')
                    return redirect('index')
            else:
                messages.error(request, 'A participant with this email already exists.')

        elif 'send_message' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                subject = contact_form.cleaned_data['subject']
                message = contact_form.cleaned_data['message']

                contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
                contact_message.save()
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('index')
            else:
                messages.error(request, 'There was an error with your contact form submission.')

        elif 'newsletter_subscribe' in request.POST:
            email = request.POST.get('email', '').strip()
            try:
                validate_email(email)
                if NewsletterSubscription.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already subscribed.')
                else:
                    NewsletterSubscription.objects.create(email=email)
                    messages.success(request, 'You have successfully subscribed to the newsletter!')
                return redirect('index')
            except ValidationError:
                messages.error(request, 'Please enter a valid email address.')

    aboutcontent = AboutContent.objects.first()
    festurecontent = FeatureContent.objects.first()
    intructor = Instructors.objects.all()
    course = ReleaseCoure.objects.all()
    testslider = testimonialSlider.objects.all()
    testimonial = Testimonial.objects.first()
    location = OurLocation.objects.first()

    context = {
        'aboutcontent': aboutcontent,
        'festurecontent': festurecontent,
        'intructor': intructor,
        'course': course,
        'course_form': course_form,
        'contact_form': contact_form,
        'testimonial': testimonial,
        'location': location,
        'testslider': testslider,
    }
    return render(request, 'joinus.html', context)