from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import LeadModelForm
from .models import Lead

"""
Class based views
"""


class LeadListView(generic.ListView):
    """
    Lead list view
    """
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    """
    Lead detail view
    """
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    """
    Lead create view
    """
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("leads:lead-list")


class LeadUpdateView(generic.UpdateView):
    """
    Lead update view
    """
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"
    form_class = LeadModelForm

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        redirect_url = reverse("leads:lead-list") + str(self.object.pk)
        return redirect_url


class LeadDeleteView(generic.DeleteView):
    """
    Lead delete view
    """
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("leads:lead-list")
