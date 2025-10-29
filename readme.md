# What Can I Plant? / O Que Posso Plantar?

## English Version

### Overview
This project is a **plant recommendation system** inspired by Stardew Valley. It uses **real-time sensor data** from an Arduino (or simulated mock data) to suggest which plant is suitable based on **temperature, humidity, and light intensity**.

### How It Works
1. The Arduino collects environmental data:
   - **Temperature** (°C)
   - **Humidity** (%)
   - **Light Intensity** (%)
2. Flask serves a **web interface** (`index.html`) showing:
   - Current sensor values
   - Recommended plant
   - Plant image
3. JavaScript fetches the data every 3 seconds and updates the page dynamically.
4. The `check()` function compares the sensor values with the ranges defined in `db.json` and returns the compatible plant.

### Arduino Components
```
        +5V
         |
         |
       [DHT11]----- DHTPIN 3 (digital)
         |
        GND

        +5V
         |
        [LDR]-----.
         |        |
       [10kΩ]     |
         |        |
        GND      LDRPIN A0 (analog)
```

- **DHT11 (DHTPIN 3)**: Digital sensor for **temperature and humidity**.
- **LDR (LDRPIN A0)**: Photoresistor forming a voltage divider with 10kΩ resistor for measuring **light intensity**.
- **+5V / GND**: Common power for sensors.
- **Serial communication**: Arduino sends data only when it receives `'T'` command from Flask.
- **Values sent**: `temperature;humidity;lightPercent` separated by semicolon.

### Installation
1. Clone the repository.
2. Install Python dependencies:
   ```bash
   pip install flask pyserial
   ```
3. Connect Arduino to your PC.
4. Run the Flask app:
   ```bash
   python app.py
   ```
5. Open your browser at `http://localhost:5000/`.

### Notes
- Plant images should be placed in `static/images/` and named exactly as in `db.json`.

---

## Versão em Português

### Visão Geral
Este projeto é um **sistema de recomendação de plantas** inspirado em Stardew Valley. Ele usa **dados de sensores em tempo real** de um Arduino (ou dados simulados) para sugerir qual planta é adequada com base em **temperatura, umidade e intensidade de luz**.

### Como Funciona
1. O Arduino coleta os dados do ambiente:
   - **Temperatura** (°C)
   - **Umidade** (%)
   - **Intensidade de Luz** (%)
2. O Flask serve uma **interface web** (`index.html`) exibindo:
   - Valores atuais dos sensores
   - Planta recomendada
   - Imagem da planta
3. O JavaScript busca os dados a cada 3 segundos e atualiza a página dinamicamente.
4. A função `check()` compara os valores dos sensores com os intervalos definidos em `db.json` e retorna a planta compatível.

### Componentes do Arduino
```
        +5V
         |
         |
       [DHT11]----- DHTPIN 3 (digital)
         |
        GND

        +5V
         |
        [LDR]-----.
         |        |
       [10kΩ]     |
         |        |
        GND      LDRPIN A0 (analog)
```

- **DHT11 (DHTPIN 3)**: Sensor digital que mede **temperatura e umidade**.
- **LDR (LDRPIN A0)**: Fotoresistor formando um divisor de tensão com resistor de 10kΩ para medir **intensidade de luz**.
- **+5V / GND**: Alimentação comum para todos os sensores.
- **Comunicação Serial**: O Arduino envia dados apenas quando recebe o comando `'T'` do Flask.
- **Valores enviados**: `temperature;humidity;lightPercent` separados por ponto e vírgula.

### Instalação
1. Clone o repositório.
2. Instale as dependências do Python:
   ```bash
   pip install flask pyserial
   ```
3. Conecte o Arduino ao PC.
4. Execute o Flask app:
   ```bash
   python app.py
   ```
5. Abra o navegador em `http://localhost:5000/`.

### Observações
- As imagens das plantas devem estar em `static/images/` e nomeadas exatamente como no `db.json`.

