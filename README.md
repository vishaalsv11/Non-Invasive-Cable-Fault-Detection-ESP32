# Non-Invasive Cable Fault Detection using ESP32

An ESP32-based non-invasive cable fault detection system that uses an analog Hall-effect sensor to monitor electromagnetic field variations around an electrical cable.

## 📌 Project Overview

This project demonstrates a non-invasive approach to monitoring electrical cable conditions by sensing changes in the surrounding electromagnetic field.

The system combines:

- ESP32-based analog sensor acquisition
- Hall-effect sensing
- Baseline calibration
- Percentage deviation analysis
- Fault-status classification
- Python-based serial data processing
- Moving-average filtering
- MATLAB-based electromagnetic signal simulation and FFT analysis

The project is divided into three main parts: **ESP32 hardware detection, Python signal processing, and MATLAB simulation**.

---

## 🎯 Objectives

- Detect variations in the electromagnetic field around an electrical cable without directly modifying the cable.
- Establish a baseline sensor value during normal operation.
- Calculate the percentage deviation of subsequent sensor readings from the baseline.
- Classify the monitored condition as **NORMAL, WARNING, or FAULT**.
- Analyze simulated electromagnetic signal variations using MATLAB.

---

## 🛠️ Hardware Components

- ESP32 Development Board
- Analog Hall-effect Sensor
- Electrical Cable
- Breadboard
- 12 V AC Step-Down Transformer
- Connecting Wires
- USB Cable / Power Supply

---

## 💻 Software & Tools

- Arduino IDE
- Python
- MATLAB
- Git & GitHub

---

## ⚙️ System Working

The system operates in the following stages:

1. The Hall-effect sensor is positioned near the cable under observation.
2. The ESP32 reads the analog sensor output through GPIO34.
3. The system performs an initial calibration under normal cable conditions.
4. The average sensor value is stored as the baseline.
5. Subsequent sensor readings are compared with the baseline.
6. The percentage deviation is calculated.
7. The deviation is used to classify the cable condition.
8. Python receives the ESP32 readings through serial communication.
9. A moving-average filter is applied to reduce short-term variations.
10. MATLAB is used separately to simulate electromagnetic signal variations and perform FFT analysis.

---

## 🔌 ESP32 Connections

| Hall-effect Sensor | ESP32 |
|---|---|
| VCC | 3.3 V |
| GND | GND |
| Analog Output (A0) | GPIO34 |
| Digital Output (D0) | Not connected |

---

## 📐 Fault Detection Logic

The percentage deviation is calculated using:

```text
Deviation (%) = |Measured Value - Baseline| / Baseline × 100
