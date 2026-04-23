# Proyecto Final – Análisis de Habilidades en Demanda

## Contexto del negocio

En un entorno tecnológico altamente dinámico, la toma de decisiones basada en datos es clave para mantener la competitividad. Empresas que no alinean sus estrategias tecnológicas con las tendencias del mercado corren el riesgo de adoptar herramientas obsoletas o perder oportunidades emergentes.

Este proyecto simula un caso real de consultoría, donde una empresa busca identificar qué tecnologías priorizar en términos de adopción, capacitación y reclutamiento.

---

## Objetivo del Proyecto

Analizar el comportamiento de tecnologías en el ecosistema TI para:
- Identificar tecnologías consolidadas, emergentes y en declive  
- Evaluar la relación entre uso actual, interés futuro y satisfacción  
- Detectar oportunidades estratégicas de adopción tecnológica 

---

## Fuente de datos
- Stack Overflow Developer Survey 2024 (subconjunto)  
- Datos complementarios obtenidos mediante APIs y Web Scraping  

> Nota: Los datos corresponden a respuestas autodeclaradas, por lo que reflejan percepción de los desarrolladores.


---

## Enfoque metodológico
Se implementó un flujo completo de análisis de datos estructurado en 6 fases:

1. **Preguntar** → Definición del problema y preguntas de negocio  
2. **Preparar** → Evaluación de calidad y selección de datos  
3. **Procesar** → Limpieza, transformación y modelado relacional  
4. **Analizar** → Exploración de datos y construcción de métricas  
5. **Compartir** → Visualización mediante dashboard interactivo  
6. **Actuar** → Traducción de insights en decisiones estratégicas 

---

## Métricas clave
El análisis se basa en indicadores diseñados para evaluar el posicionamiento de cada tecnología:

- **Usage Rate** → Nivel de adopción actual  
- **Interest Rate** → Demanda futura  
- **Admired Rate** → Nivel de satisfacción  
- **Interest Ratio** → Deseabilidad relativa  
- **Opportunity Score** → Potencial estratégico compuesto  
- **Alignment Gap** → Brecha entre percepción y mercado  

---

## Hallazgos clave

- Tecnologías como **JavaScript, Python, HTML/CSS y SQL** se mantienen como el núcleo del ecosistema, combinando alta adopción, interés y valoración.

- Existen tecnologías emergentes (como **Rust y Go**) con **alto interés y admiración pero baja adopción**, lo que indica oportunidades de crecimiento.

- Se identificó una **brecha entre uso y percepción**: no todas las tecnologías ampliamente utilizadas son bien valoradas, lo que sugiere posibles señales de saturación.

- Las tecnologías consolidadas (ej. **AWS, PostgreSQL**) muestran estabilidad, con alta adopción pero menor crecimiento relativo.

- El análisis de **Alignment Gap** permitió detectar tecnologías subestimadas y sobrevaloradas dentro del mercado.

- La percepción de las tecnologías se vuelve más crítica conforme aumenta la experiencia del desarrollador.

---

## Recomendaciones estratégicas

- Priorizar la adopción y capacitación en tecnologías con **alto interés y baja adopción** (oportunidades emergentes).

- Mantener tecnologías consolidadas como base para garantizar estabilidad operativa y disponibilidad de talento.

- Limitar la incorporación de tecnologías con **bajo interés y baja admiración** en nuevos desarrollos.

- Alinear estrategias de reclutamiento con tendencias tecnológicas y perfiles emergentes del mercado.

- Implementar pilotos controlados para evaluar tecnologías con alto potencial antes de su adopción a gran escala.

---

## Dashboard interactivo
El proyecto incluye un dashboard desarrollado en Power BI que permite:

- Explorar uso, interés y satisfacción de tecnologías  
- Analizar tendencias por categoría (lenguajes, bases de datos, cloud, herramientas)  
- Identificar oportunidades mediante análisis por cuadrantes  

---

## Herramientas y Tecnologías

- **Python** (Pandas, Matplotlib, Seaborn)
- **Jupyter Notebook**
- **Power Bi**
- **Excel**

---

## Estructura del Proyecto


```
proyecto-final-habilidades-en-demanda/
├── 01_Preguntar/               # Problema de negocio y preguntas analíticas
├── 02_Preparar/                # Evaluación y comprensión de datos
├── 03_Procesar/                # Limpieza y transformación
├── 04_Analizar/                # Análisis exploratorio de datos (EDA)
├── 05_Compartir/               # Dashboard y visualizaciones
└── 06_Actuar/                  # Recomendaciones estratégicas
```

---

## Valor del proyecto
Este análisis proporciona una visión estructurada del ecosistema tecnológico, permitiendo:

- Reducir incertidumbre en decisiones tecnológicas  
- Identificar tendencias emergentes del mercado  
- Optimizar estrategias de talento y capacitación  
- Detectar oportunidades de innovación  

---

## Limitaciones

- Datos basados en percepción (encuesta)  
- Subconjunto del dataset original  
- No representa necesariamente el mercado en tiempo real  
- Análisis descriptivo (no causal)  

---

## Autor

Ingeniero en Mecatrónica con certificación en **Análisis de Datos por IBM**, orientado a roles **junior en análisis de datos, captura de información y soporte analítico**.



