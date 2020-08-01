# Resulve Prueba

This (little) backend API is running with Flask microframework for solve a described problem [here](https://github.com/resuelve/prueba-ing-backend)

## Requirements

Python >= 3.6

## instalation

- clone this repository

- move to folder

- Project require some dependecies for working

  `pip install -r requirements.txt`

### Development

1.  For run development server

    `python app.js`

2. Should be running `http://localhost:9000`


### Production

For run production server, flask require a WSGI server, which is installed with dependencies [Gunicorn](https://gunicorn.org/)

`gunicorn -w 4 app:app`

It will run at PORT=8000 by default



## Testing request

```
[
   {
      "nombre":"El Rulo",
      "goles_minimos":10,
      "goles":9,
      "sueldo":30000,
      "bono":15000,
      "sueldo_completo": 14250,
      "equipo":"rojo"
   }
]
```
