#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""

from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return {f"how are you"}

@app.get("/property")
def property():
    return "this is our property number"

@app.get("/cars")
def cars():
    return {"cars":{"mercedes","audi"}}

@app.get("/property/21")
def property():
    return "This is our property number 21"


@app.post("/adduser")
def adduser():
    return "this a user page"



