# Non-Invasive Cable Fault Detection using ESP32

An ESP32-based non-invasive cable fault detection system that uses an analog Hall-effect sensor to monitor electromagnetic field variations around an electrical cable.

## 📌 Project Overview

This project demonstrates a non-invasive approach to detecting abnormal conditions in electrical cables by sensing changes in the surrounding electromagnetic field.

The system combines:

- ESP32-based sensor acquisition
- Analog Hall-effect sensing
- Baseline calibration
- Percentage deviation analysis
- Moving-average filtering using Python
- Electromagnetic signal simulation using MATLAB

The project is divided into hardware detection, Python-based signal processing, and MATLAB-based simulation.

## 🎯 Objectives

- Detect variations in the electromagnetic field around a cable without directly cutting or modifying the cable.
- Process Hall-effect sensor readings and classify the cable condition as **NORMAL, WARNING, or FAULT**.
- Simulate electromagnetic signal variations under normal and fault conditions using MATLAB.

## 🛠️ Hardware Components

- ESP32 Development Board
- Analog Hall-effect Sensor
- Electrical Cable
- 3.3 V Power Supply
- Connecting Wires
- USB Cable

## 💻 Software & Tools

- Arduino IDE
- Python
- MATLAB
- GitHub

## ⚙️ System Working

The system works in the following stages:

1. The Hall-effect sensor is positioned near the electrical cable.
2. The ESP32 reads the analog electromagnetic field response through GPIO34.
3. During startup, the system performs calibration under normal cable conditions.
4. The measured baseline value is stored.
5. Subsequent sensor readings are compared with the baseline.
6. The percentage deviation is calculated.
7. Based on the deviation, the system classifies the condition as:
   - **NORMAL**
   - **WARNING**
   - **FAULT**
8. Python receives the ESP32 serial data and applies a moving-average filter.
9. MATLAB is used to simulate electromagnetic signal variations and analyze the frequency spectrum using FFT.

## 🔌 ESP32 Connections

| Hall Sensor | ESP32 |
|---|---|
| VCC | 3.3 V |
| GND | GND |
| Analog Output (A0) | GPIO34 |
| Digital Output (D0) | Not connected |

## 📐 Fault Detection Logic

The system calculates the percentage deviation from the calibrated baseline:

```text
Deviation (%) = |Measured Value - Baseline| / Baseline × 100
