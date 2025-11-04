
import flask as fl
import serial, time

try:
    arduino = serial.Serial('COM4',9600,timeout=1)
    time.sleep(2)
except serial.SerialException as e:  
    print(f"Error: arduino not connected! {e}")
    arduino = None

app = fl.Flask(__name__)

@app.route('/')
def index():
    return fl.render_template('index.html')


@app.route('/get_data/')
def getSensorData():
    if not arduino:
        return fl.jsonify({"error": "Arduino não conectado"})

    command = 'T'
    arduino.write(command.encode())
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8', errors='replace').strip()
        values = line.split(";")

        if len(values) >= 3:
            return fl.jsonify({
                "temperature": values[0],
                "humidity": values[1],
                "lightIntensity": values[2],
            })
        else:
            return fl.jsonify({"error": f"No valid data detected: {line}"})
    else:
        return fl.jsonify({"error": "No Data Available"})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader = False)