from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadModelForm
from .models import Lead
from agents.mixins import OrganizerAndLoginRequiredMixin

"""
Class based views
"""


class LeadListView(LoginRequiredMixin, generic.ListView):
    """
    Lead list view
    """
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)

        return queryset


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Lead detail view
    """
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)

        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
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


class LeadUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    """
    Lead update view
    """
    template_name = "leads/lead_update.html"
    context_object_name = "lead"
    form_class = LeadModelForm

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        redirect_url = reverse("leads:lead-list") + str(self.object.pk)
        return redirect_url

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)


class LeadDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    """
    Lead delete view
    """
    template_name = "leads/lead_delete.html"

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("leads:lead-list")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)
