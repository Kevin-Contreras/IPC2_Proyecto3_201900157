from django.http import HttpResponse
from django.template import Template,Context 
def vista(request):
 Principal= open("C:/Users/kevin/Desktop/PROYECTO 3/Vista/Vista/Plantillas/index.html")
 temp = Template(Principal.read())
 Principal.close()
 ctx = Context()
 return HttpResponse(temp.render(ctx))
def archivo1(request):
  Principal= open("C:/Users/kevin/Desktop/PROYECTO 3/Vista/Vista/Plantillas/archivo.html")
  temp = Template(Principal.read())
  Principal.close()
  ctx = Context()
  return HttpResponse(temp.render(ctx))  

def archivo2(request):
  Principal= open("C:/Users/kevin/Desktop/PROYECTO 3/Vista/Vista/Plantillas/archivo.html")
  temp = Template(Principal.read())
  Principal.close()
  ctx = Context()
  
 
  
  return HttpResponse(temp.render(ctx))  
