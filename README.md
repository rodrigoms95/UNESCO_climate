# UNESCO_climate

## Archivos

### Principales

- **indice_clima.ipynb**: Calcula un índice por país de exposición al cambio climático 
    - Crea el archivo *"../share/Indexes/climate_index.csv"*
    - Crea la carpeta *"../results/hotpots/"* y los archivos que contiene.

- **indice_socio.ipynb**: Calcula un índice por país de vulnerabilidad socioeconómica ante riesgos físicos
    - Crea el archivo *"../share/Indexes/Physical_vulnerability_index.csv"*

- **indice_riesgo.ipynb**: Calcula un índice por país de riesgo ante el cambio climático
    - Crea el archivo *"../share/Indexes/climate_risk_index.csv"*
    - Requiere correr antes *"indice_clima.ipynb"* e *"indice_socio.ipynb"*

- **indice_work.ipynb**: Calcula un índice por país de vulnerabilidad
socioeconómica ante riesgos de transición
    - Crea el archivo *"../share/Indexes/Transition_vulnerability_index.csv"*

- **workers_vulnerability.ipynb**: Calcula la cantidad de trbajadores vulnerables al cambio climático
    - Crea el archivo *"share/Indexes/vulnerable_workers.csv"*
    - Requiere correr antes *"indice_clima.ipynb"*, *"indice_socio.ipynb"*, e *"indice_work.ipynb"*

- **heritage.ipynb**: Calcula los sitios patrimonio de la humanidad expuestos al cambio climático
    - Crea el archivo *"results/WHC/WHC.shp"*, para calcular manualmente en QGIS los sitios expuesto al aumento del nuvel del mar
    - Crea el archivo *"share/Indexes/WHC_sites.csv"*
    - Requiere correr antes *"indice_clima.ipynb"*, *"indice_socio.ipynb"*, e *"indice_work.ipynb"*
    - Requiere la carpeta *"results/WHC_sea_level_rise/"* generada con un anaálisis manual en QGIS

- **impact_pop.ipynb**: Calcula la exposición al cambio climático de sectores demográficos específicos.
    - Crea el archivo *"share/Indexes/extreme_poor.csv"*
    - Requiere correr antes*"indice_clima.ipynb"*, *"indice_socio.ipynb"*, e *"indice_work.ipynb"*

- **NDC.ipynb**: Mapas de Climate Action Tracker, evaluación de NDCs

- **impact_women.py**: Calcula la exposición al cambio climático para grupos demográficos femeninos
    - Crea los archivo *"share/Index/age_sex_structures_1995_2014.csv"* y *"share/Index/age_sex_structures_2040_2059_SSP245.csv"*
    - Requiere haber creado los archivos de la carpeta *"results/hotspots_1km/"* en QGIS a partir de *"results/hotspots/"*, que a su vez son producto de correr *"indice_clima.ipynb"*

- **immpact_women.ipynb**:Visualización de la la exposición al cambio climático para grupos demográficos femeninos

### Secundarios y no utilizados
- **sea_level.ipynb**: Crea una tabla y un NetCDF de cambios en el nivel del mar con los datos de la NASA
    - Crea el archivo "share/Climate/sea_level_change.csv" y "results/sea_level_change_ssp245_2050.nc"
- **quantile.ipynb**: Obtiene las variables climáticas, socioeconómicas y de gobernanza y cálcula índices para cada categoría
mapa.ipynb: Pruebas de mapas nacionales y subnacionales

### Archivos
- Los archivos de la carpeta "../results/graphs/" se copiaron directo de los cuadernos de Jupyter, no los guarda el programa