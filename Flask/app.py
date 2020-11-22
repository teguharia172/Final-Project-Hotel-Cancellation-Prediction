from flask import Flask, render_template, request, jsonify
import plotly
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go 
import json5
from sqlalchemy import create_engine
import joblib
import json

app = Flask(__name__)

pd.read_csv(r'C:\Users\teguh\Purwadhika\Final Project\hotel_final.csv')

def category_plot(
    cat_plot = 'histplot',
    cat_x = 'hotel', cat_y = 'is_canceled',
    estimator = 'count', hue = 'market_segment'):

#generate data frame from csv
    hotel = pd.read_csv(r'C:\Users\teguh\Purwadhika\Final Project\hotel_final.csv')

    if cat_plot == 'histplot':
        data = []

        for val in hotel[hue].unique():
            hist = go.Histogram(
                x = hotel[hotel[hue]==val][cat_x],
                y = hotel[hotel[hue]==val][cat_y],
                histfunc = estimator,
                name = val
            )
            data.append(hist)
        title = 'Histogram'
    
    elif cat_plot == 'boxplot':
        data = []

        for val in hotel[hue].unique():
            box = go.Box(
                x = hotel[hotel[hue]==val][cat_x],
                y = hotel[hotel[hue]==val][cat_y],
                name = val
            )
            data.append(box)
        title = 'Box'
    
    if cat_plot == 'histplot':
        layout = go.Layout(
            title = title,
            xaxis = dict(title = cat_x),
            yaxis = dict(title = 'tes'),
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
    plot = category_plot()

    list_plot = [('histplot', 'Histogram'), ('boxplot', 'Box')]
    list_x = [('hotel', 'Hotel'), ('month_year', 'Month & Year'),('booking_location', 'Booking Location'), ('market_segment', 'Market Segment')]
    list_y = [('adr', 'Average Daily Rate'), ('lead_time', 'Lead Time'), ('total_stays', 'Total Stays')]
    list_est = [('count', 'Count'), ('avg', 'Average'), ('max', 'Max'), ('min', 'Min')]
    list_hue = [('hotel', 'Hotel'), ('booking_location', 'Booking Location'), ('market_segment', 'Market Segment')]

    return render_template(

        'category.html',
        plot=plot,
        focus_plot = 'histplot',
        focus_x='hotel',
        focus_estimator='count',
        focus_hue = 'is_canceled',
        drop_plot = list_plot,
        drop_x = list_x,
        drop_y = list_y,
        drop_estimator = list_est,
        drop_hue = list_hue)




if __name__ == '__main__':

    model = joblib.load(r'C:\Users\teguh\Purwadhika\Final Project\Flask\model_hotel_base')
    app.run(debug = True)