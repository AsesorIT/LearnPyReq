#!/usr/bin/python

import requests as req
import re

resp = req.get("http://www.asesorit.com")

content = resp.text

stripped = re.sub('<[^<]+?>', '', content)
print(stripped)
