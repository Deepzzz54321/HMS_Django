from django.shortcuts import redirect, render
from institute.models import Block, Student, Official
from students.models import Attendance, Outing
from django.http import HttpResponse
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def student_check(user):
    return user.is_authenticated and user.is_student

# Create your views here.

@user_passes_test(student_check)
def student_home(request):
    user = request.user
    user_details = Institutestd.objects.get(email_id=user.email)
    current = attendance.objects.get(regd_no_id=user_details.regd_no).dates
    dates = current.split(',')
    abse = len(list(filter(lambda x: (x.startswith('X')), dates)))
    pres = len(list(filter(lambda x: not (x.startswith('X')), dates)))
    complaints=list(user_details.complaints.filter(status="Registered")) + list(user_details.complaints.filter(status="Processing"))

    return render(request, 'students/student-home.html', {'user_details': user_details, 'pres':pres, 'abse':abse, 'complaints':complaints})

@user_passes_test(student_check)
def outing_app(request):
    if request.method == 'POST':
        fromDate = request.POST['fromDate']
        fromTime = request.POST['fromTime']
        toDate = request.POST['toDate']
        toTime = request.POST['toTime']
        purpose = request.POST['purpose']
        student = Institutestd.objects.get(email_id = request.user.email)
        parents_mobile = student.ph_phone

        print(fromDate, fromTime, toDate, toTime, purpose, parents_mobile)

        fromDateObj = datetime.datetime.strptime(fromDate, '%Y-%m-%d')
        toDateObj = datetime.datetime.strptime(toDate, '%Y-%m-%d')
        fromTimeObj = datetime.datetime.strptime(fromTime, '%H:%M')
        toTimeObj = datetime.datetime.strptime(toTime, '%H:%M')

        application = outing(
            regd_no= student,
            fromDate=fromDateObj,
            fromTime=fromTimeObj,
            toDate=toDateObj,
            toTime=toTimeObj,
            purpose=purpose,
            parent_mobile=parents_mobile
        )
        application.save()
        messages.success(request, 'Outing Application submitted successfully! Check Outing History for status')
        return redirect('students:outing_app')

    return render(request, 'students/OutingApp.html')


@user_passes_test(student_check)
def attendance_history(request):
    user_details = Institutestd.objects.get(email_id = request.user.email)
    current = attendance.objects.get(regd_no_id=reg_no).dates
    dates = current.split(',')
    abse = list(filter(lambda x: (x.startswith('X')), dates))
    pres = list(filter(lambda x: not (x.startswith('X')), dates))
    abse = list(map(lambda x: x.replace('X',''), abse))

    return render(request, 'students/attendance-history.html', {'user_details':user_details, 'pres':pres, 'abse':abse})


@user_passes_test(student_check)
def outing_history(request):
    user_details = Institutestd.objects.get(email_id = request.user.email)
    outing_details = outing.objects.filter(regd_no=user_details.regd_no)

    return render(request, 'students/outingHisto.html', {'user_details': user_details, 'outing_details':outing_details})

