# Análisis de Tecnologías en TI | Fase 3: Procesamiento de Datos  

El objetivo de esta etapa es transformar el conjunto de datos original en un dataset analítico consistente y reproducible, adecuado para análisis exploratorio y modelado descriptivo.

---

## Limpieza inicial  

- Se eliminaron 20 registros duplicados utilizando drop_duplicates() para evitar sesgos en los conteos y análisis posteriores.
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

- Se normalizaron los nombres de países utilizando la librería pycountry, basada en el estándar ISO 3166-1 alpha-3
- Registros no definidos en la librería fueron corregidos manualmente
-	Presenta aproximadamente 10% de valores faltantes, se conservan los registros como nulos para mantener la integridad del estándar ISO-3166-1

---

### Nivel Educativo (EdLevel)



