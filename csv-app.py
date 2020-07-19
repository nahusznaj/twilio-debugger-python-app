import json
import csv
from flask import Flask, request

app = Flask(__name__)

@app.route("/write-csv", methods=['POST'])
def writingCSV():
    file = 'debugger-app/testcsv.csv'

    request_dict = request.form.to_dict() # this will transform the POST request payload into a dictionary
    print(request_dict) #to double check, print it in the terminal
    
    with open(file, mode='a', newline='') as CSVfile:
        CSVwriter = csv.writer(CSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        row = list(request_dict.values())
        CSVwriter.writerow(row)
        return '', 200

if __name__ == "__main__":
    app.run(debug=True)