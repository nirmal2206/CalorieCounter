from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from nutrition.models import NutritionFactsLabel, ConsumedCalorie
from datetime import date
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
        if ConsumedCalorie.objects.filter(date=date.today()).count() == 0 :
            ConsumedCalorie.objects.create(user=username, date=date.today())
        consumed_calorie = ConsumedCalorie.objects.filter(user=username).order_by('-date')[:6]

        return render(request, 'index.html', {'consumed_calorie':consumed_calorie,})
    else:
        return redirect('accounts:login')

def foodList(request):
    if request.user.is_authenticated:
        nfl = NutritionFactsLabel.objects.order_by('food_name')
        return render(request, 'nutrition/food_list.html', {'nfl':nfl})
    else:
        return redirect('accounts:login')

def add(request, id):
    if request.user.is_authenticated:
        food = get_object_or_404(NutritionFactsLabel, id=id)
        if request.method == 'POST':
            serving = request.POST.get('serving')
            if not serving.isnumeric() and int(serving) < 0 :
                messages.warning(request, 'Invalid Serving size')
                return render(request, 'nutrition/add.html', {'food':food})
            calorie = round(float(serving) * (food.calories / food.serving_size))
            username = request.user.get_username()
            user_calorie = get_object_or_404(ConsumedCalorie, user=username, date=date.today())
            user_calorie.total_calorie += calorie
            user_calorie.save()
            messages.success(request, 'Added successfully')
            return redirect('mainapp:food_list')

        return render(request, 'nutrition/add.html', {'food':food})
    else:
        return redirect('accounts:login')

def remove(request, id):
    if request.user.is_authenticated:
        food = get_object_or_404(NutritionFactsLabel, id=id)
        if request.method == 'POST':
            serving = request.POST.get('serving')
            if not serving.isnumeric() and int(serving) < 0 :
                messages.warning(request, 'Invalid Serving size')
                return render(request, 'nutrition/add.html', {'food':food})
            calorie = round(float(serving) * (food.calories / food.serving_size))
            username = request.user.get_username()
            user_calorie = get_object_or_404(ConsumedCalorie, user=username, date=date.today())
            user_calorie.total_calorie -= calorie
            user_calorie.save()
            messages.success(request, 'Removed successfully')
            return redirect('mainapp:food_list')

        return render(request, 'nutrition/remove.html', {'food':food})
    else:
        return redirect('accounts:login')

def resetCalorie(request):
    username = request.user.get_username()
    data = ConsumedCalorie.objects.get(user=username, date=date.today())
    data.total_calorie = 0
    data.save()
    messages.success(request, 'Reset Success')
    return redirect('mainapp:index')