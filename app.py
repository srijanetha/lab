from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        print("success")
        print("form data: ",request.form)
        return "registration done"
    return render_template('register.html')
if __name__=='__main__':
    app.run()