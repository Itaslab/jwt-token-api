import time
import jwt
import requests
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_ACCOUNT_INFO = {
    "client_email": "c000441@teco-prod-dl-openwater-0d8d.iam.gserviceaccount.com",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCzOKWbcOMsHH9y\noOJjpwXhkwLxoqE+7DjlkRe4FFXeJ+CwpTpvCGAtbrlVOaJIQ6Y8TA+roQ/zpWeN\nNbtNhR1LSAZDCdKjZY9kpJO2CZ7cYaWt01i2b2km3iCFFTOVmX2EI/djsXCKdQdL\nucnAe14xbFuuY9Xf7l/vvJPHqNzNcdnloUH8Bn+YZpzRjLxzhpfD6XGnpEyZO34e\nbhl1+S9M10RVQ4TTaQ89XYTxvkdOSSQ2iSIpZIC22G9FL73a8nfelh6pOO9/HjOx\n9Acg5hZwJSIE79XEkGw2TlFS7PXNEybvr/D562hr7Ny5l6tRSo+VvEE8RN3G2MBS\nrUmcEFZFAgMBAAECggEAGmu/8k3ul5qt6TqxlUpSsiIHnZLBnbKaYrGEoyUQUZtk\nYvZAyoycDSaVGOzRsUCT2bDG4KDyZpNcVDN3JOL6YhZAohJpJKB8xrQCeKQrcMbO\nc3VET0TWZh36AlSRUb0ahWf9+Qr4EdlV1YKSrRci2DtmuqtKJOSR7RhKWvVYc8rV\nSeMRx8Uka7AowCScl/nFJz6QfmaUH4OkC5l0WvIv2GnvoC7f8hoStBf7iJwSvUah\nc+DxNe8FQXPaiNII5Q4Hg1Mz1wBYvm6PNYnW6QuztuKZtaP9ZJ7zQzF1ySsBcwCu\nx/CF/ZXIt4KM6kJty6xmYdoget9e9zzVaOZbh1lOsQKBgQDdRCIY0Kc08NUWYglh\nl/U+uuDv6yqX3RFPSzGrdCn0buY2px3TGizD79UHN5vLTxg/rlqrbtNg4vxsN9Jn\naaHeB5SyHTxCdtkHIK7ScmTXnJ+cDaomRoqSLu8Qd7zTWQnekSz44kFI0hZZY3kq\n/EvpdAybR47QZVRqh5G1QIpzWQKBgQDPWuLdQo8gcxAMr/88KJ/Z+Ar9viSOuQSV\nCzy/toRyqrPOBKxEyDgSs3Y+n0pdwS2q0khtq4zd1nQGbQsLuAzmRirtVGefzY7p\nSgg2E2b0Hao0riKrP/U9vwQvGZE6vMsWPzy24XHPOlzJxS9kQXzg+X10TPnxEOsq\ncDCRJVq4zQKBgCjZQj44jxXr/DrkoHy+9Ay/rXU9giCFNIPiCupvSKuSqbefRJdL\ndsY5iaeKcZ2oHX7sLlsF28pAPX+xEov66WI3HhF/6jcO/+Qb+YpqiglwJdtGfooQ\nbdatCX+Ny3NtNbA8NwQ/qPPLrUqVXbI837rarNUh8dCxVFNScej3YFgJAoGAdRgc\n/tfEXY28pX2Jw94pDvzssAf9Ov+uX8BdyOF4AAz3xsKKybjLOXxQrOJlK3aYpFtl\nfVEgFnIxSSOw1ihUWIGNYkKE1hBNwN4Grwrb28UYxfEEMPLIOdsxsKtegO32PZTu\nY1QCYgTSOzr4HUSCEcWyG8gQaRqlwmxicMTIa40CgYBl+F5bEcAKvOHSLJDgw91U\nGEXcbgJAcbZMFeQEsSiIR0qNq4UkJFNcuNX/dlHeJT0SNw86Q8TXkMjgR2qVk1R6\n2fGBY7sJf1w8c3BEB6ctbAgO3UvGhTF5ggUNVtnj8TE5IKK6wZqQ4g6+vYf4WUa0\nD/Rh0rDbiCxRbNv6Be4FWA==\n-----END PRIVATE KEY-----\n",
    "token_uri": "https://oauth2.googleapis.com/token"
}

@app.route('/get-token', methods=['GET'])
def get_token():
    try:
        issued_at = int(time.time())
        expiration_time = issued_at + 3600

        payload = {
            'iss': SERVICE_ACCOUNT_INFO['client_email'],
            'scope': 'https://www.googleapis.com/auth/bigquery',
            'aud': SERVICE_ACCOUNT_INFO['token_uri'],
            'iat': issued_at,
            'exp': expiration_time
        }

        jwt_token = jwt.encode(payload, SERVICE_ACCOUNT_INFO['private_key'], algorithm='RS256')

        response = requests.post(
            SERVICE_ACCOUNT_INFO['token_uri'],
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": jwt_token
            }
        )

        token = response.json().get("access_token")
        if token:
            return jsonify({"access_token": token})
        else:
            return jsonify({"error": "Failed to retrieve access token"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

@app.route('/')
def home():
    return "API JWT Token Generator funcionando correctamente"

@app.route('/health')
def health():
    return {"status": "ok"}

