from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

#Simulating a database of vehicles
vehicle = [
   
    {
        "id": 2,
        "name": "City Shuttle",
        "image": "https://via.placeholder.com/800x400?text=City+Shuttle",
        "price_per_seat": 30,
        "rows": 4,
        "booked_seats": [0, 0]
    }
]

@app.route('/')
def index():
    return render_template('index.html', vehicle=vehicle)

@app.route('/book', methods=['POST'])
def book_seats():
    data = request.json
    vehicle_id = data.get('vehicle_id')
    seats = data.get('seats')
    date = data.get('date')
    
    # Here you would normally save this to a real database
    print(f"Booking confirmed for Vehicle {vehicle_id}: Seats {seats} on {date}")
    
    return jsonify({"status": "success", "message": "Booking successful!"})

if __name__ == '__main__':
    app.run(debug=True)
