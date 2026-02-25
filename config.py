import pandas as pd

# Estamos cargando el archivo Excel que contiene la información de los niveles de trabajo y sus perfiles asociados. Luego, convertimos esta información en un diccionario para facilitar su uso en la categorización de trabajos.
job_level_df = pd.read_excel('master_data/profile.xlsx')
JOB_LEVEL_DICT = job_level_df.set_index('Value')['Profile'].to_dict()

# De manera similar, estamos cargando otro archivo Excel que contiene información sobre los grupos de trabajo y sus categorías asociadas. También convertimos esta información en un diccionario para su uso en la categorización de trabajos.
job_group_df = pd.read_excel('master_data/categories.xlsx')
JOB_GROUP_DICT = job_group_df.set_index('keyword')['category'].to_dict()

# Finalmente, definimos una lista de palabras clave que se utilizarán para identificar trabajos remotos en la función de categorización de trabajos.
REMOTE_KEYWORDS = ['remote', 'hybrid', 'on site']

states_df = pd.read_excel('master_data/states.xlsx')
STATES_DICT = states_df.set_index('State')['Code'].to_dict()

# Definimos un diccionario que contiene factores de conversión para diferentes intervalos de tiempo. Esto se utilizará para convertir salarios a una base anual, facilitando la comparación entre diferentes ofertas de trabajo que pueden tener salarios expresados en diferentes intervalos (por ejemplo, mensual, semanal, diario, etc.).
INTERVAL_FACTORS = {'yearly':1, 'monthly':12, 'weekly':49, 'daily':230, 'hourly':1840}

skills_df = pd.read_excel('master_data/skills.xlsx')
SKILLS_DICT = skills_df.set_index('Skills')['Group'].to_dict()

EDUCATION_PRIORITY = {"None":0, "Bachelor":1, "Master":2, "MBA":3, "Phd":4}

CATEGORIES = {
    'programming_lenguajes': {"Python", "Java", "C++", "JavaScript", "R", "SQL", "Go", "Ruby", "PHP", "Rust", "C#", "DAX", "VBA", "ABAP", "HTML", "CSS", "Julia", "Swift"},
    'lenguajes':{"English", "Spanish", "French", "German", "Chinese", "Japanese", "Portuguese", "Russian", "Arabic", "Hindi"}
}