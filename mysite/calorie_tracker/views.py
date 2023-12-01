from django.shortcuts import redirect, render
from .models import Consume, Food
# Create your views here.


def index(request):
    if request.method == 'POST':
        food_consumed = request.POST.get('food_consumed')
        if food_consumed == '0':
            return redirect('index')
        consumed = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consumed)
        consume.save()

        return redirect('index')

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    context = {"foods": foods, "consumed_food": consumed_food}
    return render(request, 'calorie_tracker/index.html', context)


def delete(request):
    user = request.user
    consumed_food = Consume.objects.filter(user=user)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('index')

    return render(request, 'calorie_tracker/delete.html')