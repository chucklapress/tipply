from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,CreateView,ListView
from django.http import HttpResponse
from app.models import EmployeeListing, Employee, WorkSkill, PointOfInterest, PeopleWeKnow, Book
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
from geoposition.forms import GeopositionField
#from django.shortcuts import render_to_response, RequestContext



# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class BusinessMapView(TemplateView):
    template_name = 'findus.html'

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            return render(request, "user_create_view.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create_view.html", {"form": form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class EmployeeListingCreateView(CreateView):
    model = EmployeeListing
    fields = ['applicant_name','applicant_image','applicant_email','applicant_phone','position_applying_for','post_resume_or_cover']
    success_url = '/'
    def upload_pic(request):
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = EmployeeListing.objects.get(pk=id)
            m.model_pic = form.cleaned_data['applicant_image']
            m.save()
            return HttpResponse('image upload success')
            return HttpResponseForbidden('allowed only via POST')



class ApplicantListView(ListView):
    model = EmployeeListing


class EmployeeListView(ListView):
    model = WorkSkill


class EmployeeWorkSkillCreateView(CreateView):
    model = WorkSkill
    fields = ['employee_number','employee_name','appearence','customer_skills','team_work','adhere_company_policies','accepts_coaching','self_starting']
    success_url = '/'



class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['employee_name','dob','address','telephone_number','federal_and_state_filling_status','department','start_date','end_date','recieved_employee_handbook','personel_notes']
    success_url = '/'

def poi_list(request):
    pois = PointOfInterest.objects.all()
    return render(request, 'poi_list.html', {'pois': pois})

def pwk_list(request):
    pwks = PeopleWeKnow.objects.all()
    return render(request, 'whoweknow.html', {'pwks': pwks})

class BookView(ListView):
    template_name = 'book_view.html'
    model = Book

    def get_queryset(self):
        return Book.objects.all()
