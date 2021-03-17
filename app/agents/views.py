from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganizerAndLoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    """
    Agent list view
    """
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        request_user_org = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_org)


class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    """
    Agent create view
    """
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("agents:agent-list")


class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    """
    Agent update view
    """
    template_name = "agents/agent_update.html"
    queryset = Agent.objects.all()
    context_object_name = "agent"
    form_class = AgentModelForm

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        redirect_url = reverse("agents:agent-list") + str(self.object.pk)
        return redirect_url


class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    """
    Agent detail view
    """
    template_name = "agents/agent_detail.html"

    def get_queryset(self):
        request_user_org = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_org)


class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    """
    Agent delete view
    """
    template_name = "agents/agent_delete.html"

    def get_success_url(self):
        """
        Success URL
        :return:
        """
        return reverse("agents:agent-list")

    def get_queryset(self):
        request_user_org = self.request.user.userprofile
        return Agent.objects.filter(organization=request_user_org)