from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student, Track
# Create your views here.
def home(request):
    all_students = Student.objects.all()
    context = {'student_list': all_students}
    return render(request, 'djapp/home.html', context)

def show(request, st_id):
    st = Student.objects.get(id=st_id)
    context = {'st': st}
    return render(request, 'djapp/show.html', context)
    
def del_St(request, st_id):
    st = Student.objects.get(id = st_id)
    st.delete()
    return redirect('home')