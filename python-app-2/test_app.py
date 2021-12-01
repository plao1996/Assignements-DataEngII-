import pytest
import requests
import app
import time

def test_url():
    assert requests.get("http://localhost:5000/mean").status_code == 200, "the site is not working"

def test_output():
    assert float(requests.get("http://localhost:5000/mean?list=1,2,3").content) == 2.0 , "mean function is incorrect"
    assert float(requests.get("http://localhost:5000/mean?list=15,25,20").content) == 20.0 , "mean function is incorrect"
    assert float(requests.get("http://localhost:5000/mean?list=5,18,22").content) == 15.0 , "mean function is incorrect"

def test_stress():
    list_time = []
    for i in range(1000):
        response = requests.get("http://localhost:5000/mean?list=15,25,20")
        list_time.append(response.elapsed.total_seconds()*1000)
    avg_time = sum(list_time)/len(list_time)
    assert avg_time < 100 
