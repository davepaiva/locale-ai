from chalice import Chalice  #AWS library for packaging, deploying and managing severless APIs
import psycopg2              #used to connect to a PSQL database and run queries
from decimal import Decimal
from datetime import datetime


<<<<<<< HEAD
app = Chalice(app_name='locale-api')
app.debug = True
=======
app = Chalice(app_name='locale-api')  # Init chalice app
>>>>>>> 5bbcbe14393594b98f48a7d6eec5830ab4c61034

def create_conn():    #function to try to esatblish a connection the database, return the connection object
    conn = None
    try:
        conn = psycopg2.connect(dbname='XRides', user='davepaiva', password='davepaivapassword', host='locale-ai.cbx79mt5d5sd.ap-south-1.rds.amazonaws.com', port='5432')
    except: 
        print('cannot connect')
    
    return conn


@app.route('/', methods = ['POST'])  # POST method endpoint
def index():
    req_data = app.current_request.to_dict()  #stores the http request data
    query_params = req_data['query_params']    # stores all the data passed through querry parameters

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


    conn = create_conn()  #call the unction to create a connection
    cur = conn.cursor()
# insert the data to respective tables:
    cur.execute("INSERT INTO drivers ( driver_id, vehicle_model_id) VALUES (%s, %s) ;", (driver_id_data, vehicle_model_id_data, ))
    cur.execute("INSERT INTO riders (user_id) VALUES (%s) ;", (user_id_data, ))
    cur.execute("INSERT INTO rides (user_id_fk, driver_id_fk, booking_id, package_id, travel_type_id, from_area_id, to_area_id, from_city_id, to_city_id, from_date, to_date, online_booking, booking_created, from_lat, from_long, to_lat, to_long) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ;", (user_id_data, driver_id_data, booking_id_data, package_id_data, travel_type_id_data, from_area_id_data, to_area_id_data, from_city_id_data, to_city_id_data, from_date_data, to_date_data, online_booking_data, booking_created_data, from_lat_data, from_long_data, to_lat_data, to_long_data, ))
    conn.commit()
    cur.close()  
    conn.close()  #close connection
    

    return {
        "message" : "successfully inserted into database with:",
        "riderid": user_id_data,
        "driverid": driver_id_data,
        "bookingid": booking_id_data

    }






