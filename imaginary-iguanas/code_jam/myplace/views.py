from typing import Union
from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect

from users.models import Profile
from myplace.forms import ProfileCommentForm


def user(request, username_or_id: Union[int, str]):
    try:
        profile = _get_profile(username_or_id)
    except Profile.DoesNotExist:
        messages.error(request, 'That user profile does not exist.')
        return render(request, 'users/home.html')

    if request.method == 'POST':
        return add_profile_comment(request, profile)
    else:
        context = {
            'profile': {
                'username': profile.user.username,
                'is_online': profile.is_online,
                'last_login': profile.user.last_login,
                'image': profile.image.url,
                'gender': profile.get_gender_display(),
                'country': profile.get_country_display(),
                'city': profile.city,
                'years_old': (date.today() - profile.date_of_birth).days // 365,
                'audio_track': profile.audio_track
            },
            'title': profile,
            'custom_css': profile.profile_css,
            'profile_comments': profile.comments.all(),
            'new_comment_form': ProfileCommentForm()
        }
        return render(request, 'myplace/profile.html', context)


def _get_profile(username_or_id: Union[int, str]) -> Profile:
    """
    Tries to get Profile model object based on user id or username.

    :return: Profile object
    """
    if isinstance(username_or_id, int):
        return Profile.objects.get(id=username_or_id)
    else:
        return Profile.objects.get(user__username=username_or_id)


def add_profile_comment(request, profile: Profile):
    comment_form = ProfileCommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user_profile = profile
        comment.author = request.user.profile
        comment.save()

        messages.success(request, 'Comment added.')
        return redirect(request.build_absolute_uri())
    else:
        messages.error(request, 'Comment is invalid-')
        return redirect(request.build_absolute_uri())
