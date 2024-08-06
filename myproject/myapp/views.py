from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import SignUpForm, StudentForm, SectionForm
from .models import Student
import pywhatkit
import logging
from django.contrib import messages

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def aboutus_view(request):
    return render(request, 'aboutus.html')

@login_required
def teacher_view(request):
    section = request.GET.get('section')
    students = Student.objects.all()
    if section:
        students = students.filter(section=section)

    if request.method == 'POST':
        attendance_data = {}
        for key, value in request.POST.items():
            if key.startswith('attendance_'):
                student_id = key.split('_')[1]
                attendance_data[student_id] = value
        
        absent_students = [student_id for student_id, status in attendance_data.items() if status == 'absent']
        
        # Pass absent student IDs to send_messages view
        request.session['absent_students'] = absent_students
        return redirect('send_messages')

    section_form = SectionForm()
    return render(request, 'teacher.html', {'section_form': section_form, 'students': students})

@login_required
def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_display', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'student.html', {'form': form})

@login_required
def student_display_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_display.html', {'student': student})

@login_required
def search_view(request):
    return render(request, 'search.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successfully!')
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def student_edit_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_display', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form})

@login_required
def student_delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_delete.html', {'student': student})

@login_required
def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

class SendWhatsAppMessagesView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        absent_students = request.session.get('absent_students', [])
        # Fetch student objects to get phone numbers
        students = Student.objects.filter(id__in=absent_students)
        return render(request, 'send_messages.html', {'students': students})

    def post(self, request):
        absent_students = request.session.get('absent_students', [])
        for student_id in absent_students:
            student = get_object_or_404(Student, id=student_id)
            phone_number = student.phone_number
            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone_number, 
                    "Welcome to ABCD school your kid is Absent today", 
                    wait_time=20, 
                    tab_close=True, 
                    close_time=5
                )
                logging.info(f"Message sent to {phone_number}")
            except Exception as e:
                logging.error(f"Failed to send message to {phone_number}: {e}")
        return redirect('success')

class SuccessView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'success.html')
    

    import logging

# Configure the logger
logger = logging.getLogger(__name__)

# Example usage in a view
def my_view(request):
    try:
        # Your code here
        logger.info("This is an info message")
    except Exception as e:
        logger.error(f"An error occurred: {e}")



from django.shortcuts import render, redirect

def set_session_view(request):
    # Set a session variable
    request.session['my_variable'] = 'Hello, World!'
    return redirect('get_session')

def get_session_view(request):
    # Get a session variable
    my_variable = request.session.get('my_variable', 'Default Value')
    return render(request, 'home.html', {'my_variable': my_variable})

def delete_session_view(request):
    # Delete a session variable
    if 'my_variable' in request.session:
        del request.session['my_variable']
    return redirect('get_session')

def flush_session_view(request):
    # Flush the entire session data
    request.session.flush()
    return redirect('get_session')


@login_required
def mark_absent_view(request):
    if request.method == 'POST':
        absent_students = []
        for key, value in request.POST.items():
            if value == 'absent':
                student_id = key.split('_')[1]
                absent_students.append(student_id)
        request.session['absent_students'] = absent_students
        return redirect('send_messages')

# @login_required
# def send_messages_view(request):
#     if request.method == 'POST':
#         absent_students = request.session.get('absent_students', [])
#         for student_id in absent_students:
#             student = get_object_or_404(Student, id=student_id)
#             phone_number = student.phone_number
#             try:
#                 pywhatkit.sendwhatmsg_instantly(
#                     phone_number, 
#                     "Welcome to ABCD School. Your kid is absent today.",
#                     wait_time=20, 
#                     tab_close=True, 
#                     close_time=5
#                 )
#                 logging.info(f"Message sent to {phone_number}")
#             except Exception as e:
#                 logging.error(f"Failed to send message to {phone_number}: {e}")
#         return redirect('success')
    
#     absent_students = request.session.get('absent_students', [])