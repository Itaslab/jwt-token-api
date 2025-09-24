import time
import jwt
import requests
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_ACCOUNT_INFO = {
    "client_email": "c000441@teco-prod-dl-openwater-0d8d.iam.gserviceaccount.com",
    "private_key": """-----BEGIN PRIVATE KEY-----
TU_CLAVE_PRIVADA_AQUÍ
-----END PRIVATE KEY-----""",
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
