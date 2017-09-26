# Request Header Parser Microservice

------

## Requirements
- Django==1.10


## Install
In the terminal
```

$ cd request_header_microservice
$ pip install -r requriements.txt
$ python manage.py runserver
```

## Example usage:
```
http://127.0.0.1:8000/api/whoami/
```

## Example output
```
{"ipaddress": "127.0.0.1", "language": "en-US,en;q=0.5", "software": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0"}
```


Have fun... :)