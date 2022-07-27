#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sathwik
"""

from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    Name:str
    Age:int 
    section:str 

class Product(BaseModel):
    name:str 
    price:int 
    discount:int 
    discounted_price:float

app=FastAPI()

@app.get("/user/admin")
def admin():
    return {"This is a admin page"}


#creating the profile using Basemodel
@app.post("/adduser")
def adduser(profile:Profile):
    return Profile

#calculating the discounted price of a product
@app.post("/addproduct")
def addproduct(product:Product):
    product.discounted_price =product.price-(product.price*product.discount)/100
    return product













