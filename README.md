# BledControl

A Python script to control Bluetooth Low Energy (BLE) RGB lights using the Bleak library. This script allows you to control RGB lights that use the FFF0/FFF3 service/characteristic UUID protocol.

## Features
- Connect to BLE RGB lights
- Control lights with predefined colors (red, green, blue, white, purple, yellow)
- Set custom RGB values
- Power on/off functionality
- Simple command-line interface

## Requirements
- Python 3.7+
- `bleak` library
- A compatible BLE RGB light
- Windows 10+ / macOS / Linux with Bluetooth support

## Installation
1. Clone this repository:
```bash
git clone https://github.com/noahmerhai/BledControl
```

2. Install required package:
```bash
pip install bleak
```

## Usage
1. Make sure your Bluetooth is turned ON
2. Do NOT connect to the light through your system's Bluetooth settings
3. Run the script:
```bash
python light_control.py
```

4. Available commands:
- Type a color name: `red`, `green`, `blue`, `white`, `purple`, `yellow`
- Type `rgb` to enter custom RGB values (0-255)
- Type `off` to turn off the light
- Type `quit` to exit the program

## Protocol Details
The script communicates with the light using the following command structure:

```python
# Color command structure:
[0x7E, 0x07, 0x05, 0x03, R, G, B, 0x10, 0xEF]

# Power command structure:
[0x7E, 0x04, 0x04, ON/OFF, 0x00, 0x00, 0x00, 0x00, 0xEF]
```

Where:
- `R`, `G`, `B` are values between 0-255
- `ON/OFF` is 0x01 for on, 0x00 for off

## Compatibility
This script is designed for BLE RGB lights using:
- Service UUID: 0000fff0-0000-1000-8000-00805f9b34fb
- Characteristic UUID: 0000fff3-0000-1000-8000-00805f9b34fb

## Troubleshooting
- Ensure the light is powered on and within range
- Make sure no other devices are connected to the light
- If connection fails, try removing the device from your system's Bluetooth settings

## Contributing
Feel free to open issues or submit pull requests for improvements.

## Acknowledgments
- Based on reverse engineering of the light's Bluetooth protocol through Jadx and Ehome light apk
- Uses the [Bleak](https://github.com/hbldh/bleak) library for BLE communication
