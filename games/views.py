# games/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Game
from .forms import GameForm

class GameListView(ListView):
    model = Game
    template_name = "games/game_list.html"
    context_object_name = "games"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

class GameDetailView(DetailView):
    model = Game
    template_name = "games/game_detail.html"
    context_object_name = "game"

class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = "games/game_form.html"
    # success_url opcional: si no se define, se usa get_absolute_url() del modelo

class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm
    template_name = "games/game_form.html"

class GameDeleteView(DeleteView):
    model = Game
    template_name = "games/game_confirm_delete.html"
    success_url = reverse_lazy("games:game-list")


# Create your views here.
