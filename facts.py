from pyDatalog import pyDatalog
pyDatalog.create_terms('enfermedad, vision, dolor, herencia, afectacion, otros_sintomas, color, edad, patologia, ubicacion_orzuelo, pus')
pyDatalog.create_terms('X, Y')
pyDatalog.create_terms('ask, que_dolor, Attr, Val, preguntar, que_color')
pyDatalog.create_terms('yes, no, sintoma')

+sintoma('Presenta dolores de cabeza')
+sintoma('Presenta dolor en la zona afectada')
+sintoma('No presenta dolor')
+sintoma('presenta ardor en la zona afectada')
# 
+sintoma('su vision es borrosa en general')
+sintoma('su vision es borrosa al ver objetos lejanos')
+sintoma('su vision es borrosa al ver objetos cercanos')
+sintoma('ve doble')
+sintoma('Presenta sensibilidad a la luz')
+sintoma('Se le dificulta ver de noche')
# 
+sintoma('Tiene familiares que padezcan diabetes')
+sintoma('Tiene familiares que padezcan miopia')
# 
+sintoma('Presenta fatiga visual')
+sintoma('ha tenido alguna herida en el ojo recientemente')
+sintoma('Tiene los ojos rojos')
+sintoma('Tiene la sensacion de tener un objeto en el ojo')
+sintoma('La zona afectada esta hinchada')
+sintoma('Tiene picazon en la zona afectada')
+sintoma('Presenta lagrimeo')
# 
+sintoma('De la zona afectada sale pus amarillo')
+sintoma('De la zona afectada sale pus verde')
+sintoma('Tiene pus en la protuberancia')
# 
+sintoma('se le dificulta ver los colores y el brillo')
+sintoma('Se le dificulta diferenciar el azul del morado')
+sintoma('Es incapaz de diferenciar el rojo y el verde')
+sintoma('Es incapaz de diferenciar el azul y el amarillo')
+sintoma('Percibe resplandor y luces anormales')
+sintoma('ve los colores destenidos')
# 
+sintoma('Padece diabetes')
+sintoma('Padece blefaritis')
+sintoma('Padece dermatitis')

+ubicacion_orzuelo('en_base_pestana')
+ubicacion_orzuelo('en_interior_parpado')
# 
+sintoma('Tiene una protuberancia roja en el ojo')
+sintoma('Esta expuesto a radiacion constantemente')
+sintoma('Esta expuesto a rayos ultravioletas constantemente')
+sintoma('La zona afectada es sensible al tacto')
# 
+sintoma('Es mayor de 30 anios')
+sintoma('Es menor de 30 anios')
+sintoma('Es mayor de 60 anios')

enfermedad('astigmatismo') <= yes('Presenta dolores de cabeza') &\
                              yes('su vision es borrosa en general') &\
                              yes('Se le dificulta ver de noche') &\
                              yes('Presenta fatiga visual')                              

enfermedad('miopia') <= yes('Presenta dolores de cabeza') &\
                        yes('su vision es borrosa al ver objetos lejanos') &\
                              yes('Presenta fatiga visual') &\
                              yes('Tiene familiares que padezcan diabetes') &\
                              yes('Tiene familiares que padezcan miopia')

enfermedad('hipermetropia') <= yes('Es mayor de 30 anios') &\
                               yes('su vision es borrosa al ver objetos lejanos') &\
                               yes('su vision es borrosa al ver objetos cercanos')

enfermedad('hipermetropia') <= yes('Es menor de 30 anios') & \
                               yes('su vision es borrosa al ver objetos lejanos')

enfermedad ('conjuntivitis_infecciosa') <= yes('Presenta sensibilidad a la luz') & \
                                           yes('presenta ardor en la zona afectada') & \
                                           yes('Tiene los ojos rojos') & \
                                           yes('Presenta lagrimeo') & \
                                           yes('Tiene la sensacion de tener un objeto en el ojo')& \
                                           yes('De la zona afectada sale pus amarillo')

enfermedad ('conjuntivitis_infecciosa') <= yes('Presenta sensibilidad a la luz') & \
                                           yes('presenta ardor en la zona afectada') & \
                                           yes('Tiene los ojos rojos') & \
                                           yes('Presenta lagrimeo') & \
                                           yes('Tiene la sensacion de tener un objeto en el ojo')& \
                                           yes('De la zona afectada sale pus verde')

enfermedad('conjuntivitis_alergica') <= yes('Presenta sensibilidad a la luz') & \
                                        yes('presenta ardor en la zona afectada') & \
                                        yes('Tiene los ojos rojos')  & \
                                        yes('Tiene la sensacion de tener un objeto en el ojo') &\
                                        ~yes('De la zona afectada sale pus amarillo') &\
                                        ~yes('De la zona afectada sale pus verde') 


enfermedad ('cataratas') <= yes('su vision es borrosa en general') & \
                            yes('Se le dificulta ver de noche') &\
                            yes('ve doble') &\
                            yes('Es incapaz de diferenciar el rojo y el verde') & \
                            yes('ve los colores destenidos')

enfermedad('cataratas') <=    yes('Es mayor de 60 anios') &\
                            yes('Padece diabetes')

enfermedad('cataratas') <=  yes('Es mayor de 60 anios') &\
                            yes('ha tenido alguna herida en el ojo recientemente')

enfermedad('cataratas') <=  yes('Es mayor de 60 anios') &\
                            yes('Esta expuesto a radiacion constantemente')

enfermedad('cataratas') <=  yes('Es mayor de 60 anios') &\
                            yes('Esta expuesto a rayos ultravioletas constantemente')
                                                      
enfermedad ('orzuelo') <=  yes('protuberancia_roja') & \
                           yes('Presenta dolor en la zona afectada') &\
                           yes('La zona afectada esta hinchada') & \
                           yes('Tiene picazon en la zona afectada') &\
                           yes('Presenta lagrimeo') & \
                           yes('Tiene pus en la protuberancia') or \
                           yes('Presenta sensibilidad a la luz') or\
                           yes('Tiene la sensacion de tener un objeto en el ojo')

enfermedad('chalizion') <= yes('Tiene una protuberancia roja en el ojo') & \
                                         yes('No presenta dolor')

enfermedad('chalizion') <=  yes('La zona afectada es sensible al tacto') & \
                                          yes('su vision es borrosa en general') & \
                                          yes('Padece diabetes')

enfermedad('chalizion') <=  yes('La zona afectada es sensible al tacto') & \
                            yes('su vision es borrosa en general') & \
                            yes('Padece blefaritis')

enfermedad('chalizion') <=  yes('La zona afectada es sensible al tacto') & \
                            yes('su vision es borrosa en general') & \
                            yes('Padece dermatitis')

enfermedad('presbicia') <= yes('su vision es borrosa al ver objetos cercanos') & \
                                         yes('Presenta fatiga visual') & \
                                         yes('Presenta dolores de cabeza')

enfermedad('daltonismo') <= yes('se le dificulta ver los colores y el brillo')

enfermedad('daltonismo') <= yes('Se le dificulta diferenciar el azul del morado')

enfermedad('daltonismo') <= yes('Es incapaz de diferenciar el rojo y el verde')

enfermedad('daltonismo') <= yes('Es incapaz de diferenciar el azul y el amarillo')