# Práctica: Árbol de Decisión Simple con GitFlow

**Universidad Da Vinci de Guatemala**\
**Curso:** Cesar Sazo\
**Práctica:** Árbol de Decisión y Flujo GitFlow\
**Nombre:** Elder Donaldo Salazar Garrido\
**Carnet:** 202305764\
**Fecha de entrega:** 15/11/2025

## Objetivo General

Crear un programa en Python que genere datos aleatorios y los clasifique
usando un árbol de decisión sencillo, aplicando el flujo GitFlow para
llevar un control correcto de las versiones del proyecto.

## Objetivos Específicos

-   Hacer un script en Python que genere números al azar.\
-   Clasificarlos entre "Alto" o "Bajo" según un valor límite.\
-   Mostrar ejemplos, contar resultados y medir el tiempo de ejecución.\
-   Utilizar GitFlow para organizar las ramas del proyecto.\
-   Finalizar la práctica creando un tag de la versión final.

## Descripción del Árbol de Decisión

El árbol de decisión que utilicé es bastante simple. Solo tiene un nodo
que compara cada número con un umbral de 50: - Mayor o igual a 50 →
Alto - Menor a 50 → Bajo

## Metodología

### 1. Pasos del Script

1.  Generé una semilla aleatoria.\
2.  Creé una lista de 1000 números entre 0 y 100.\
3.  Clasifiqué cada número como Alto o Bajo usando el umbral.\
4.  Mostré los primeros 10 datos como ejemplo.\
5.  Conté cuántos fueron Altos y cuántos fueron Bajos.\
6.  Medí el tiempo total de ejecución del programa.\
7.  Guardé todos los resultados en un archivo de texto.

### 2. Flujo GitFlow

-   git init\
-   git flow init -d\
-   git flow feature start clasificacion\
-   Desarrollé el script en la rama feature\
-   git flow feature finish clasificacion\
-   git flow release start 1.0.0\
-   git flow release finish 1.0.0

## Resultados

Primeros 10 ejemplos:\
44 → Bajo, 55 → Alto, 58 → Alto, 32 → Bajo, 50 → Alto,\
65 → Alto, 46 → Bajo, 9 → Bajo, 83 → Alto, 44 → Bajo

### Conteos finales

-   Altos: 525\
-   Bajos: 475

### Tiempo total

0.015671 segundos

## Evidencias

Las evidencias de la práctica se encuentran en:\
`docs/evidencias`

## Conclusiones

Con esta práctica aprendí a trabajar con GitFlow paso a paso, creando
ramas y llevando todo el proceso hasta generar un tag final.\
También comprendí cómo funciona un árbol de decisión simple basado en un
umbral, y cómo puede clasificar datos de una manera rápida y directa.
