from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView
from .models import *

# Create your views here.
class ProjectCreationView(CreateView):
    form_class =ProjectCreationForm
    model = Project
    template_name = 'project/create_project.html'
    success_url = '/user/managerpage/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'project_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'project/create_project.html'
    success_url = '/user/managerpage/'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project_detail'
    
    def get(self, request, *args, **kwargs):
        team = ProjectTeam.objects.filter(Project_id=self.kwargs['pk'])
        module = ProjectModule.objects.filter(project_id=self.kwargs['pk'])
        return render(request, self.template_name, {'project_detail': self.get_object(),'team':team, 'module':module})   
    
class ProjectDeleteView(DeleteView):
    model = Project
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/project/list_project/'    


class Create_Project_team(CreateView):
    form_class =ProjectTeamCreationForm
    template_name = 'project/project_team_create.html'
    success_url = '/project/list_project_team'

class ProjectTeamListView(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'project_team_list'
    
class ProjectTeamByProject(ListView):
    model = ProjectTeam
    template_name = 'project/project_team_list.html'
    context_object_name = 'list_project_team'
    
    def get_queryset(self):
        return super().get_queryset().filter(Project_id=self.kwargs['pk'])    


class CreateProjectModule(CreateView):
    model = ProjectModule
    form_class = CreateProjectModuleForm
    template_name = 'project/project_module_create.html'
    success_url = '/project/list_project_module/'

    def get(self, request , *args: str, **kwargs):
        # print(self.kwargs['pk'])
        return super().get(request, *args, **kwargs)


class ProjectModuleListByProject(ListView):
    model = ProjectModule
    template_name = 'project/project_module_list.html'
    context_object_name = 'project_module_list'

    def get_queryset(self):
        return super().get_queryset().filter(project_id=self.kwargs['pk'])
    

class ProjectModuleList(ListView):
    model = ProjectModule
    template_name = 'project/project_module_list.html'
    context_object_name = 'project_module_list'

    # def get_queryset(self):
    #     return super().get_queryset().filter(project_id=self.kwargs['pk'])
    


    
    
    
    
        