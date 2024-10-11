from flask import render_template, request, jsonify,redirect, url_for

from app import create_app
from app.main.logger_setup import logger
app = create_app()

@app.route("/")
@app.route('/index')
def home():
    return render_template('index.html')
    #return render_template('test.html')

"""
Post done using the javascript front end
@app.route('/submit-option', methods=['POST'])
def submit_option():
    data = request.get_json()
    selected_option = data.get('option')
    print(f"Selected option: {selected_option}")
    #return jsonify({'status': 'success', 'selected_option': selected_option})
    return redirect(url_for('success', name={selected_option}))
"""
@app.route('/submit', methods=['POST','GET'])
def submit():
    print("Post called")
    if request.method == 'POST':
        ToolsOptions = request.form.get('Tools')
        print(f"Selected option: {ToolsOptions}")
        if ToolsOptions=="Performance":
            return redirect(url_for('performance'))
        elif ToolsOptions=="Memory profiling":
            return render_template('memoryprofile.html')
        elif ToolsOptions=="Timestamps":
            return ToolsOptions
        elif ToolsOptions=="Log Details":
            return ToolsOptions
        else:
            print("Not possible!!!")
            return ToolsOptions.get('Tools')

@app.route('/performance')
def performance():
    return render_template('performance.html')
if __name__ == '__main__':
   
   logger.info("SI Army knifer started")
   app.run( host='0.0.0.0',debug=True)