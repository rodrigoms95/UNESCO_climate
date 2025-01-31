# Calcula la exposición al cambio climático para grupos demográficos femeninos

# Importamos librerías
import os
import shutil
import numpy as np
import pandas as pd
import xarray as xr

# Carpetas
file_path = "results/hotspots_1km/" 
data_path = "Bases_de_datos/Worldpop/"

d_f = ["results/"]
d_n = ["diss_me"]
s_f = ["2040_2059_SSP245"]
g_f = ["f"]
g_n = ["Female"]
a_f = [70, 75, 80]
a_n = ( [f"{x} years" for x in [ "70-75", "75-80", "more than 80" ] ] )
#d_f = ["share/Indexes/", "results/"]
#d_n = ["ISO_N3", "diss_me"]
#s_f = ["1995_2014", "2040_2059_SSP245"]
#g_f = ["f", "m"]
#g_n = ["Female", "Male"]
#a_f = [0, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
#a_n = ( ["0-12 months"] + [f"{x} years" for x in [ "1-5",  "5-10", "10-15",
#  "15-20", "20-25", "25-30", "30-35", "35-40", "40-45", "45-50", "50-55",
#  "55-60", "60-65", "65-70", "70-75", "75-80", "more than 80" ] ] )

# Variables de población afectada
vars = [ "Only extreme rainfall", "Only extreme heat",
         "Only drought", "Only strong hurricanes",
         "Extreme rainfall & heat", "Extreme rainfall & drought",
         "Extreme rainfall & hurricanes", "Extreme heat & drought",
         "Extreme heat & hurricanes", "Drought & strong hurricanes",
         "Extreme rainfall, heat, & drought",
         "Extreme rainfall, heat, & hurricanes",
         "Extreme rainfall, drought, & hurricanes",
         "Extreme heat, drought, & hurricanes",
         "Extreme rainfall, heat, drought, & hurricanes" ]
var_clim = [ "Extreme rainfall", "Extreme heat",
             "Drought", "Strong hurricanes" ]
var_ci   = [
  [ "Only extreme rainfall", "Extreme rainfall & heat",
    "Extreme rainfall & drought", "Extreme rainfall & hurricanes",
    "Extreme rainfall, heat, & drought",
    "Extreme rainfall, heat, & hurricanes",
    "Extreme rainfall, drought, & hurricanes",
    "Extreme rainfall, heat, drought, & hurricanes" ],
  [ "Only extreme heat", "Extreme rainfall & heat",
    "Extreme heat & drought",
    "Extreme heat & hurricanes",
    "Extreme rainfall, heat, & drought",
    "Extreme rainfall, heat, & hurricanes",
    "Extreme heat, drought, & hurricanes",
    "Extreme rainfall, heat, drought, & hurricanes" ],
  [ "Only drought", "Extreme rainfall & drought",
    "Extreme heat & drought", "Drought & strong hurricanes",
    "Extreme rainfall, heat, drought, & hurricanes",
    "Extreme rainfall, heat, & drought",
    "Extreme rainfall, drought, & hurricanes",
    "Extreme heat, drought, & hurricanes", ],
  [ "Only strong hurricanes", "Extreme rainfall & hurricanes",
    "Extreme heat & hurricanes", "Drought & strong hurricanes",
    "Extreme rainfall, heat, & hurricanes",
    "Extreme rainfall, drought, & hurricanes",
    "Extreme heat, drought, & hurricanes",
    "Extreme rainfall, heat, drought, & hurricanes" ] ]
var_tot  = "Extreme climate"

# Archivos de zonas afectadas
files_n = [ "pre", "temp", "drought", "hurr",
          "temp_pre", "pre_drought", "pre_hurr",
          "temp_drought", "temp_hurr", "hurr_drought",
          "temp_pre_drought", "temp_pre_hurr",
          "pre_hurr_drought", "temp_drought_hurr",
          "temp_pre_hurr_drought" ]

# Ruta de archivo
names     = "age_sex_structures"
name_path = f"{data_path}{names}/"

