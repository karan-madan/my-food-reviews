from django.urls import path

from.import views

urlpatterns = [
    path('', views.home, name='food-home'),
    path('about/', views.about, name='food-about'),
    path('contactus/', views.contactus, name='food-contactus'),
    path('butterchicken/', views.butterchicken, name='food-butterchicken'),
    path('chickencurry/', views.chickencurry, name='food-chickencurry'),
    path('keema/', views.keema, name='food-keema'),
    path('shahipaneer/', views.shahipaneer, name='food-shahipaneer'),
    path('kadhaipaneer/', views.kadhaipaneer, name='food-kadhaipaneer'),
    path('masaladosa/', views.masaladosa, name='food-masaladosa'),
    path('pasta/', views.pasta, name='food-pasta'),
    path('burger/', views.burger, name='food-burger'),
    path('pizza/', views.pizza, name='food-pizza'),
    path('rolls/', views.rolls, name='food-rolls'),
    path('naanza/', views.naanza, name='food-naanza'),
    path('coffee/', views.coffee, name='food-coffee'),
    path('lassi/', views.lassi, name='food-lassi'),
    path('shawarma/', views.shawarma, name='food-shawarma'),
    path('biryani/', views.biryani, name='food-biryani'),
    path('roastedchicken/', views.roastedchicken, name='food-roastedchicken'),
    path('tandoorichicken/', views.tandoorichicken, name='food-tandoorichicken'),
    path('afghanichicken/', views.afghanichicken, name='food-afghanichicken'),
    path('paneertikka/', views.paneertikka, name='food-paneertikka'),
    path('mushroomtikka/', views.mushroomtikka, name='food-mushroomtikka'),



]
