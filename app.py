#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
import joblib


# In[2]:


def formatINR(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    return "".join([r] + d)


# In[3]:


app = Flask(__name__)


# In[4]:


model = joblib.load('model.pkl')
model


# In[5]:


scaler = joblib.load('scaler.pkl')
scaler


# In[6]:


@app.route("/")
def home():
    return render_template('index.html')


# In[7]:


@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        stops = request.form['stops']
        class_type = request.form['class']
        duration = float(request.form['duration'])
        days_left = int(request.form['days_left'])
        bool_mapping = {'Yes': 1, 'No': 0}
        airline_air_india = bool_mapping[request.form['airline_Air_India']]
        airline_GO_FIRST = bool_mapping[request.form['airline_GO_FIRST']]
        airline_indigo = bool_mapping[request.form['airline_Indigo']]
        airline_spicejet = bool_mapping[request.form['airline_SpiceJet']]
        airline_vistara = bool_mapping[request.form['airline_Vistara']]
        flight_uk_720 = bool_mapping[request.form['flight_UK_720']]
        flight_uk_822 = bool_mapping[request.form['flight_UK_822']]
        flight_uk_826 = bool_mapping[request.form['flight_UK_826']]
        flight_uk_828 = bool_mapping[request.form['flight_UK_828']]
        flight_uk_874 = bool_mapping[request.form['flight_UK_874']]
        class_mapping = {'Economy': 0, 'Business': 1}
        arrival_time_mapping = {'Early_Morning': 0,
                                 'Morning': 1,
                                 'Afternoon': 2,
                                 'Evening': 3,
                                 'Night': 4,
                                 'Late_Night': 5}
        stops_mapping = {'zero': 0, 'one': 1, 'two_or_more': 2}
        stops = stops_mapping[stops]
        class_type = class_mapping[class_type]
        arrival_time = arrival_time_mapping[request.form['arrival_time']]
        departure_time = arrival_time_mapping[request.form['departure_time']]
        
        data = [[stops,
                 class_type,
                 duration,
                 days_left,
                 airline_air_india,
                 airline_GO_FIRST,
                 airline_indigo,
                 airline_spicejet,
                 airline_vistara,
                 flight_uk_720,
                 flight_uk_822,
                 flight_uk_826,
                 flight_uk_828,
                 flight_uk_874,
                 arrival_time,
                 departure_time]]
        
        scaled_data = scaler.transform(data)
        pred = formatINR(round(model.predict(scaled_data)[0],2))
        return render_template('index.html',prediction_text=f"The predicted price of your flight is ₹{pred}.")


# In[ ]:


if __name__ == '__main__':
    app.run(port=8080)

