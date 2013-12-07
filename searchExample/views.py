# Create your views here.
import json

from searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from searchExample.forms import NotesSearchForm, UserForm, UserProfileForm, SaveThisSearchForm
from django.shortcuts import *


#from searchExample.query import NotesQuery
import urllib
from urllib import urlparse
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail


def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    all_notes = Note.objects.all().order_by('-id')[:3]
    context = {
        'notes': notes,
        'all_notes': all_notes,
    }
    #return render_to_response('notes.html', {'notes': notes})
    return render(request, "searchExample/notes.html", context)

def note(request, pk):
    #this isn't right
    note = get_object_or_404(Note, id=pk)
    #all_notes = Note.objects.all()
    notesegment = get_object_or_404(NoteSegment, id=pk)
    all_segments = list(note.notesegment_set.all())
    #all_segments = NoteSegment.objects.all()
    
    
    
    pageURL = request.get_full_path()
    urlData = urlparse(pageURL)
    theQuery = urlData.query.strip('=')

    context = {
        'tempvar': theQuery,
        'note': note,
        'notesegment': notesegment,
        'all_segments': all_segments,
    }
    return render(request, "searchExample/note.html", context)

def archive(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    all_notes_rev = Note.objects.all().order_by('-id')
    context = {
        'notes': notes,
        'all_notes_rev': all_notes_rev,
    }
    return render(request, "searchExample/archive.html", context)

#def note_list(request, pk):
#    note = get_object_or_404(Note, id=pk)
#    all_notes = Note.objects.all()
#    return render(request, "../haystackExample/templates/base.html", {'all_notes': all_notes})

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
                #profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'searchExample/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                
                #send_mail('Abandon Ship', 'Hope you found a lifeboat...', 'admin@capitolhound.com',
                #[user.email])
                
                msg = EmailMultiAlternatives(
                subject="Capitol Hound Alert",
                body="This is a test email for the Capitol Hound alert system",
                from_email="Capitol Hound Support <support@capitolhound.com>",
                to=[user.email]
                #headers={'Reply-To': "Service <support@example.com>"} # optional extra headers
                )
                msg.attach_alternative("<p>This is a test email for the <b>Capitol Hound</b> alert system.</p>", "text/html")
                
                #Send it:
                msg.send()
                
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('searchExample/login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Like before, obtain the request's context.
    context = RequestContext(request)

    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def edit_profile(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    #registered = True

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        #user_form = UserForm(data=request.POST)
        #profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            #registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'searchExample/register.html',
            {'user_form': user_form, 'profile_form': profile_form},
            context)

@login_required
def topics(request):
    context = RequestContext(request)
    
    #search_id = get_object_or_404(User, id=pk)
    
    if request.method == 'POST':
        
        #will save 'key' to topics if it is a string I've made. Somehow not getting theQuery
 
        user = request.user
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
        
                #profile = request.user.get_profile()
        
                #search_form = SaveThisSearchForm(data=request.POST)
                search_form = SaveThisSearchForm(request.POST)
                #saved_searches = 'something!'

                if(search_form.is_valid()):
                
                    ### Doesn't seem to be executing this, but it isn't returning the 'else' HttpResponse ###
                    saved_searches = request.POST['saved_searches']
                    search = search_form.save(commit=False)
                    search.user = request.user
                    search.save()
                    #SaveThisSearch.save()
                    #saved_searches = form.cleaned_data['topics']
                    return HttpResponse(json.dumps({'saved_searches': saved_searches}))
                
                else:
                    print search_form.errors
                    return HttpResponse("This form is broken.")
                
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('searchExample/email_success.html', {}, context)
    
    return render_to_response('searchExample/note.html', {}, context)


### EMAIL ###
#NOT DOING ANYTHING RIGHT NOW
@login_required
def email_test(request):
    msg = EmailMultiAlternatives(
    subject="Capitol Hound Alert",
    body="This is a test email for the Capitol Hound alert system",
    from_email="Capitol Hound Support <support@capitolhound.com>",
    to=[user.email]
    #headers={'Reply-To': "Service <support@example.com>"} # optional extra headers
    )
    msg.attach_alternative("<p>This is a test email for the <b>Capitol Hound</b> alert system.</p>", "text/html")
                
    #Send it:
    msg.send()