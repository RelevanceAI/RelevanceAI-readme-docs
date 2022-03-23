
#!/usr/bin/env python3

import requests

from requests import Request

async def run_request():
    req = Request(
        method=method.upper(),
        url=self._dashboard_request_url,
        headers=self.auth_header,
        json=request_body,
        # params=parameters if method.upper() == "GET" else {},
    ).prepare()
    with requests.Session() as s:
        response = s.send(req)


