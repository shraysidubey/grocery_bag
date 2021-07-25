from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from gro_app.forms import UserForm, UserProfileForm, GroceryItemForm 
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from gro_app.models import UserProfile, GroceryItem

def get_context_dict(logged_in_user):
    context_dic = {}
    user_profile = UserProfile.objects.get(user=logged_in_user)
    grocery_list = GroceryItem.objects.filter(user_profile=user_profile).order_by('-date')
    context_dic['grocery_list'] = grocery_list
    context_dic['user_profile'] = user_profile
    return context_dic


def index(request):
    if request.user.is_authenticated():
        return render(request, 'gro_app/index.html', get_context_dict(request.user))
    else:
        return render(request, 'gro_app/login.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'gro_app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gro_app/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your gro_app account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'gro_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/gro_app/')

def grocery_details(request):
    context_dic = {}
    if request.user.is_authenticated():
        context_dic = get_context_dict(request.user)
        if request.method == 'POST':
            user_profile = UserProfile.objects.get(user=request.user)
            form = GroceryItemForm(request.POST)
            if form.is_valid():
                grocery_item_object = form.save(commit=False)
                grocery_item_object.user_profile = user_profile
                grocery_item_object.save()
                return HttpResponseRedirect('/gro_app/')
                return render(request, 'gro_app/index.html',context_dic)
            else:
                print(form.errors) 

        form = GroceryItemForm()
        context_dic['form'] = form
        return render(request, 'gro_app/grocery_item.html', context_dic)
    else:
        return render(request, 'gro_app/login.html')
