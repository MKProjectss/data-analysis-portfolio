# Análisis de Tecnologías en TI | Fase 4: Análisis de datos

El objetivo de esta fase es identificar las tecnologías más usadas, deseadas y admiradas, asi como tendencias y oportunidades o brechas entre uso actual e interés futuro.

---

## Enfoque de análisis

El análisis se realizó empleando métricas previamente calculadas como *InterestRatio*, *AdmiredRatio*, *UsageRate*, *InterestRate* y *AdmiredRate*, permitiendo evaluar la popularidad y percepción relativa de cada una de las tecnologías.  

---

## Análisis exploratorio

### Popularidad y preferencias
Se analizaron las tecnologías desde múltiples perpectivas:  

- Top 10 de tecnologías más usadas
- Top 10 más deseadas
- Top 10 más admiradas
- Top 10 por *InterestRatio*
- Top 10 por *AdmiredRatio*

Este análisis permite diferenciar entre:
- Tecnologías que usan actualmente los profesionales de TI
- Lo que desean aprender a usar
- Lo que realmente valoran o disfrutan

---

### Comparación directa entre métricas
Se realizó una comparación en valores absolutos entre:

- Uso actual (*HaveWorkedWith*)
- Interés (*WantToWorkWith*)
- Admiración (*Admired*)

Esto permite identificar diferencias entre adopción real y preferencias

---

## Análisis de relaciones (cuadrantes)

Se utilizaron gráficos de dispersión para segmentar tecnologías según distintas métricas.

### Tipos de análisis realizados
- **HaveWorkedWith** vs **InterestRatio**
- **InterestRatio** vs **AdmiredRatio**
- **InterestRate** vs **AdmiredRate**

Estos análisis permiten clasificar tecnologías en cuadrantes como:

- Alta adopción / bajo interés → posibles tecnologías saturadas
- Bajo uso / alto interés → tecnologías emergentes
- Alta admiración → tecnologías bien valoradas por sus usuarios

---

## Análisis de segmentación

### Clasificación por cuadrantes 
Se definieron dos enfoques de segmentación:

- **MarketQuadrant**: basado en uso e interés
- **PerceptionQuadrant**: basado en interés y admiración

Se realizó:

- Cruce entre ambos caudrantes (crosstab)
- Análisis de alineación entre mercado y percepción

---

### Oportunity Score

Para identificar tecnologías con mayor potencial, se definió un indicador compuesto llamado **Opportunity Score**.

Este score combina la posición de mercado y la percepción de los usuarios en una sola métrica.

#### Definición

> OpportunityScore = (MarketScore × 0.6) + (PerceptionScore × 0.4)

#### Lógica del modelo

- **MarketScore (60%)**  
  Tiene mayor peso, ya que refleja la adopción real y la demanda en el mercado.

- **PerceptionScore (40%)**  
  Representa la valoración de los usuarios, complementando el análisis con un enfoque cualitativo.

#### Interpretación

- Valores altos → Tecnologías con fuerte adopción y buena percepción  
- Valores medios → Tecnologías con potencial pero con áreas de mejora  
- Valores bajos → Tecnologías con bajo posicionamiento o baja valoración  

Este indicador permite priorizar tecnologías considerando tanto su impacto actual como su percepción futura.

#### Uso en el análisis

- Ranking de tecnologías (Top 10)  
- Visualización mediante gráficos de barras y heatmaps  
- Identificación de tecnologías con mayor potencial estratégico  

---

### Alignment Gap
Para evaluar la diferencia entre la percepción de una tecnología y su posición en el mercado, se definió un indicador llamado **Alignment Gap**.

Este se calculó como la diferencia entre dos scores:

- **MarketScore**: basado en la clasificación de mercado (*MarketQuadrant*)
- **PerceptionScore**: basado en la percepción de los usuarios (*PerceptionQuadrant*)

#### Asignación de scores

**MarketScore:**
- Growth → 3  
- Emerging → 2  
- Mature → 1  
- Declining → 0  

**PerceptionScore:**
- Leaders → 3  
- Loved Niche → 2  
- Trendy → 1  
- Weak → 0  

#### Definición

El **Alignment Gap** se define como:

> AlignmentGap = PerceptionScore − MarketScore

#### Interpretación

- **Gap positivo** → Tecnologías mejor valoradas por los usuarios que su posición en el mercado  
- **Gap negativo** → Tecnologías con mayor adopción que valoración percibida  
- **Gap cercano a 0** → Alineación entre mercado y percepción  

Este indicador permite identificar tecnologías subestimadas, sobrevaloradas o correctamente posicionadas.

---

## Análisis por segmentos demográficos

### Experiencia
- Relación entre años de experiencia y cuadrantes (boxplot)  
- Distribución de experiencia por tipo de tecnología (KDE plot)  

---

### Edad
- Crosstab entre grupo de edad y percepción  
- Distribución de percepción por grupo de edad (stacked bar)  
- Tendencias de percepción según la edad (gráfico de líneas)  

Este análisis permite identificar cómo cambian las preferencias según el perfil del desarrollador.

---

## Hallazgos principales

- El Top 4 de lenguajes más utilizados, deseados y admirados se mantiene consistente (JavaScript, Python, HTML/CSS y SQL), lo que indica que el ecosistema actual está fuertemente sustentado en desarrollo web y manejo de datos.

- Lenguajes como Rust y Go muestran altos niveles de interés y admiración relativa, lo que sugiere un fuerte potencial de crecimiento y consolidación en el mediano plazo.

- Existe una clara diferencia entre adopción y percepción: no todas las tecnologías ampliamente utilizadas son altamente valoradas, lo que evidencia posibles señales de saturación en tecnologías maduras.

- Las tecnologías con alta intención relativa pero baja base de usuarios representan oportunidades emergentes, aunque con mayor nivel de incertidumbre en su adopción.

- Las tecnologías consolidadas (como bases de datos SQL y plataformas cloud líderes) mantienen grandes bases de usuarios y crecimiento estable, reflejando baja volatilidad en el corto plazo.

- Se identifican brechas entre percepción y mercado (Alignment Gap), permitiendo detectar tecnologías subestimadas o sobrevaloradas dentro del ecosistema.

- La percepción de las tecnologías tiende a volverse más crítica conforme aumenta la experiencia de los desarrolladores, lo que sugiere un cambio en criterios de evaluación según el nivel profesional.

---

## Limitaciones del análisis

- Los resultados se basan en una muestra específica de la encuesta y pueden no representar completamente el estado global del mercado tecnológico.  

- Las métricas reflejan percepciones y autodeclaraciones de los participantes, lo que puede introducir sesgos.  

- Algunas tecnologías con baja base de usuarios pueden presentar métricas volátiles o menos estables.  

- El análisis es de carácter descriptivo y no implica causalidad.

---

## Conclusión

El análisis permitió identificar patrones clave entre adopción, interés y percepción, proporcionando una visión integral del estado actual del mercado tecnológico y posibles tendencias futuras.
