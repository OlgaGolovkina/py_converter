![py_converter Logo](https://apptha-blog.s3.amazonaws.com/blog/wp-content/uploads/2018/10/over.png)
# py_converter
Simple system for converting the currency. Lightweight implementation (only success pass, just a quick example for the coding interview). 
#
Python 3.7 is supported. Install all requirements, preferably within a virtualenv:
* Clone this repo
* Install pip and virtualenv:
```bash
python3 get-pip.py
pip install virtualenv
```
* Create a virtual environment:
```bash
virtualenv -p python3 venv
```
* Activate the virtual environment:
```bash
source venv/bin/activate
```
* Install requirements and set up development environment:
```bash
pip install -r requirements.txt
```
* Run server
```bash
python server.py
```
#
* In another terminal window run client:
```bash
cd convert_currency/
python client.py -t=EUR -i=input.json -o=output.json
```

> NOTE: in this case `input.json` file should be in the same directory as `client.py`.
* As a result `output.json` file will be created. 
