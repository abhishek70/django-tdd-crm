from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadModelForm
from .models import Lead

"""
Class based views
"""


class LeadListView(LoginRequiredMixin, generic.ListView):
    """
    Lead list view
    """
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Lead detail view
    """
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Lead create view
    """
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def form_valid(self, form):
        # TODO
        # 1. Send an email
        # 2. Add an event in event bus
        return super(LeadCreateView, self).form_valid(form)

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("leads:lead-list")


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
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


class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
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
