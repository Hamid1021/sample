from django.shortcuts import render

from seo.models import Seo
from cantact.forms import CantactForm
from cantact.models import Message


def cantact_page(request):
    form = CantactForm(request.POST or None)
    seo_information = Seo.objects.all().filter(status=True).last()
    context = {
        "form": form,
        "seo": seo_information,
    }

    if form.is_valid():
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        if full_name == "":
            full_name = "بدون نام"
        if subject == "":
            subject = "بدون موضوع"
        
        try:
            Message.objects.create(full_name=full_name, email=email,
                                   message=message, subject=subject)
            context["message"] = "پیام شما ارسال گردید بعد از بررسی در صورت وارد کردن ایمیل با شما ارتباط برقرار خواهیم کرد"
        except:
            context["message_1"] = "پیام شما ارسال نگردید دوباره تلاش نمایید"
        context["form"] = CantactForm()

    return render(request, "contact.html", context)
