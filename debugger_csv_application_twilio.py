import json
import csv
from flask import Flask, request, redirect, jsonify


app = Flask(__name__)

# @app.route("/voiceWebhook", methods=['GET', 'POST'])
# def answer_call():
#     #time.sleep(4) 
#     params = request.form.to_dict()
#     resp = VoiceRespons()
#     # Read a message aloud to the caller
#     resp.say("hello world!", voice='alice')

#     return str(resp)


@app.route("/SimpleDebugger", methods=['GET', 'POST'])
def debugger():  
    file = 'csv_debugger.csv'


    request_dict = request.form.to_dict()


    items = ['Timestamp', 'Level', 'Sid', 'AccountSid'] #these are the fields from the payload that we'd like to have.
    new_params = {x:request_dict[x] for x in items}
    payload_dict = json.loads(request_dict['Payload']) #but some relevant parts are within nested dictionaries,
    new_params['ErrorCode'] = payload_dict['error_code'] #like error code, and message
    new_params['Message'] = payload_dict['more_info']['msg']

    if payload_dict['more_info']['url'] == "http://something.unexpected.com/":
        with open(file, mode='a', newline='') as debuggerCSVfile:
            debuggerCSVwriter = csv.writer(debuggerCSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            row = list(new_params.values())
            debuggerCSVwriter.writerow(row)
        return '', 200
    else:    
        return '', 200



@app.route("/SimpleDebuggerFilter", methods=['GET', 'POST'])
def debugger():  

    ### CSV 
    file = 'simple_csv_debugger_FILTER.csv'
    request_dict = request.form.to_dict()

   
    if validation == True:
        items = ['Timestamp', 'Level', 'Sid', 'AccountSid'] #these are the fields from the payload that we'd like to have.
        new_params = {x:request_dict[x] for x in items}
        payload_dict = json.loads(request_dict['Payload']) #but some relevant parts are within nested dictionaries,
        new_params['ErrorCode'] = payload_dict['error_code'] #like error code, and message
        new_params['Message'] = payload_dict['more_info']['msg']

        if payload_dict['more_info']['url'] == "http://ed23dcf3.ngrok.io/voiceWebhook":
            with open(file, mode='a', newline='') as debuggerCSVfile:
                debuggerCSVwriter = csv.writer(debuggerCSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                row = list(new_params.values())
                debuggerCSVwriter.writerow(row)
            return '', 200
        else:    
            return '', 200
    else:
        return '', 400


@app.route("/SafeDebuggerFilter", methods=['GET', 'POST'])
def debugger():  

    ## VALIDATION
    # Your Auth Token from twilio.com/user/account
    auth_token = os.environ['AUTH_TOKEN']
    validator = RequestValidator(auth_token)
    url = 'http://.ngrok.io/debugger' ## add your URL
    twilio_signature = request.headers["X-Twilio-Signature"]
    validation = validator.validate(url, params, twilio_signature)
    
    ### CSV 
    file = 'safee_csv_debugger_FILTER.csv'
    request_dict = request.form.to_dict()

   
    if validation == True:
        items = ['Timestamp', 'Level', 'Sid', 'AccountSid'] #these are the fields from the payload that we'd like to have.
        new_params = {x:request_dict[x] for x in items}
        payload_dict = json.loads(request_dict['Payload']) #but some relevant parts are within nested dictionaries,
        new_params['ErrorCode'] = payload_dict['error_code'] #like error code, and message
        new_params['Message'] = payload_dict['more_info']['msg']

        if payload_dict['more_info']['url'] == "http://ed23dcf3.ngrok.io/voiceWebhook":
            with open(file, mode='a', newline='') as debuggerCSVfile:
                debuggerCSVwriter = csv.writer(debuggerCSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                row = list(new_params.values())
                debuggerCSVwriter.writerow(row)
            return '', 200
        else:    
            return '', 200
    else:
        return '', 400




if __name__ == "__main__":
    app.run(debug=True)