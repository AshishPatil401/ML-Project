from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
        
    return "CI/CD pipeline has been established..."


if __name__=="__main__":
    app.run(debug=True)
    