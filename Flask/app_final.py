from flask import Flask, render_template,url_for,request
from flask_material import Material
import json
import pandas as pd
import numpy as np
# import plotly.express as px
import joblib
import plotly 
import plotly.graph_objs as go


hotel2 = pd.read_csv(r'C:\Users\teguh\Purwadhika\Final Project\Flask\data\hotel_final.csv')


app = Flask(__name__)
Material(app)

def category_plot(
    cat_plot = 'histplot',
    cat_x = 'hotel', cat_y = 'adr',
    estimator = 'count', hue = 'is_canceled'):

    # generate dataframe tips.csv
    # tips = pd.read_csv('./static/tips.csv')

    # jika menu yang dipilih adalah histogram
    if cat_plot == 'histplot':
        # siapkan list kosong untuk menampung konfigurasi hist
        data = []
        # generate config histogram dengan mengatur sumbu x dan sumbu y
        for val in hotel2[hue].unique():
            hist = go.Histogram(
                x=hotel2[hotel2[hue]==val][cat_x],
                y=hotel2[hotel2[hue]==val][cat_y],
                histfunc=estimator,
                name=val
            )
            #masukkan ke dalam array
            data.append(hist)
        #tentukan title dari plot yang akan ditampilkan
        title='Count Plot'
    elif cat_plot == 'boxplot':
        data = []

        for val in hotel2[hue].unique():
            box = go.Box(
                x=hotel2[hotel2[hue] == val][cat_x], #series
                y=hotel2[hotel2[hue] == val][cat_y],
                name = val
            )
            data.append(box)
        title='Box'
    # menyiapkan config layout tempat plot akan ditampilkan
    # menentukan nama sumbu x dan sumbu y
    if cat_plot == 'histplot':
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title='tes'),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    else:
        layout = go.Layout(
            title=title,
            xaxis=dict(title=cat_x),
            yaxis=dict(title=cat_y),
            # boxmode group digunakan berfungsi untuk mengelompokkan box berdasarkan hue
            boxmode = 'group'
        )
    #simpan config plot dan layout pada dictionary
    result = {'data': data, 'layout': layout}

    #json.dumps akan mengenerate plot dan menyimpan hasilnya pada graphjson
    graphJSON = json.dumps(result, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview')
def preview():
    df = pd.read_csv(r'C:\Users\teguh\Purwadhika\Final Project\Flask\data\hotel_final.csv')
    return render_template('preview.html', df_view = df.head(100))

@app.route('/analyze', methods = ['POST'])
def analyze ():
    if request.method == 'POST':
        hotel = request.form['Hotel Choice'] 
        location = request.form['location']
        lead_time = request.form['lead_time']
        market_segment = request.form['market_segment']
        deposit_type = request.form['deposit_type']
        parking_space = request.form['parking_space']
        total_of_special_request = request.form['total_of_special_requests']
        is_previously_cancelled = request.form['is_previously_cancelled']
        is_repeated_guest = request.form['is_repeated_guest']
        is_booking_changes = request.form['is_booking_changes']
        customer_type = request.form['customer_type']
        total_stays = request.form['total_stays']
        total_guest = request.form['guests']
    
        hotel = int(hotel)
        location = int(location)
        lead_time = int(lead_time)
        parking_space = int(parking_space)
        total_of_special_request = int(total_of_special_request)
        is_previously_cancelled = int(is_previously_cancelled)
        is_repeated_guest = int(is_repeated_guest)
        is_booking_changes = int(is_booking_changes)
        total_stays = int(total_stays)
        total_guest = float(total_guest)

        data = {
            "hotel_encoded" : hotel,
            "booking_location_encoded" : location,
            "lead_time" : lead_time,
            "market_segment" : market_segment,
            'deposit_type': deposit_type,
            'parking_space':parking_space,
            'total_of_special_requests':total_of_special_request,
            'is_previously_cancelled':is_previously_cancelled,
            'is_repeated_guest':is_repeated_guest,
            'is_booking_changes':is_booking_changes,
            'customer_type':customer_type,
            'total_stays': total_stays,
            'guests': total_guest}

    df_predict = pd.DataFrame(data = data, index = [1])

    model = joblib.load(r'C:\Users\teguh\Purwadhika\Final Project\Flask\model_hotel_base')
    prediction = model.predict_proba(df_predict)
    prediction_fix = model.predict(df_predict)
    round_prediction = round(100 * prediction[0][1],2)
    round_prediction_confirmed = round(100 * prediction[0][0],2)
    print(f'The Chances of cancellation is {round(100 * prediction[0][1],2)}%')
    print(f'This Booking Will Be : {prediction_fix[0]}')

    final_prediction = ""

    if prediction_fix[0] == 0:
        final_prediction = "Confirmed"
    
    else :
        final_prediction = "Cancelled"






    return render_template('index.html', hotel = hotel,
            location = location,
            lead_time = lead_time,
            market_segment = market_segment,
            deposit_type = deposit_type,
            parking_space = parking_space,
            total_of_special_request = total_of_special_request,
            is_previously_cancelled = is_previously_cancelled,
            is_repeated_guest = is_repeated_guest,
            is_booking_changes = is_booking_changes,
            customer_type = customer_type,
            total_stays = total_stays,
            total_guest = total_guest,
            round_prediction = round_prediction,
            prediction = prediction,
            round_prediction_confirmed = round_prediction_confirmed,
            final_prediction = final_prediction)


@app.route('/category')
def category():
    return render_template('category.html')


    
    








if __name__ == '__main__':
    app.run(debug = True)