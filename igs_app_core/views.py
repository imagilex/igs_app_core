from django.shortcuts import render


def hello(request):
    return render(request, "igs_app_core/hello.html", {"mensaje": "Hola desde la app reusable igs_app_core"})