# Iteramos para países y estados
for d in range(len(d_f)):
  # Iteramos para cada escenario
  for s in range(len(s_f)):

    # Nombres de archivos de zonas afectadas
    files = [ f"{x}_{s_f[s]}.tif" for x in files_n ]

    # Iteramos por género
    for g in range(len(g_f)):
      # Iteramos para cada edad
      for a in range(len(a_f)):

        # Archivo de población
        file_g = f"global_{g_f[g]}_{a_f[a]}_2020_1km.tif"
        path_g = f"../{name_path}{file_g}"

        # Archivo de países
        path_c = f"../{data_path}global_level{d}_1km_2000_2020.tif"

        # Solo corremos si existe el archivo de población.
        if os.path.exists(f"/Volumes/DATA/UNESCO/{name_path}{file_g}"):

          # Nombres de columnas y variables
          var_n   = f"{g_n[g]} population, {a_n[a]} old"
          name_n  = f" affected {var_n.lower()}"
          if   d_n[d] == "ISO_N3" : file_n  = f"{names}_{s_f[s]}.csv"
          elif d_n[d] == "diss_me": file_n  = f"{names}_{s_f[s]}_admin_1.csv"
          print(f"Processing {var_n}")
          name_p  = [ f"{v}{name_n}" for v in vars       ]
          name_pp = [ f"% {v}{name_n}" for v in vars     ]
          name_c  = [ f"{v}{name_n}" for v in var_clim   ]
          name_cp = [ f"% {v}{name_n}" for v in var_clim ]
          name_t  =   f"{var_tot}{name_n}"
          name_tp =   f"% {var_tot}{name_n}"
          name_ci = []
          for x in var_ci:
            name_ci.append( [ f"{v}{name_n}" for v in x ] )

          # Creamos la columna de datos si no existe
          if d_n[d] == "ISO_N3":
            if not os.path.exists( f"{d_f[d]}{file_n}" ):
              # Tabla base
              iso = "../Bases_de_datos/Country_ISO_code.csv"
              df_iso = pd.read_csv(iso).set_index("alpha-3")
              df_iso.index.name = d_n[d]
              df_iso = df_iso.rename(columns = {"country-code": d_n[d]})
              df_iso[var_n] = np.nan
              df_iso[name_p] = np.nan
              df_iso[name_pp] = None
              df_iso[["name", d_n[d], "region", "sub-region", "OECD", "EU27",
                "BRICS+", "BRICS", "LDC", "SIDS", "LLDC"] + name_p + name_pp
                ].to_csv( f"{d_f[d]}{file_n}" )
            else:
              df_iso = pd.read_csv( f"{d_f[d]}{file_n}", index_col = d_n[d] )
            if not var_n in df_iso.columns:
              df_iso[var_n] = np.nan
              df_iso[name_p] = np.nan
              df_iso[name_pp] = None
          elif d_n[d] == "diss_me":
            if not os.path.exists( f"{d_f[d]}{file_n}" ):
              # Tabla base
              df_iso = pd.DataFrame(index = np.arange(1, 20013))
              df_iso.index.name = d_n[d]
            else:
              df_iso = pd.read_csv( f"{d_f[d]}{file_n}",
                index_col = d_n[d] )
            if not var_n in df_iso.columns:
              df_iso[var_n] = np.nan
              df_iso[name_p] = np.nan
              df_iso[name_pp] = None

          # Copiamos el archivo de población a disco
          if not os.path.exists(path_g):
            print("Copying file...")
            shutil.copy2( f"/Volumes/DATA/UNESCO/{name_path}{file_g}", path_g )

          # Abrimos el archivo de países
          with xr.open_dataset(path_c) as countries:
            countries = countries.isel(band = 0).drop_vars(
              ["band", "spatial_ref"] ).rename_dims(
              {"x": "lon", "y": "lat"} ).rename_vars(
              {"x": "lon", "y": "lat"} )
            
            # Abrimos el archivo de población
            with xr.open_dataset(path_g) as gender:
              gender = gender.isel(band = 0).drop_vars(
                ["band", "spatial_ref"] ).rename_dims(
                {"x": "lon", "y": "lat"} ).rename_vars(
                {"x": "lon", "y": "lat"} )
              
              # Ajustamos índices
              gender["lat"] = countries["lat"]
              gender["lon"] = countries["lon"]
              gender["band_data"] = gender["band_data"].T

              # Coordenadas extremas
              lat_min = min( gender["lat"].values[0],
                            gender["lat"].values[-1] )
              lat_max = max( gender["lat"].values[0],
                            gender["lat"].values[-1] )
              lon_min = min( gender["lon"].values[0],
                            gender["lon"].values[-1] )
              lon_max = max( gender["lon"].values[0],
                            gender["lon"].values[-1] )
              if d_n[d] == "ISO_N3":
                lim_lat = [ slice(lat_max, (lat_max+lat_min)/2),
                            slice(lat_max, (lat_max+lat_min)/2),
                            slice((lat_max+lat_min)/2, lat_min),
                            slice((lat_max+lat_min)/2, lat_min) ]
                lim_lon = [ slice(lon_min, (lon_max+lon_min)/2),
                            slice((lon_max+lon_min)/2, lon_max),
                            slice(lon_min, (lon_max+lon_min)/2),
                            slice((lon_max+lon_min)/2, lon_max) ]
              elif d_n[d] == "diss_me":
                lim_lat = [ slice(lat_max, (lat_max*3+lat_min)/4),
                            slice(lat_max, (lat_max*3+lat_min)/4),
                            slice(lat_max, (lat_max*3+lat_min)/4),
                            slice(lat_max, (lat_max*3+lat_min)/4),
                            slice((lat_max*3+lat_min)/4, (lat_max+lat_min)/2),
                            slice((lat_max*3+lat_min)/4, (lat_max+lat_min)/2),
                            slice((lat_max*3+lat_min)/4, (lat_max+lat_min)/2),
                            slice((lat_max*3+lat_min)/4, (lat_max+lat_min)/2),
                            slice((lat_max+lat_min)/2, (lat_max+lat_min*3)/4),
                            slice((lat_max+lat_min)/2, (lat_max+lat_min*3)/4),
                            slice((lat_max+lat_min)/2, (lat_max+lat_min*3)/4),
                            slice((lat_max+lat_min)/2, (lat_max+lat_min*3)/4),
                            slice((lat_max+lat_min*3)/4, lat_min),
                            slice((lat_max+lat_min*3)/4, lat_min),
                            slice((lat_max+lat_min*3)/4, lat_min),
                            slice((lat_max+lat_min*3)/4, lat_min) ]
                lim_lon = [ slice(lon_min, (lon_max+lon_min*3)/4),
                            slice((lon_max+lon_min*3)/4, (lon_max+lon_min)/2),
                            slice((lon_max+lon_min)/2, (lon_max*3+lon_min)/4),
                            slice((lon_max*3+lon_min)/4, lon_max),
                            slice(lon_min, (lon_max+lon_min*3)/4),
                            slice((lon_max+lon_min*3)/4, (lon_max+lon_min)/2),
                            slice((lon_max+lon_min)/2, (lon_max*3+lon_min)/4),
                            slice((lon_max*3+lon_min)/4, lon_max),
                            slice(lon_min, (lon_max+lon_min*3)/4),
                            slice((lon_max+lon_min*3)/4, (lon_max+lon_min)/2),
                            slice((lon_max+lon_min)/2, (lon_max*3+lon_min)/4),
                            slice((lon_max*3+lon_min)/4, lon_max),
                            slice(lon_min, (lon_max+lon_min*3)/4),
                            slice((lon_max+lon_min*3)/4, (lon_max+lon_min)/2),
                            slice((lon_max+lon_min)/2, (lon_max*3+lon_min)/4),
                            slice((lon_max*3+lon_min)/4, lon_max) ]

              # Iteramos para cada categoría climática
              for i, v in enumerate(vars):
                print(f" {v}                                     ")#, end = "\r")

                cols = [var_n, name_p[i], name_pp[i]]

                # Abrimos archivo climático
                path_clim = f"{file_path}{files[i]}"
                with xr.open_dataset( f"{file_path}{files[i]}") as clim:
                  clim = clim.isel(band = 0).drop_vars(
                    ["band", "spatial_ref"] ).rename_dims(
                    {"x": "lon", "y": "lat"} ).rename_vars(
                    {"x": "lon", "y": "lat"} )
                  
                  # Ajustamos índices
                  clim["lat"] = countries["lat"]
                  clim["lon"] = countries["lon"]
                
                  # Igualamos la extensión de los 
                  # archivos y pasamos a DataFrame
                  countries_i = []
                  for j in range( len(lim_lat) ):
                    gender_j = gender.sel(
                      {"lat": lim_lat[j], "lon": lim_lon[j]} )
                    clim_j = clim.sel(
                      {"lat": lim_lat[j], "lon": lim_lon[j]} )
                    countries_j = countries.sel(
                      {"lat": lim_lat[j], "lon": lim_lon[j]} )    
                    gender_j = gender_j.to_dataframe().reset_index(drop = True)
                    clim_j   =   clim_j.to_dataframe().reset_index(drop = True)
                    countries_i.append( countries_j.to_dataframe(
                      ).reset_index(drop = True) )

                    # Calculamos la población afectada
                    countries_i[j][var_n] = gender_j["band_data"]
                    countries_i[j][v] =   clim_j["band_data"]
                    countries_i[j] = countries_i[j].set_index("band_data")
                    countries_i[j].index.name = a_n[a]
                    countries_i[j][name_p[i]] = (
                      countries_i[j][v] * countries_i[j][var_n] )
                    countries_i[j] = countries_i[j].groupby(a_n[a]).sum()
                    countries_i[j].index = countries_i[j].index.astype(int)
                  
                  # Calculamos el porcentaje de afectados
                  countries_i = pd.concat(countries_i).groupby(a_n[a]).sum()
                  countries_i[name_pp[i]] = ( 100 * countries_i[name_p[i]]
                    / countries_i[var_n] )

                  df_iso[cols] = countries_i[cols]

          # Afectados climáticos totales
          df_iso[name_t] = df_iso[name_p].sum(axis = 1)
          df_iso[name_tp] = ( 100 * df_iso[name_t] / df_iso[var_n] )
          for i, v in enumerate(name_c):
            df_iso[v]  = df_iso[name_ci[i]].sum(axis = 1)
            df_iso[name_cp[i]] = 100 * df_iso[v] / df_iso[var_n]
          df_iso.to_csv( f"{d_f[d]}{file_n}" )

          # Quitamos el archivo demográfico del disco
          os.remove( path_g )

          print("\nVariable processed.\n")