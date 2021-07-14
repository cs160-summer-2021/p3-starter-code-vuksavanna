from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')
def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')
def demo(request):
    return render(request, 'coloring/demo.html')
def work(request):
    return render(request, 'coloring/work.html')
def gallery(request):
    return render(request, 'coloring/gallery.html')
def explore(request):
    return render(request, 'coloring/explore.html')
