##Where is my CNN looking at?

###Introduction
Media y desviación stándard de la muestra para casos y controles en dataset
Primeras pruebas 77f1, alrededor de 80%precision/recall. 
Buenos resultados pero no lógicos para radiólogo torácico. 
Decisión de buscar métodos de interpretabilidad.

###Hypotesis
1. Detectar regiones importantes mediante mapas de activación basados en los gradientes, GradCAM. 
1.1 Regiones demasiado grandes, la radiografía de tórax incluye muchas estructuras, los mapas de activación no eran concluyentes. 

2. Detectar detalles a nivel de pixeles mediante guided backpropagation.
2.1 Se registran las regiones que detectan las primeras capas de la red pero no parecen relevantes para la decisión.
2.2 No se observan diferencias en los mapas en las diferentes clases y experimentos.

3. Combinar los dos métodos para conseguir más detalle en las regiones que generan activación. 
3.1 GuidedBackpropagation
