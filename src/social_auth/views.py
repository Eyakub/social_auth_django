from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount


def index(request):
    # social_info = SocialAccount.objects.filter(user=request.user)
    # fb_id = SocialAccount.objects.filter(
    #     user=request.user, provider='facebook')[0].uid
    # context = {
    #     'social_info': social_info,
    #     'fb_id': fb_id,
    # }
    # print(social_info.values('extra_data')[0])
    return render(request, "index.html")
