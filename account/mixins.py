from random import randint
import uuid
from django.contrib.auth.hashers import make_password


class ValidateFormMixin():
    def form_valid(self, form):
        self.message = form.save(commit=False)
        self.message.status = "r"
        if self.message.email == "None" or self.message.email == None:
            self.message.email = ""
        self.message.save()
        return super().form_valid(form)


class ValidFormMixin():
    def get_initial(self):
        initial = super(ValidFormMixin, self).get_initial()
        global password_unChange
        password_unChange = self.object.password
        initial["password"] = self.object.pass_per_save
        return initial

    def form_valid(self, form):
        cleend_form = form
        password = cleend_form.cleaned_data.get("password")
        pass_per_save = cleend_form.cleaned_data.get("pass_per_save")

        self.user = form.save(commit=False)
        if pass_per_save != password:
            self.user.pass_per_save = password
            self.user.password = make_password(password)
        else:
            self.user.password = password_unChange
        self.user.save()
        return super(ValidFormMixin, self).form_valid(form)


class ValidFormCreateMixin():
    def generate_ranint(self):
        return randint(100000, 999999)

    def form_valid(self, form):
        cleend_form = form
        password = cleend_form.cleaned_data.get("password")
        self.user = form.save(commit=False)
        self.user.pass_per_save = password
        self.user.password = make_password(password)
        self.user.custom_user_id = str(uuid.uuid4())[:11:-1]
        self.user.code_send = self.generate_ranint()
        self.user.save()
        return super(ValidFormCreateMixin, self).form_valid(form)
