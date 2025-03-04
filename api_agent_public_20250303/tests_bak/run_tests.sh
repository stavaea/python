#!/bin/bash
pytest --alluredir=./allure-results
allure serve ./allure-results