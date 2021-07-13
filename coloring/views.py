from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')
def demo(request):
    return render(request, 'coloring/demo.html')
def work(request):
    return render(request, 'coloring/work.html')
