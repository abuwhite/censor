"""Main module test."""

from services.backend import Flask, request

app = Flask(__name__)

with app.test_request_context("/?value=20000"):
    assert request.path == "/"
    assert request.args["value"] == "20000"
