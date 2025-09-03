from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        print("succes")
        print("form data:", reqest.form)
        return "done"
    return render_template("register.html")
if __name__=='__main__':
    app.run()
