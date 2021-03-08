from django.test import TestCase
from django.urls import reverse
from .models import Lead, Agent
from .forms import LeadModelForm
from http import HTTPStatus


class Leads(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Class method
        Create user and agent
        :return:
        """
        from django.contrib.auth import get_user_model
        # Create user
        cls.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        cls.user.save()
        # Create agent
        Agent.objects.create(user=cls.user)
        return super().setUpClass()

    def setUp(self) -> None:
        """
        Setup method
        :return:
        """
        # Get first agent
        self.agent = Agent.objects.first()
        # Create lead
        Lead.objects.create(first_name='lead', last_name='lead', age=20, agent=self.agent)
        super().setUp()

    # Views
    def test_lead_list_view(self):
        """
        Test lead list view
        :return:
        """
        response = self.client.get(reverse('leads:lead-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'leads/lead_list.html')

    def test_lead_create_view(self):
        """
        Test lead create view
        :return:
        """
        response = self.client.get(reverse('leads:lead-create'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'leads/lead_create.html')

    def test_lead_update_view(self):
        """
        Test lead update view
        :return:
        """
        lead = Lead.objects.first()
        url = reverse('leads:lead-update', args=(lead.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'leads/lead_update.html')

    def test_lead_create(self):
        """
        Test lead create
        :return:
        """
        response = self.client.post(reverse('leads:lead-create'), data={
            'first_name': 'create',
            'last_name': 'lead',
            'age': 40,
            'agent': Agent.objects.first()
        })
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_lead_detail_view(self):
        """
        Test lead detail view
        :return:
        """
        lead = Lead.objects.first()
        url = reverse('leads:lead-detail', args=(lead.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'leads/lead_detail.html')

    def test_lead_delete_view(self):
        """
        Test lead delete view
        :return:
        """
        lead = Lead.objects.first()
        url = reverse('leads:lead-delete', args=(lead.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'leads/lead_delete.html')

    # Forms
    def test_create_lead_form_invalid_data(self):
        """
        Test create lead form for invalid data
        :return:
        """
        form = LeadModelForm({})
        self.assertFalse(form.is_valid())

    def test_create_lead_form_valid_data(self):
        """
        Test create lead form for valid data
        :return:
        """
        form = LeadModelForm({
            'first_name': 'test',
            'last_name': 'lead',
            'age': 20,
            'agent': Agent.objects.first()
        })
        self.assertTrue(form.is_valid())
        lead = form.save()
        self.assertEqual(lead.first_name, 'test')
        self.assertEqual(lead.age, 20)
        self.assertEqual(lead.last_name, 'lead')
