import serial
import time
import re
from collections import deque


# ==================================================
# SETTINGS
# ==================================================

PORT = "COM7"
BAUD_RATE = 115200

FILTER_WINDOW = 5

WARNING_THRESHOLD = 10.0
FAULT_THRESHOLD = 25.0


# ==================================================
# MOVING AVERAGE FILTER
# ==================================================

class MovingAverage:

    def __init__(self, size):
        self.values = deque(maxlen=size)

    def update(self, value):
        self.values.append(value)
        return sum(self.values) / len(self.values)


# ==================================================
# FAULT CALCULATION
# ==================================================

def calculate_deviation(value, baseline):

    if baseline == 0:
        return 0

    return abs(value - baseline) / baseline * 100


def get_status(deviation):

    if deviation < WARNING_THRESHOLD:
        return "NORMAL"

    elif deviation < FAULT_THRESHOLD:
        return "WARNING"

    else:
        return "FAULT"


# ==================================================
# EXTRACT ADC VALUE
# ==================================================

def extract_adc(data):

    match = re.search(
        r"ADC=([0-9]+(?:\.[0-9]+)?)",
        data
    )

    if match:
        return float(match.group(1))

    return None


# ==================================================
# MAIN PROGRAM
# ==================================================

def main():

    print("=" * 60)
    print(" NON-INVASIVE CABLE FAULT DETECTION")
    print("=" * 60)

    print("Port:", PORT)
    print("Baud:", BAUD_RATE)

    try:

        esp32 = serial.Serial(
            PORT,
            BAUD_RATE,
            timeout=1
        )

    except serial.SerialException as error:

        print("ERROR: ESP32 not connected")
        print(error)

        return

    time.sleep(2)

    print("ESP32 connected.")
    print("Waiting for sensor data...")
    print("-" * 60)

    baseline = None

    filter_data = MovingAverage(
        FILTER_WINDOW
    )

    try:

        while True:

            if not esp32.in_waiting:
                continue

            line = (
                esp32.readline()
                .decode(
                    "utf-8",
                    errors="ignore"
                )
                .strip()
            )

            if not line:
                continue

            # Get calibration baseline
            if line.startswith("BASELINE="):

                try:

                    baseline = float(
                        line.split("=")[1]
                    )

                    print(
                        f"Baseline = "
                        f"{baseline:.2f}"
                    )

                except ValueError:
                    pass

                continue

            if "CALIBRATION_COMPLETE" in line:

                print(
                    "Calibration complete."
                )

                continue

            # Extract ADC
            adc = extract_adc(line)

            if adc is None:
                continue

            # If baseline unavailable
            if baseline is None:

                baseline = adc

            # Filter
            filtered = filter_data.update(
                adc
            )

            # Calculate deviation
            deviation = calculate_deviation(
                filtered,
                baseline
            )

            # Determine status
            status = get_status(
                deviation
            )

            print(
                f"ADC={adc:.2f} | "
                f"Filtered={filtered:.2f} | "
                f"Deviation={deviation:.2f}% | "
                f"Status={status}"
            )

    except KeyboardInterrupt:

        print("\nSystem stopped.")

    finally:

        esp32.close()


if __name__ == "__main__":
    main()
