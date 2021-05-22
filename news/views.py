from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import LatestProblems
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_group_notification
import json


class ProblemsView(TemplateView):
    template_name = 'problems.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_problems'] = LatestProblems.objects.all()
        context['webpush'] = {'group': 'everyone'}
        return context 


