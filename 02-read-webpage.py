#!/usr/bin/python

import requests as req

resp = req.get("http://www.asesorit.com")

print(resp.text)
