#!/usr/bin/python

import requests as req

resp = req.get("http://www.asesorit.com")
print(resp.status_code)

resp = req.get("http://asesorit.com/servicios.html")
print(resp.status_code)

