Informe Técnico: Análisis de Impacto de la Inflación del USD en los Adultos Mayores en Cuba.

Proyecto de Ciencia de Datos - ICD & Programación
Fecha: 06/01/2025

Tema: Análisis del impacto de la inflación del tipo de cambio del dólar estadounidense (USD) en la población adulta mayor cubana.

Los adultos mayores en Cuba representan un grupo vulnerable en la población cubana, con ingresos fijos (pensiones) que no están acordes a la inflación. La devaluación del peso cubano (CUP) frente al USD en el mercado informal afecta directamente los precios de los alimentos, medicamentos y productos de aseo, impactando gravemente a este sector poblacional. Este proyecto analiza cómo la depreciación del dólar y el aumento de precios impactan la capacidad adquisitiva de este segmento poblacional, utilizando datos cuantitativos y cualitativos de múltiples fuentes, incluyendo datos diarios del precio del USD en el mercado informal entre el 15 de octubre y el 5 de diciembre de 2025 y precios de productos en USD y CUP.

Se utilizaron cinco fuentes de datos válidas y complementarias que:
·	Se almacenaron en archivos JSON usando funciones personalizadas.
·	Los precios en USD o CUP de los productos se calcularon usando el precio promedio del dólar estadounidense calculado con los datos obtenidos desde el 15 de octubre hasta el 5 de diciembre del 2025.
·	Las comparaciones entre los precios de los productos en las tiendas particulares y el precio topado impuesto por el gobierno se hicieron tomando en cuenta productos con gramaje parecido.
·	Las comparaciones entre los precios de las tiendas particulares y las estatales se hicieron tomando en cuenta el precio promedio de cada tipo de producto.

Fuentes de datos:
Datos Oficiales (ONEI)
· Contenido: Pensiones promedio, datos demográficos de adultos mayores.
· Estructura JSON: onei_datos.json
{
  "metadata": {
    "fuente": "ONEI",
    "ultima_actualizacion": "2025-11-30",
    "unidades": "CUP"
  },
  "datos": [
    {
      "año": 2024,
      "mes": 1,
      "pension_promedio": 1250,
      "indice_precios": 145.2,
      "poblacion_adultos_mayores": 2154300
    }
  ]
}

2.2. Gaceta Oficial de Cuba
· Contenido: Resoluciones y normativas sobre pensiones y subsidios.
· Estructura JSON: gaceta_normativas.json

Se usaron herramientas como:
La biblioteca utils.py que incluye:
·	Funciones para manejar los archivos JSON, algunas extraen datos específicos.
·	Funciones para realizar el cambio de precios a otra moneda.
·	Funciones específicas para crear gráficos, teniendo en cuenta los datos existentes.

El análisis se enfoca en:
·	El impacto directo de la inflación del dólar en el poder adquisitivo de los pensionados.
·	La variación del precio del dólar en el mercado informal.
·	El cumplimiento de las medidas tomadas por el gobierno para ayudar a los más vulnerables.

Se usaron gráficos como:
·	Gráfico de variación del USD: Precio del USD por día, entre el 15 de octubre y el 5 de diciembre.
·	Gráfico de cantidad de establecimientos por región: Enseña el porciento de establecimientos (estatales, particulares y agropecuarios) que hay el La Habana y más específicamente en Centro Habana.
·	Gráfico de precios promedios: Precio promedio de cada tipo de alimento representado en un gráfico de barra demostrando que tantas partes de la pensión promedio representa.
·	Gráfico de precios topados: De los productos analizados representa aquellos que tienen un precio topado, impuesto por el gobierno, con el precio que tiene realmente en cada establecimiento particular.
·	Gráfico de comparación de precios entre los establecimientos de distinta naturaleza: Toma el precio promedio de los productos en común entre las tiendas particulares, con venta en CUP, y las estatales, con venta en USD (sus precios fueron convertidos a CUP, usando la tasa promedio del dólar) y los compara con el objetivo de mostrar cual tiene preci
