# fastapi-dev
A very simple first attempt of using FastAPI. The concept and some of the code is copied from a functional application 
which uses Flask OpenAPI3.  

This example exposes an endpoint that receives a nautobot webhook event then
just prints the event content. The code doesn't perform any other processing than that.  

## file layout
* app - main application folder
  * `main.py` - contains the bootstrap for either running the app from a command line or as a wsgi
  * `.env` - contains the app inventory environment
  * `event_test_client.py` - a test client 
  * test - unit/py test (no tests so far)
    * mock_data - folder containing mock data
      * [README.md](./tests/mock_data/README.md)
  * models - contains pydantic models
    * `nautobot.py` - Nautobot device event model
  * static - meant for any static files such as images, CSS, etc. but could contain Javascript
  * routers - endpoint routes are defined here
    * `webhook.py` - exposes a nautobot webhook event receiver 


## run app
The following examples assume a python virtual environment is available in `.venv`

### run from python
```shell
.venv/bin/python -m app.main

```

### run as uvicorn
```shell
.venv/bin/uvicorn app.main:app
```