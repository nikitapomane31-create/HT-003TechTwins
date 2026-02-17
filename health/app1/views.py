from django.shortcuts import render
from .models import SymptomCheck

from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm

def home(request):
    return render(request, 'home.html')

def medi(request):
    return render(request, 'medi.html')

def tips(request):
    return render(request, 'tips.html')



def em(request):
    return render(request, 'em.html')

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



def reminder(request):
    return render(request, 'reminder.html')




def mark_taken(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    medicine.is_taken = True
    medicine.save()
    return redirect('medicine_list')






from django.shortcuts import render
from django.http import JsonResponse
from .models import EmergencyAlert
import json

def emergency_page(request):
    return render(request, "emergency.html")


def save_sos(request):
    if request.method == "POST":
        data = json.loads(request.body)

        name = data.get("name")
        lat = data.get("latitude")
        lng = data.get("longitude")

        link = f"https://www.google.com/maps?q={lat},{lng}"

        EmergencyAlert.objects.create(
            name=name,
            latitude=lat,
            longitude=lng,
            location_link=link
        )

        return JsonResponse({"status": "success"})




from django.http import JsonResponse
import json
from .models import Medicine   # make sure this import exists

def set_reminder(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        time_str = data.get("time")

        medicine = Medicine.objects.get(id=id)
        medicine.reminder_time = time_str
        medicine.status = "Scheduled"
        medicine.save()

        return JsonResponse({"message": "Reminder set successfully"})
