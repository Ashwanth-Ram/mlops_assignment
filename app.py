#%%
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqlconnector://root:passasar@localhost:3306/login",echo=True)
conn=engine.connect()

#%%
conn.execute('INSERT INTO acc VALUES("admin",1234);')

#%%
conn.execute('INSERT INTO acc VALUES("user1",100);')

#%%
result=conn.execute('SELECT * FROM acc;')
cred=[]
for i in result:
    cred+=[i]
if ('admin','1234') in cred:
    print('yes')
#%%
from flask import Flask,render_template,request
app=Flask(__name__)
import pickle

model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/checkpost',methods=['post'])
def check():
    inp=[]
    cred=[]
    for i in request.form.values():
        inp+=[i]
    inp=tuple(inp)
    result=conn.execute('SELECT * FROM acc;')
    for i in result:
        cred+=[i]
    if inp in cred:
        return render_template('success.html')
    else:
        return render_template('fail.html')
    
@app.route('/predict',methods=['post'])
def predict():
    features=[]
    for i in request.form.values():
        features+=[float(i)]
    pred = model.predict([features])
    if(pred==1):
        return render_template("predict.html",a="placed")
    else:
        return render_template("predict.html",a="not placed")
if(__name__=='__main__'):
    app.run(host='localhost',port=5000)
#%%