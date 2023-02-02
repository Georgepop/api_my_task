
from flask import Flask, request, render_template

app = Flask(__name__)

s = ' '
power_on = "OFF"
color='RED'

@app.route('/',methods = ['POST', 'GET'])
def student():
    global s, color, power_on
       
    if request.method == 'POST':
        
        return render_template("index.html",s=s )
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html",s=s )



@app.route('/score', methods=['POST'])
def score():
    global s, color, power_on
    
    features = request.json
    
    if features["command"] == 'ON':
        s = color
        power_on = 'ON'
    elif features["command"] == 'OFF':
        power_on = 'OFF'
        s = 'OFF'
    elif features["command"] == 'COLOR':
        color = features["metadata"]
        if power_on == 'ON':
            s = color
    elif features["command"] == 'NEW':
        s = 'NEW COMMAND'

    else:
        pass

    return
    





if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    

