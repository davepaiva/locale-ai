from chalice import Chalice
import psycopg2
from decimal import Decimal
from datetime import datetime


app = Chalice(app_name='locale-api')

def create_conn():
    conn = None
    try:
        conn = psycopg2.connect(dbname='XRides', user='davepaiva', password='davepaivapassword', host='locale-ai.cbx79mt5d5sd.ap-south-1.rds.amazonaws.com', port='5432')
    except: 
        print('cannot connect')
    
    return conn


@app.route('/', methods = ['POST'])
def index():
    req_data = app.current_request.to_dict()
    query_params = req_data['query_params']

    booking_id_data = int(query_params['booking_id'])
    user_id_data = int(query_params['user_id'])
    vehicle_model_id_data = int(query_params['vehicle_model_id'])
    package_id_data = int(query_params['package_id'])
    travel_type_id_data = int(query_params['travel_type_id'])
    from_area_id_data = int(query_params['from_area_id'])
    to_area_id_data =int(query_params['to_area_id'])
    from_city_id_data =int(query_params['from_city_id'])
    to_city_id_data = int(query_params['to_city_id'])
    from_date_data = int(query_params['from_date'])
    to_date_data = int(query_params['to_date'])
    online_booking_data = int(query_params['online_booking'])
    booking_created_data = int(query_params['booking_created'])
    from_lat_data = Decimal(query_params['from_lat'])
    from_long_data = Decimal(query_params['from_long'])
    to_lat_data = Decimal(query_params['to_lat'])
    to_long_data = Decimal(query_params['to_long'])
    driver_id_data = int(query_params['driver_id'])


    conn = create_conn()
    cur = conn.cursor()

    cur.execute("INSERT INTO drivers ( driver_id, vehicle_model_id) VALUES (%s, %s)", (driver_id_data, vehicle_model_id_data, ))
    cur.execute("INSERT INTO riders (user_id) VALUES (%s)", (user_id_data, ))
   # cur.execute("INSERT INTO rides (booking_id, package_id, travel_type_id, from_area_id, to_area_id, from_city_id, to_city_id, from_date, to_date, online_booking, booking_created, from_lat, from_long, to_lat, to_long) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (booking_id_data, package_id_data, travel_type_id_data, from_area_id_data, to_area_id_data, from_city_id_data, to_city_id_data, from_date_data, online_booking_data, booking_created_data, to_date_data, from_date_data, from_lat_data, from_long_data, to_lat_data, to_long_data, ))
    #cur.execute("INSERT INTO ride_info (user_id, driver_id, booking_id) VALUES (%s, %s, %s)", (user_id_data, driver_id_data, booking_created_data, ))

    return req_data





