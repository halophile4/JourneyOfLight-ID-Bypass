from mitmproxy import http

def request(flow: http.HTTPFlow):
    if "accounts.7doc.com.cn/app/sdk/do_certification" in flow.request.pretty_url:
        print("[*] Intercepted certification request!")
        flow.response = http.Response.make(
            200,  # Status code
            b'{"retCode":0,"retMsg":"success","data":{}}',  # Body
            {"Content-Type": "application/json"}  # Headers
        )
