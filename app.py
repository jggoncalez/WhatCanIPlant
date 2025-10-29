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
        return fl.jsonify({"erro": "Arduino não conectado"})

    command = 'T'
    arduino.write(command.encode())
    if arduino.in_waiting > 0:
        time.sleep(1)
        line = arduino.readline().decode('utf-8', errors='replace').strip()
        values = line.split(";")

        if len(values) >= 3:
            return fl.jsonify({
                "temperature": values[0],
                "humidity": values[1],
                "lightIntensity": values[2],
            })
        else:
            return fl.jsonify({"erro": f"No valid data detected: {line}"})
    else:
        return fl.jsonify({"error": "No Data Available"})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader = False)

"""
import flask as fl
import serial
import time
import random

# Tenta conectar ao Arduino
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)
    print("✅ Arduino conectado com sucesso!")
    MOCK_MODE = False
except serial.SerialException as e:  
    print(f"⚠️ Arduino não conectado: {e}")
    print("🔧 Iniciando em MODO DE TESTE (dados simulados)")
    arduino = None
    MOCK_MODE = True

# Criação do app Flask
app = fl.Flask(__name__)  # <-- deixa o padrão, não muda o static_folder!

# --- Funções auxiliares ---
def get_mock_data():
    scenarios = [
        {"temperature": random.uniform(22, 28), "humidity": random.uniform(68, 85), "lightIntensity": random.uniform(75, 95)},
        {"temperature": random.uniform(16, 23), "humidity": random.uniform(75, 92), "lightIntensity": random.uniform(72, 90)},
        {"temperature": random.uniform(12, 20), "humidity": random.uniform(55, 90), "lightIntensity": random.uniform(45, 65)},
        {"temperature": random.uniform(18, 30), "humidity": random.uniform(55, 78), "lightIntensity": random.uniform(70, 95)},
        {"temperature": random.uniform(15, 21), "humidity": random.uniform(80, 95), "lightIntensity": random.uniform(65, 90)},
        {"temperature": random.uniform(22, 32), "humidity": random.uniform(50, 70), "lightIntensity": random.uniform(75, 95)},
        {"temperature": random.uniform(16, 27), "humidity": random.uniform(60, 80), "lightIntensity": random.uniform(75, 92)},
        {"temperature": random.uniform(10, 25), "humidity": random.uniform(50, 80), "lightIntensity": random.uniform(50, 70)},
        {"temperature": random.uniform(20, 32), "humidity": random.uniform(50, 80), "lightIntensity": random.uniform(75, 100)},
        {"temperature": random.uniform(15, 28), "humidity": random.uniform(40, 80), "lightIntensity": random.uniform(50, 75)},
        {"temperature": random.uniform(12, 24), "humidity": random.uniform(55, 85), "lightIntensity": random.uniform(50, 70)},
        {"temperature": random.uniform(18, 28), "humidity": random.uniform(60, 85), "lightIntensity": random.uniform(75, 95)},
        {"temperature": random.uniform(12, 24), "humidity": random.uniform(50, 80), "lightIntensity": random.uniform(40, 60)},
        # Cenário extra de falha / dados ruins
        {"temperature": random.uniform(5, 10), "humidity": random.uniform(20, 35), "lightIntensity": random.uniform(10, 25)},
    ]
    data = random.choice(scenarios)
    return {
        "temperature": f"{data['temperature']:.1f}",
        "humidity": f"{data['humidity']:.1f}",
        "lightIntensity": f"{data['lightIntensity']:.1f}"
    }

# --- Rotas principais ---
@app.route('/')
def index():
    return fl.render_template('index.html')

@app.route('/get_data/')
def get_sensor_data():
    if MOCK_MODE:
        print("📊 Gerando dados simulados...")
        mock_data = get_mock_data()
        print(f"   Temp: {mock_data['temperature']}°C | Humid: {mock_data['humidity']}% | Light: {mock_data['lightIntensity']}%")
        return fl.jsonify(mock_data)
    
    if not arduino:
        return fl.jsonify({"error": "Arduino não conectado"})
    
    command = 'T'
    arduino.write(command.encode())
    
    if arduino.in_waiting > 0:
        time.sleep(1)
        line = arduino.readline().decode('utf-8', errors='replace').strip()
        values = line.split(";")
        
        if len(values) >= 3:
            return fl.jsonify({
                "temperature": values[0],
                "humidity": values[1],
                "lightIntensity": values[2],
            })
        else:
            return fl.jsonify({"error": f"Dados inválidos: {line}"})
    else:
        return fl.jsonify({"error": "Sem dados disponíveis"})

@app.route('/toggle_mock/')
def toggle_mock():
    global MOCK_MODE
    MOCK_MODE = not MOCK_MODE
    status = "TESTE (Mock)" if MOCK_MODE else "REAL (Arduino)"
    return fl.jsonify({"mode": status, "mock_enabled": MOCK_MODE})

# --- Execução do servidor ---
if __name__ == '__main__':
    print("\n" + "="*50)
    if MOCK_MODE:
        print("   SERVIDOR EM MODO DE TESTE")
        print("   Dados simulados serão gerados automaticamente")
        print("   Acesse /toggle_mock/ para alternar modos")
    else:
        print("   SERVIDOR EM MODO REAL")
        print("   Conectado ao Arduino na COM4")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
"""