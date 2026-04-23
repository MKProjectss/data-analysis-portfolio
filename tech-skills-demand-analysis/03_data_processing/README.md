# Análisis de Tecnologías en TI | Fase 3: Procesamiento de Datos  

El objetivo de esta etapa es transformar el conjunto de datos original en un dataset analítico consistente y reproducible, adecuado para análisis exploratorio y modelado descriptivo.

---

## Limpieza inicial  

- Se eliminaron 20 registros duplicados utilizando **drop_duplicates()** para evitar sesgos en los conteos y análisis posteriores
-	Se normalizaron cadenas de texto eliminando espacios en blanco al inicio y final para evitar categorías inconsistentes
-	Eliminación de registros sin información en tecnologías a analizar

---

## Estandarización y transformación de variables  

### Experiencia en programación (YearsCode  y YearsCodePro)  

- Originalmente variables categóricas (tipo objeto) debido a valores textuales.
- Se convirtieron en variables numéricas ordinales aplicando
  - **'Less than 1 year'** → **0**
  - **‘More than 50 years’** → **51**

---

### País (Country)

- Se normalizaron los nombres de los países utilizando la librería **pycountry**, basada en el estándar **ISO 3166-1 alpha-3**
- Registros no definidos en la librería fueron corregidos manualmente
-	Presenta aproximadamente 10% de valores faltantes, se conservan los registros como nulos para mantener la integridad del estándar ISO-3166-1

---

### Nivel Educativo (EdLevel)

- Se redujo la carnalidad agrupando 8 categorías origianles en 4 macro-categorías:
  -	**No formal degree**, incluye: Primary/elementary school, Secondary school y Some college/university
  -	**Undergraduate Degree**: Associate degree y Bachelor’s degree
  -	**Postgraduate Degree**: Master’s degree y Professional degree
  -	**Other**: Something else
-	Los valores faltantes se conservaron como **"No especificado"** debido a la naturaleza informativa en encuestas

---

### Age

- Variable categórica ordinal
- Se estandarizó las etiquetas eliminando el sufijo “years old” para mejorar la legibilidad sin modificar el sentido semántico, ejemplos:
  - **'18-24 years old'** → **'18-24'**
  - **'25-34 years old'** → **'25-34'**
 
---

## Variables con multirespuesta

- Las **columnas multivalor** (separadas por delimitador ;) se transforman a un **modelo relacional** (formato long):
  - Se implementó una función reutilizable basada en **explode()** para normalizar respuestas múltiples por encuestado
  - Cada registro representa una relación única entre **ResponseId** y una entidad tecnológica
  - Se incorporó una variable **Relation** para diferenciar entre:
    - **HaveWorkedWith** (uso actual)
    - **WantToWorkWith** (interés)
    - **Admired** (satisfacción)
  - Se generaron tablas independientes por dominio:
    - Lenguajes
    - Bases de datos
    - Plataformas
    - Herramientas colaborativas
- Los datasets resultantes se almacenan en formato **Parquet**
- La tabla base de encuestados se mantiene sin modificaciones, permitiendo su uso para segmentaciones demográficas

---

## Enriquecimiento analítico  

A partir del modelo relacional, se construyeron métricas clave para evaluar el posicionamiento de cada tecnología:

- **Adopción**: Usage Rate
- **Interés futuro**: Interest Rate
- **Satisfacción**: Admired Rate
- **Deseabilidad relativa**: Interest Ratio
- **Potencial de crecimiento**: Growth Potential
- **Interés neto**: Net Interest
- **Conversión potencial**: Conversion Potential  

Estas métricas permiten analizar:

- Brechas entre uso actual e interés
- Tecnologías emergentes vs consolidadas
- Oportunidades de adopción en el mercado

---

## Tratamiento de valores nulos

- Para evitar sesgos o alterar los resultados del análisis se decidió no eliminar los nulos en esta etapa del proceso
- Se optó por un enfoque contextual, donde el tratamiento dependerá del análisis específico y la variable involucrada

---

## Validación de la calidad de los datos

- Se realizaron verificaciones de consistencia
  - Tipos de datos correctos
  - Cardinalidad en variables categóricas
  - Eliminación de duplicados
 
---

## Resultados de fase

Se obtiene un conjunto de datos normalizado compuesta por:  
- Tabla de encuestados
- Tablas relacionales por dominio tecnológico  

Listo para consumo en la fase de análisis sin necesidad de reprocesamiento.






