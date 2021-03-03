from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                    ListView,DetailView,
                                    CreateView,UpdateView,
                                    DeleteView)
from django.http import HttpResponse
from .models import School,Student
from django.urls import reverse_lazy
# Create your views here.

class Index(TemplateView):
    template_name = 'cbv_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["showMe"] = "This is my first CBV trial"
        return context

class SchoolList(ListView):
    context_object_name = 'schools'
    model = School

class SchoolDetail(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'cbv_app/school_details.html'

class InsertRecs(CreateView):
    fields = ('name','address','founded','hod')
    model = School

class UpdateRecs(UpdateView):
    fields = ('name','address','hod')
    model = School

class DeleteRecs(DeleteView):
    model = School
    success_url = reverse_lazy('list')
