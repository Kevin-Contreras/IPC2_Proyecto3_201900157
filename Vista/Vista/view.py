from django.http import HttpResponse
from django.template import Template,Context 
from django.shortcuts import redirect

def vista(request):
 Principal= open("../Vista/Vista/Plantillas/index.html")
 temp = Template(Principal.read())
 Principal.close()
 ctx = Context()
 return HttpResponse(temp.render(ctx))
def archivo1(request):
  Principal= open("../Vista/Vista/Plantillas/archivo.html")
  temp = Template(Principal.read())
  Principal.close()
  ctx = Context()
  return HttpResponse(temp.render(ctx))  

def archivo2(request):

  xml=""
  archivo= open("../Vista/Vista/archivos/"+request.POST["CARGAR_ARCHIVO"],encoding="utf8")
  for linea in archivo.readlines():
    print(xml)
    xml = xml+linea +" "
  print(xml)
  return redirect("/")
def operaciones(request):
  Principal= open("../Vista/Vista/Plantillas/operaciones.html")
  temp = Template(Principal.read())
  Principal.close()
  ctx = Context()
  return HttpResponse(temp.render(ctx))  
def filtar(request):
  Principal= open("../Vista/Vista/Plantillas/filtrar.html")
  temp = Template(Principal.read())
  Principal.close()
  ctx = Context()
  return HttpResponse(temp.render(ctx))  
def filtar2(request):
  Principal= open("../Vista/Vista/Plantillas/filtro2.html")
  temp = Template(Principal.read())
  Principal.close()
  ctx = Context()
  return HttpResponse(temp.render(ctx))  