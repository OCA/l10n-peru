Utilitario para generar el archivo de ubigeo a partir de la información de INEI
=================================================================================

**NOTA**: Necesita la librería python 'xlrd'

1. Descargar el excel de todo el Ubigeo de la web del Instituto Nacional de
   Estadística e Informática(INEI) de Perú. Utilizar la 'BÚSQUEDA POR UBICACIÓN
   GEOGRÁFICA' dejando los filtros para Departamento, Provincia y Distrito con el valor
   'TODOS'. Hay que tener en cuenta que no debe renombrarse el archivo que se
   descarga y deben mantenerse sus mayúsculas y minúsculas:

   http://webinei.inei.gob.pe:8080/sisconcode/web/ubigeo/listaBusquedaUbigeoPorUbicacionGeograficaXls/5/1/1/null/null/null

2. Mover el archivo descargado 'rptUbigeo.xls' a la carpeta gen_src
3. Ejecutar:

        python gen_data_toponym.py
4. Se generará un archivo ubigeo_data.xml en la carpeta wizard que sustituirá el
   anterior
