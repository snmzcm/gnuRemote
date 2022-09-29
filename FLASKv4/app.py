from flask import Flask, render_template, url_for, request
import pyClasses

app = Flask(__name__)

#creating class instance to get Current OS for accurate commands
current = pyClasses.plt.system()

@app.route("/")
def HomePage():
    return render_template("index.html",compname = pyClasses.plt.node())



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    if name == '':
        name == "/kapat"
    if name == "/kapat":
        #name = "Kapatılıyor"
        kapat = pyClasses.shutdown(current)
    elif name == "/uyku":
        #name = "Uyku Moduna geçiliyor"
        uyku = pyClasses.sleepMode(current)
    elif name == "/logoff":
        lgf = pyClasses.LogOff(current)
    elif name == "/lock":
        lock = pyClasses.LockScreen(current)
        

    return render_template('index.html', name = name)

    


if __name__ == "__main__":
    app.run(debug=True,port=80)

