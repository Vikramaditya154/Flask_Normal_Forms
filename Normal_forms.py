from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/form',methods=['GET',"POST"])
def Form_Creation():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return form_data['na']
    return render_template('form.html')


if __name__=='__main__':
    app.run(debug=True)
