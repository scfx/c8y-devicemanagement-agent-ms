#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify

app = Flask(__name__)


# Verify the status of the microservice
@app.route('/health')
def health():
    return '{ "status" : "DOWN" }'


@app.route('/environment')
def environment():
    environment_data = {
        'platformUrl': os.getenv('C8Y_BASEURL'),
        'mqttPlatformUrl': os.getenv('C8Y_BASEURL_MQTT'),
        'tenant': os.getenv('C8Y_BOOTSTRAP_TENANT'),
        'user': os.getenv('C8Y_BOOTSTRAP_USER'),
        'password': os.getenv('C8Y_BOOTSTRAP_PASSWORD'),
        'microserviceIsolation': os.getenv('C8Y_MICROSERVICE_ISOLATION')
    }
    return jsonify(environment_data)


if __name__ == '__main__':
    with open("sample.txt", "a") as file_object:
        # Append 'hello' at the end of file
    file_object.write("hello")
    app.run(host='0.0.0.0', port=80)
