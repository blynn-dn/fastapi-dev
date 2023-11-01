# fastapi-dev
A very simple fist attempt of using FastAPI.  This example exposes an
endpoint that receives a nautobot webhook event.  

## file layout
* app - main application folder
  * `main.py` - contains the bootstrap for either running the app from a command line or as a wsgi
  * `.env` - contains the app inventory environment
  * `event_test_client.py` - a test client 
  * test - unit/py test (no tests so far)
    * mock_data - folder containing mock data
      * [README.md](./tests/mock_data/README.md)


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