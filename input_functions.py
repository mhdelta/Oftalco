from pyDatalog import pyDatalog
import facts
#//=================================================================================================
                    # BASE DEL CONOCIMIENTO
pyDatalog.create_terms('Enfermedad, enfermedad, yes, dolor, herencia, afectacion, otros_sintomas, color, edad, patologia, ubicacion_orzuelo, pus')
pyDatalog.create_terms('X, Y')
pyDatalog.create_terms('ask, que_dolor, Attr, Val, preguntar, que_color')
pyDatalog.create_terms('yes, no, sintoma')
+yes('')
+no('')

#ASK -> BUILDING EXPERT SYSTEMS IN PROLOG (book)

def verificar(S, entry):
  if(yes(S)):
    return str(yes(S))
  else:
    if(no(S)):
      return False
    else:
      if(ask(S, entry)==True):
        return str(yes(S))
      else:
        return False

def ask(pregunta, entry):
  # print(pregunta, "?")
  # respuesta = input()
  if ((entry == "yes") or (entry == 'y')):
    +yes(pregunta)
    return True 
  else:
    +no(pregunta)
    return False

def borrar_sintomas(sintoma):
  for i in sintoma(X):
    pyDatalog.retract_fact(str(sintoma),str(i[0]))    


########################   APLICACION DE CONSOLA   ################################
# def go():
#   end = 0
#   print("..Escriba y si su situacion coincide con la siguiente descripcion..")
#   for i in sintoma(X):
#     verificar(i[0])
#     end = end + 1
#     if(len_(enfermedad(X))>0):
#       print( "...Posiblemente padece de la\n", enfermedad(Enfermedad))
#       print( "----------")
#       return 0
#     elif end == 38:
#       print("...Nuestro sistema no encuentra una posible enfermedad ocular...")


