# BLE RGB Light Controller with Matplotlib Colors

A Python script that controls Bluetooth Low Energy (BLE) RGB lights using the full matplotlib color palette. This enhanced version allows you to use any of matplotlib's named colors to control your RGB light.

## Features
- 🎨 Access to all matplotlib named colors (148 colors!)
- 💡 Power on/off functionality
- 🎯 Direct connection using device MAC address
- 🌈 Custom RGB value support
- 📊 Color values automatically converted from matplotlib's color system
- 🔌 No system Bluetooth pairing required

## Requirements
- Python 3.7+
- Required packages:
  - `bleak`
  - `matplotlib`
- Compatible BLE RGB light
- Windows 10+ / macOS / Linux with Bluetooth support

## Installation

1. Clone this repository:
```bash
git clone https://github.com/noahmerhai/BledControl
```

2. Install required packages:
```bash
pip install bleak matplotlib
```

## Configuration
Edit these constants in `bled.py` to match your device:
```python
DEVICE_MacAdress = "be:ff:90:00:7f:cd"  # Your device's MAC address
CHARACTERISTIC_UIUD = "0000fff3-0000-1000-8000-00805f9b34fb"
```

## Usage

1. Run the script:
```bash
python bled.py
```

2. Available commands:
- Use any matplotlib color name (e.g., `crimson`, `darkturquoise`, `mediumspringgreen`)
- Type `rgb` for custom RGB values (0-255)
- Type `off` to turn off the light
- Type `on` to turn on the light
- Type `quit` to exit

## Color Examples
Some popular matplotlib colors you can use:
- `red`, `green`, `blue`
- `cyan`, `magenta`, `yellow`
- `darkred`, `lightgreen`, `navy`
- `pink`, `orange`, `purple`
- `gold`, `silver`, `indigo`
- And many more!

## Command Protocol

### Color Command Structure
```python
[0x7E, 0x07, 0x05, 0x03, R, G, B, 0x10, 0xEF]
```
- R, G, B: Color values (0-255)

### Power Command Structure
```python
[0x7E, 0x04, 0x04, 0x01/0x00, 0x00, 0x00, 0x00, 0x00, 0xEF]
```
- 0x01: Power ON
- 0x00: Power OFF

## Device Details
- Service UUID: 0000fff0-0000-1000-8000-00805f9b34fb
- Characteristic UUID: 0000fff3-0000-1000-8000-00805f9b34fb

## Troubleshooting

### Connection Issues
1. Verify your device's MAC address matches `DEVICE_MacAdress` in the script
2. Ensure Bluetooth is enabled on your computer
3. Keep the light within Bluetooth range
4. Remove device from system Bluetooth settings if previously paired

### Color Issues
1. Check matplotlib color name spelling
2. Try basic colors first (red, blue, green)
3. Use `rgb` command for precise color control

## Advanced Features
- Automatic color conversion from matplotlib's color space to RGB values
- Color name validation using matplotlib's color database
- Value clamping for RGB inputs (ensures values stay within 0-255)

## Contributing
Feel free to:
- Open issues for bugs
- Suggest new features
- Submit pull requests
- Share compatible device models

## Dependencies
- [Bleak](https://github.com/hbldh/bleak) - BLE communication
- [Matplotlib](https://matplotlib.org/) - Color management

## License
[Choose your license]

## Acknowledgments
- Built using Bleak for BLE communication
- Color management powered by Matplotlib
- Protocol reverse engineered from original light control app
