# UNESCO_climate

## Archivos

### Principales
- workers_vulnerability.ipynb: Calcula la cantidad de trbajadores vulnerables al cambio climático
- - Crea el archivo "../share/Indexes/vulnerable_workers.csv"
- - Requiere correr antes "indice_clima.ipynb", "indice_socio.ipynb", e "indice_work.ipynb"
- pais_vuln.ipynb: Calcula las capas de exposición para los mapas por país.
- - Crea la carpeta "../results/hotpots/" y los archivos que contiene.
- - Requiere correr antes "indice_clima.ipynb"
indice_work.ipynb: Calcula un índice por país de vulnerabilidad
socioeconómica ante riesgos de transición
indice_socio.ipynb: Calcula un índice por país de vulnerabilidad socioeconómica ante riesgos físicos
indice_riesgo.ipynb: Calcula un índice por país de riesgo ante el cambio climático
indice_clima.ipynb: Calcula un índice por país de exposición al cambio climático 
heritage.ipynb
impact_pop.ipynb
1km_preg.ipynb

### Secundarios y no utilizados
- sea_level.ipynb: Crea una tabla y un NetCDF de cambios en el nivel del mar con los datos de la NASA
- quantile.ipynb: Obtiene las variables climáticas, socioeconómicas y de gobernanza y cálcula índices para cada categoría
- - Crea el archivo "share/Climate/sea_level_change.csv" y "results/sea_level_change_ssp245_2050.nc"
mapa.ipynb: Pruebas de mapas nacionales y subnacionales

### Archivos
- Los archivos de la carpeta "../results/graphs/" se copiaron directo de los cuadernos de Jupyter, no los guarda el programa.