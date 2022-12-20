from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
import uuid

class User:

    def signup(self):
        print(request.form)

        # Create the user object
        user = {
            "_id" : uuid.uuid4().hex,
            "name" : request.form.get('name'),
            "email" : request.form.get('email'),
            "password" : request.form.get('password')
        }

        # Encrpyt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])


        return jsonify(user), 200 # return in json format
