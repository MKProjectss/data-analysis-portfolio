# Análisis de Tecnologías en TI | Fase 3: Procesamiento de Datos  

El objetivo de esta etapa es transformar el conjunto de datos original en un dataset analítico consistente y reproducible, adecuado para análisis exploratorio y modelado descriptivo.

---

## Limpieza inicial  

- Se eliminaron 20 registros duplicados utilizando **drop_duplicates()** para evitar sesgos en los conteos y análisis posteriores.
-	Se normalizaron cadenas de texto eliminando espacios en blanco al inicio y final para evitar categorías inconsistentes.

---

## Estandarización y transformación de variables  

### Experiencia en programación (YearsCode  y YearsCodePro)  

- Originalmente variables categóricas (tipo objeto) debido a valores textuales.
- Se convirtieron en variables numéricas ordinales aplicando
  - **'Less than 1 year'** → **0**
  - **‘More than 50 years’** → **51**

---

### País (Country)

- Se normalizaron los nombres de países utilizando la librería **pycountry**, basada en el estándar **ISO 3166-1 alpha-3**
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

- Variable categórica ordinal.
- Se estandarizó las etiquetas eliminando el sufijo “years old” para mejorar la legibilidad sin modificar el sentido semántico, ejemplos:
  - **'18-24 years old'** → **'18-24'**
  - **'25-34 years old'** → **'25-34'**
 
---

## Variables con multirespuesta

- Las **columnas multivalor** (separadas por delimitador) se transforman a un **modelo relacional**:
  - Se implementó una función genérica basada en **explode()** para normalizar respuestas múltiples
  - Cada dominio tecnológico se almacena en tablas independientes en formato parquet
  - La tabla base de encuestados permanece sin alterar
- Este enfoque evita combinaciones artificiales y permite análisis consistentes entre tecnologías y características demográficas

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






