/*
  NON-INVASIVE CABLE FAULT DETECTION
  ESP32 + Analog Hall Effect Sensor

  Connections:
  Hall +  -> ESP32 3.3V
  Hall G  -> ESP32 GND
  Hall A0 -> ESP32 GPIO34
  Hall D0 -> Not connected
*/

const int HALL_PIN = 34;

const int NUM_SAMPLES = 20;
const int SAMPLE_DELAY = 20;

float baseline = 0.0;

const float WARNING_THRESHOLD = 10.0;
const float FAULT_THRESHOLD = 25.0;


// Read averaged Hall sensor value
float readHallSensor()
{
    long total = 0;

    for (int i = 0; i < NUM_SAMPLES; i++)
    {
        total += analogRead(HALL_PIN);
        delayMicroseconds(500);
    }

    return (float)total / NUM_SAMPLES;
}


// Calculate percentage deviation
float calculateDeviation(float value)
{
    if (baseline <= 0)
        return 0;

    return abs(value - baseline) / baseline * 100.0;
}


// Calibrate sensor
void calibrateSensor()
{
    Serial.println();
    Serial.println("================================");
    Serial.println("       SENSOR CALIBRATION");
    Serial.println("================================");

    Serial.println("Keep cable in NORMAL condition.");
    Serial.println("Do not move Hall sensor.");
    Serial.println("Calibration starts in 3 seconds...");

    delay(3000);

    float total = 0;

    for (int i = 0; i < 100; i++)
    {
        total += readHallSensor();
        delay(20);
    }

    baseline = total / 100.0;

    Serial.print("BASELINE=");
    Serial.println(baseline, 2);

    Serial.println("CALIBRATION_COMPLETE");
    Serial.println();
}


void setup()
{
    Serial.begin(115200);

    delay(1000);

    analogReadResolution(12);

    pinMode(HALL_PIN, INPUT);

    Serial.println();
    Serial.println("========================================");
    Serial.println(" NON-INVASIVE CABLE FAULT DETECTOR");
    Serial.println(" ESP32 + HALL EFFECT SENSOR");
    Serial.println("========================================");

    calibrateSensor();
}


void loop()
{
    float hallValue = readHallSensor();

    float deviation = calculateDeviation(hallValue);

    String status;

    if (deviation < WARNING_THRESHOLD)
    {
        status = "NORMAL";
    }
    else if (deviation < FAULT_THRESHOLD)
    {
        status = "WARNING";
    }
    else
    {
        status = "FAULT";
    }

    Serial.print("ADC=");
    Serial.print(hallValue, 2);

    Serial.print(",Deviation=");
    Serial.print(deviation, 2);

    Serial.print("%,Status=");
    Serial.println(status);

    delay(SAMPLE_DELAY);
}
