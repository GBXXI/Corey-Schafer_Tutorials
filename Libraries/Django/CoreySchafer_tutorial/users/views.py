# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Importing flash message. It is an easy way
                                     # to sent one time alerts to a template.

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm

# Creating our form.
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()  # Saving our user to our database.
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}.')
#             return redirect('blog-home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form':form})


# Creating our custom form, that has the email field
# def register(request):
# if request.method == 'POST':
# form = UserRegisterForm(request.POST)
#
# if form.is_valid():
# form.save()  # Saving our user to our database.
# username = form.cleaned_data.get('username')
# messages.success(request, f'Account created for {username}.')
# return redirect('blog-home')
# else:
# form = UserRegisterForm()
# return render(request, 'users/register.html', {'form':form})


# Redirecting to the login page, after user creation
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Saving our user to our database.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        update_UserForm = UserUpdateForm(request.POST, instance=request.user)
        update_ProfileForm = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if update_UserForm.is_valid() and update_ProfileForm.is_valid():
            update_UserForm.save()
            update_ProfileForm.save()

            messages.success(request, 'The Account has been Updated')
            return redirect('profile')
    else:
        update_UserForm = UserUpdateForm(instance=request.user)
        update_ProfileForm = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update_UserForm': update_UserForm,
        'update_ProfileForm': update_ProfileForm
    }

    return render(request, 'users/profile.html', context)
