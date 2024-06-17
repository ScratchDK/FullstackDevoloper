from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ClientsForm
from .models import Clients
from django.views.generic import UpdateView


@login_required
def create_client(request):
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manager = request.user
            instance.save()
            return render(request, "main/create.html", {"form": form})
    else:
        form = ClientsForm()
        return render(request, "main/create.html", {"form": form})


class UpdateClient(UpdateView):
    model = Clients
    template_name = "main/create.html"

    form_class = ClientsForm


@login_required
def show_clients(request):
    clients = Clients.objects.filter(manager=request.user)

    data = {
        "clients": clients,
    }
    return render(request, "main/main.html", context=data)