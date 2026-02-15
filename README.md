# 📊 Tech Jobs Data Analysis

Proyecto de Análisis de Datos enfocado en la extracción, procesamiento y visualización de ofertas laborales del sector tecnológico a nivel global.

Este proyecto tiene como objetivo recopilar información de empleos del mundo tech, transformarla en datos estructurados y presentarla de manera clara para facilitar su análisis, interpretación y toma de decisiones basada en datos.

---

## 🚀 Objetivos

* Extraer ofertas laborales del sector tecnológico desde distintas fuentes.
* Estandarizar y limpiar los datos recolectados.
* Analizar tendencias del mercado laboral tech.
* Visualizar información relevante de forma comprensible.
* Identificar patrones como:

  * Tecnologías más demandadas
  * Rangos salariales
  * Ubicación geográfica
  * Modalidad (Remoto / Híbrido / Presencial)
  * Nivel de experiencia requerido

---

## 🛠️ Tecnologías Utilizadas

El proyecto está desarrollado en **Python**, utilizando un entorno virtual (`venv`) para aislar dependencias.

### Librerías principales:

* pandas==2.3.3
* numpy==1.26.3
* python-jobspy==1.1.82
* requests==2.32.5
* beautifulsoup4==4.14.3
* markdownify==0.13.1
* pydantic==2.12.5
* regex==2024.11.6
* python-dateutil==2.9.0.post0
* pytz==2025.2
* tzdata==2025.3
* urllib3==2.6.3
* tls-client==1.0.1

---

## 📂 Estructura del Proyecto

```
tech-jobs-data-analysis/
│
├── venv/                  # Entorno virtual
├── utils/
│   └── scraper.py         # Lógica de extracción de datos
├── main.py                # Punto de entrada del proyecto
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación
```

---

## ⚙️ Instalación

1️⃣ Clonar el repositorio

git clone https://github.com/tu-usuario/jobs-data-analysis.git

cd jobs-data-analysis

### 2️⃣ Crear entorno virtual

python -m venv venv

### 3️⃣ Activar entorno virtual

Windows:

venv\Scripts\activate

Mac / Linux:

source venv/bin/activate

### 4️⃣ Instalar dependencias

pip install -r requirements.txt

---

## ▶️ Ejecución

python main.py

El flujo general del proyecto incluye:

1. Extracción de datos desde fuentes de empleo.
2. Procesamiento y limpieza de la información.
3. Transformación en estructuras analizables.
4. Preparación de resultados para análisis o visualización.

---

## 📊 Análisis que se pueden realizar

* Tecnologías más solicitadas en el mercado.
* Distribución salarial por país o región.
* Comparación entre modalidades de trabajo.
* Demanda por nivel de experiencia.
* Tendencias emergentes en el sector tech.
* Palabras clave más frecuentes en descripciones laborales.

---

## 🔎 Enfoque Técnico

* Uso de scraping y APIs para obtención de datos.
* Validación y estructuración con Pydantic.
* Limpieza y transformación con Pandas.
* Manipulación avanzada de texto con Regex.
* Manejo de fechas y zonas horarias.
* Preparado para futura integración con dashboards o bases de datos.

---

## 🔮 Mejoras Futuras

* Integración con base de datos (PostgreSQL / MongoDB).
* Visualización interactiva con Streamlit o Dash.
* Automatización del scraping (cron jobs).
* Implementación de análisis predictivo.
* Exportación de reportes en CSV / Excel / PDF.
* Dockerización del proyecto.
* Tests automatizados.

---

## 📈 Aplicaciones

Este proyecto puede utilizarse para:

* Análisis del mercado laboral tecnológico.
* Apoyo en decisiones profesionales basadas en datos.
* Investigación de tendencias tecnológicas.
* Proyecto de portafolio en Data Analysis con Python.

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica avanzada de análisis de datos enfocado en el sector tecnológico global.
