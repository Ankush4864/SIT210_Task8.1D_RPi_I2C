# SIT210
# Ankush Singla
# 2210994864

# Import necessary libraries for I2C communication and time management
import smbus
import time

# Variables to customize the program

# Time interval in seconds between sensor readings
TIME_BETWEEN_READINGS = 1

# Define threshold values for different brightness levels
TOO_BRIGHT = 200  # Lux level for "too bright"
BRIGHT = 150      # Lux level for "bright"
MEDIUM = 100      # Lux level for "medium"
DARK = 50         # Lux level for "dark"
TOO_DARK = 30     # Lux level for "too dark"

# Setup the I2C address for the light sensor
SENSOR = 0x23

# Define the sensor mode for continuous high-resolution measurements
CONTINUOS_HIG_RES_MODE = 0x13

# Initialize the I2C communication bus
bus = smbus.SMBus(1)

# Function to read and return the light reading from the sensor
def getLightReading():
    # Read a block of data from the sensor in high-resolution mode
    reading = bus.read_i2c_block_data(SENSOR, CONTINUOS_HIG_RES_MODE)
    # The lux value is in position 1 within the data block
    return reading[1]

# Function to determine the brightness ranking based on lux level
def getBrightnessRanking(lux):
    if lux > TOO_BRIGHT:
        return "too bright"
    elif lux > BRIGHT:
        return "bright"
    elif lux > MEDIUM:
        return "medium"
    elif lux > DARK:
        return "dark"
    else:
        return "too dark"

# Main function that continuously reads and prints the light level
def main():
    while True:
        # Get the current light level from the sensor
        lightLevel = getLightReading()
        # Determine the brightness ranking based on the lux reading and print it
        print("Light level is " + getBrightnessRanking(lightLevel))
        # Wait for the specified time interval before the next reading
        time.sleep(TIME_BETWEEN_READINGS)

# Entry point of the program, ensures that the 'main' function is executed
if __name__ == "__main__":
    main()
