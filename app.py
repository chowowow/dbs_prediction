#!/usr/bin/env python
# coding: utf-8

# In[35]:


from flask import Flask


# In[36]:


import joblib


# In[37]:


app = Flask(__name__) #anything with an _ before and after is a magic number


# In[38]:


from flask import request,render_template

@app.route("/",methods=["GET","POST"])
def index():
    if request.method =="POST":
        rates = request.form.get("rates")
        print(rates)
        model1=joblib.load("regression.joblib")
        r1=model1.predict([[rates]])
        
        model2=joblib.load("tree.joblib")
        r2=model2.predict([[rates]])
        
        
        return(render_template("index.html",result1=r1,result2=r2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




