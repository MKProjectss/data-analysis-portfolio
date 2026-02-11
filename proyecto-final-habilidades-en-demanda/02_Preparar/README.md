# Proyecto: Análisis de Tecnologías en TI – Fase 2: Preparar

Este análisis se basa en datos externos, específicamente en un subconjunto de la **Encuesta de Desarrolladores de Stack Overflow 2024**.  

El subconjunto utilizado cuenta con **65,457 registros** y **114 atributos**. Entre los tipos de datos identificados se encuentran variables de tipo objeto, flotante y entero.  

Se detectó que no todos los atributos tienen correctamente definido su tipo de dato (por ejemplo, variables numéricas almacenadas como texto). Además, algunos atributos permiten múltiples respuestas separadas por el carácter `;`, lo cual influye en la forma en que serán transformados y procesados en la siguiente fase.

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

Durante la exploración inicial se identificó la presencia de valores nulos y atributos con tipos de datos incorrectamente definidos.  

En esta fase no se realizan transformaciones ni limpieza de datos. Las decisiones relacionadas con imputación, eliminación o transformación de variables serán abordadas en la fase de **Procesar**.

