from django.shortcuts import render
from .forms import TrainingForm  # à créer ensuite

def index(request):
    results = None
    if request.method == 'POST':
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            # Traitement du fichier + entraînement du modèle (à faire)
            pass
    else:
        form = TrainingForm()

    return render(request, 'trainer/index.html', {'form': form, 'results': results})
