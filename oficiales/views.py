from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .mytools import tools
from .forms import ReporteForm


@login_required
def homeOf(request):
    return render(request, "homeOf.html")

@login_required
def marcaOf(request):
    datos = {"dato1",  "datos2","dato3",  "datos4"}

    tools.mirar_db("contacts")
    print(datos)

    return render(request, 'marcaOf.html', {'datos': datos})

@login_required
def reportesOf(request):
    datos = ["array con los datos id.user para mostrar en el front"]

    return render(request, "reportesOf.html", {'datos' : datos} )

@login_required
def perfilOf(request):
    return render(request, "perfilOf.html")


@login_required
def crearReporte(request):
    if request.method == 'GET':
        return render(request, 'reportesOf.html', {
            'form': ReporteForm
        })
    else:
        try:
            form = ReporteForm(request.POST)
            reporte = form.save(commit=False)
            reporte.user = request.user
            reporte.save()
            return redirect('homeOf')
        except ValueError:
            return render(request, 'reportesOf.html', {
                'form': ReporteForm,
                'error': 'Verifique datos'
            })
