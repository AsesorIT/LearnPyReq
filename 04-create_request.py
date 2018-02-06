#!/usr/bin/python

import requests as req

resp = req.request(method='GET', url="http://www.nic.cl")
print(resp.text)
