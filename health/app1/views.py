from django.shortcuts import render
from .models import SymptomCheck

from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm

def home(request):
    return render(request, 'home.html')

def medi(request):
    return render(request, 'medi.html')

<<<<<<< HEAD
def em(request):
    return render(request, 'em.html')
=======

from django.shortcuts import render
from .models import SymptomCheck

def symptom_checker(request):
    return render(request, 'symptom_checker.html')


def symptom_result(request):
    if request.method == "POST":

        name = request.POST.get("name")

        fever = request.POST.get("fever")
        cough = request.POST.get("cough")
        headache = request.POST.get("headache")
        breath = request.POST.get("breath")
        chest_pain = request.POST.get("chest_pain")

        score = 0

        # 🧠 AI Scoring Logic
        if fever:
            score += 2
        if cough:
            score += 2
        if headache:
            score += 1
        if breath:
            score += 4
        if chest_pain:
            score += 5

        # 🎯 Risk Detection
        if score <= 2:
            risk = "Low"
            color = "success"
        elif score <= 5:
            risk = "Medium"
            color = "warning"
        else:
            risk = "High"
            color = "danger"

        # Save to Database
        SymptomCheck.objects.create(
            name=name,
            fever=bool(fever),
            cough=bool(cough),
            headache=bool(headache),
            breath=bool(breath),
            chest_pain=bool(chest_pain),
            score=score,
            risk_level=risk
        )

        return render(request, "symptom_result.html", {
            "score": score,
            "risk": risk,
            "color": color
        })





def add_medicine(request):
    form = MedicineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('medicine_list')
    return render(request, 'add_medicine.html', {'form': form})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def delete_medicine(request, pk):
    med = get_object_or_404(Medicine, pk=pk)
    med.delete()
    return redirect('medicine_list')

def edit_medicine(request, pk):
    med = get_object_or_404(Medicine, pk=pk)
    form = MedicineForm(request.POST or None, instance=med)
    if form.is_valid():
        form.save()
        return redirect('medicine_list')
    return render(request, 'add_medicine.html', {'form': form})


<<<<<<< HEAD
def reminder(request):
    return render(request, 'reminder.html')
=======


send_mail(
    "Medicine Reminder",
    "Time to take your medicine",
    "yourgmail@gmail.com",
    ["patient@email.com"],
)


from twilio.rest import Client

client = Client("ACCOUNT_SID", "AUTH_TOKEN")

client.messages.create(
    body="Time to take your medicine",
    from_="+1234567890",
    to="+91XXXXXXXXXX"
)
>>>>>>> bbf10c96cd06c2fa2c5d30b5fef2c31c88cdf88a
>>>>>>> 3b027e2111f153399c5a39b87046fe9ca7475819
