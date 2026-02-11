# Proyecto: Análisis de Tecnologías en TI – Fase 2: Preparar

Este análisis se basa en datos externos, específicamente en un subconjunto de la **Encuesta de Desarrolladores de Stack Overflow 2024**.   

El subconjunto fue proporcionado como parte del material educativo de la certificación de IBM en Coursera. Los datos originales pertenecen a Stack Overflow y se distribuyen bajo licencia abierta (ODbL).

Fuente oficial de la encuesta:
https://stackoverflow.blog/2024/08/06/2024-developer-survey/

---

## Objetivo de fase  

Evaluar la estructura, calidad y relevancia del conjunto de datos con el fin de identificar posibles problemas que afecten el análisis posterior y definir la estrategia de transformación necesaria en la fase de procesamiento.

---

## Descripción del conjunto de datos

El subconjunto utilizado cuenta con:

- **65,457 registros**
- **114 atributos**

Los tipos de datos identificados incluyen:

- Numéricos, ejemplo: CompTotal.
- Categóricos, ejemplos: Age, EdLevel.

---

## Características identificadas durante la exploración inicial

Durante la exploración general del dataset se detectaron las siguientes condiciones relevantes:

- Variables numéricas almacenadas como tipo object.  
- Columnas que permiten múltiples respuestas separadas por el carácter `;`.
- Presencia de valores nulos en múltiples atributos.
- Atributos con un alto porcentaje de datos faltantes, por ejemplo, PlatformAdmired con 34,069 nulos (52%).
- Se detectaron 20 registros duplicados.  

Estas condiciones impactan directamente la estrategia de transformación y limpieza de datos, como se lista a continuación:  
 
- Conversión de tipos object a numéricos cuando corresponda.
- Transformación de columnas multivalor mediante separación y expansión.
- Tratamiento de valores nulos según análisis por atributo.  
- Eliminación de duplicados. 

---

## Atributos por analizar

Los atributos principales seleccionados son aquellos que permiten identificar el estado actual del mercado tecnológico, sus tendencias y percepciones, alineados con los objetivos del análisis.

### Tecnologías principales

- LanguageHaveWorkedWith  
- LanguageWantToWorkWith  
- LanguageAdmired  
- DatabaseHaveWorkedWith  
- DatabaseWantToWorkWith  
- DatabaseAdmired  
- PlatformHaveWorkedWith  
- PlatformWantToWorkWith  
- PlatformAdmired  
- NEWCollabToolsHaveWorkedWith  
- NEWCollabToolsWantToWorkWith  
- NEWCollabToolsAdmired  

---

## Atributos de contexto

También se incluyen atributos que no son el foco principal del análisis, pero que pueden utilizarse para segmentaciones futuras o análisis secundarios, aportando contexto sobre el perfil del encuestado:

- Country  
- Age  
- EdLevel  
- YearsCode  
- YearsCodePro  
- CompTotal  

---

## Atributo adicional estratégico

- TechEndorse  

Este atributo permite identificar tecnologías respaldadas dentro de las empresas donde laboran los profesionales de TI, aportando una perspectiva organizacional complementaria.

---

## Identificador (Llave primaria lógica)  

- ResponseId

Es el identificador único de cada registro, permite identificar duplicados.

---

## Atributos excluidos

Se excluyen atributos que no contribuyen directamente al cumplimiento de los objetivos del proyecto, como:

- RemoteWork  
- OpSysPersonal  

Asimismo, se excluyen atributos cuya composición presenta más del 50% de valores nulos, tales como:

- EmbeddedAdmired  
- EmbeddedWantToWorkWith  
- EmbeddedHaveWorkedWith  

---

## Consideraciones sobre la calidad de los datos

Durante la exploración inicial se identificó la presencia de valores nulos y atributos con tipos de datos incorrectamente definidos. Sin embargo, dado que se trata de una encuesta voluntaria, estos valores corresponden a preguntas no respondidas y no necesariamente a errores en los datos. El análisis se realizará considerando únicamente los registros con respuesta válida para cada atributo.    

En esta fase no se realizan transformaciones ni limpieza de datos. Las decisiones relacionadas con imputación, eliminación o transformación de variables serán abordadas en la fase de **Procesar**.

