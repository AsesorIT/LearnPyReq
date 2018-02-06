#!/usr/bin/python

import requests as req

resp = req.get("http://www.something.com")
print(resp.status_code)

resp = req.get("http://www.something.com/news/")
print(resp.status_code)

