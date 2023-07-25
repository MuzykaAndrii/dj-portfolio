from django.forms import BaseModelFormSet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages


class FormSetView(LoginRequiredMixin, View):
    """
    A generic view for conveniently implementing pages with
    creation/editing inline form sets. To use this, you need
    to inherit this class and override the following class variables:

    Class Variables:
        related_field_name (str): The name of the related field on the user model.
                                  This field will be used to get the related object
                                  for the form set instance.

        FormSet (BaseModelFormSet): The form set class used for creating and editing
                                    the related objects. This should be a subclass of
                                    BaseModelFormSet.

        template_name (str): The name of the template to be used for rendering the
                             form set view.

        success_redirect (str): The URL where the user will be redirected after
                                successfully saving the form set data.
    """
    related_field_name: str = None
    FormSet: BaseModelFormSet = None
    template_name: str = None
    success_redirect: str = None

    def _get_related_field(self, request):
        return getattr(request.user, self.related_field_name)

    def get(self, request):
        related_field = self._get_related_field(request)
        form_set = self.FormSet(instance=related_field)

        return render(request, self.template_name, {'form_set': form_set})

    def post(self, request):
        related_field = self._get_related_field(request)
        form_set = self.FormSet(instance=related_field, data=request.POST, files=request.FILES)

        if not form_set.is_valid():
            from pprint import pprint
            pprint(form_set.errors)
            messages.error(request, "An error occurred. Please fill in the correct data.")
            return render(request, self.template_name, {'form_set': form_set})

        form_set.save()

        messages.success(request, "Data saved successfully.")
        return redirect(self.success_redirect)
