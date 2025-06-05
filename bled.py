import asyncio
import matplotlib
from bleak import BleakClient, BleakScanner
import sys

# Constants for your specific device
DEVICE_MacAdress ="be:ff:90:00:7f:cd"
CHARACTERISTIC_UIUD = "0000fff3-0000-1000-8000-00805f9b34fb"
#Gets all the colors from matplotlib
mplColors = list(matplotlib.colors.cnames.keys())


def create_color_command(r, g, b):
    """Create the command bytes for setting a color"""
    return bytes([
        0x7E,  # Start byte
        0x07,  # Length
        0x05,  # Command type
        0x03,  # RGB sub-command
        r,     # Red value
        g,     # Green value
        b,     # Blue value
        0x10,  # Mode
        0xEF   # End byte
    ])

def create_power_command(on=True):
    """Create the command bytes for power on/off"""
    return bytes([
        0x7E,  # Start byte
        0x04,  # Length
        0x04,  # Command type
        0x01 if on else 0x00,  # On/Off
        0x00,  # Mode
        0x00,  # Value
        0x00,  # Value
        0x00,  # Value
        0xEF   # End byte
    ])

async def find_light_device():
    """Scan for the specific light device using its MacAdress"""
    print("Scanning for your light...")
    devices = await BleakScanner.discover()
    
    for device in devices:
        print(device.address)
        if device.address.lower() == DEVICE_MacAdress:
            return device.address
    return None

async def main():
    # Find the device
    address = await find_light_device()
    if not address:
        print(f"Could not find the light device with MacAdress: {DEVICE_MacAdress}")
        print("Make sure the light is turned on and in range.")
        return

    print(f"Found light at {address}")

    try:
        async with BleakClient(address) as client:
            print("Connected to the light!")
            
            # Turn on the light first
            await client.write_gatt_char(CHARACTERISTIC_UIUD, create_power_command(True))
            print("Light turned on successfully!")
            
            while True:
                print("\nAvailable commands:")
                print("- Color names: " + ", ".join(mplColors))
                print("- 'rgb': Enter custom RGB values")
                print("- 'off': Turn off the light")
                print("- 'quit': Exit program")
                
                color_input = input("\nEnter your choice: ").lower()
                
                if color_input == 'quit':
                    print("Turning off light and exiting...")
                    await client.write_gatt_char(CHARACTERISTIC_UIUD, create_power_command(False))
                    break
                
                if color_input == 'rgb':
                    try:
                        r = int(input("Enter red value (0-255): "))
                        g = int(input("Enter green value (0-255): "))
                        b = int(input("Enter blue value (0-255): "))
                        r = max(0, min(255, r))  # Clamp values between 0-255
                        g = max(0, min(255, g))
                        b = max(0, min(255, b))
                    except ValueError:
                        print("Invalid input. Please enter numbers between 0-255.")
                        continue
                
                elif color_input in mplColors:
                    r, g, b = tuple(int(x * 255) for x in matplotlib.colors.to_rgb(color_input))
                    if color_input == 'off':
                        await client.write_gatt_char(CHARACTERISTIC_UIUD, create_power_command(False))
                        print("Light turned off")
                        continue
                elif color_input == 'on':
                    await client.write_gatt_char(CHARACTERISTIC_UIUD, create_power_command(True))
                    print("Light turned on")
                    continue
                else:
                    print(f"Unknown command. Please try again.")
                    continue
                
                # Send the color command
                try:
                    command = create_color_command(r, g, b)
                    await client.write_gatt_char(CHARACTERISTIC_UIUD, command)
                    print(f"Set color to: {color_input if color_input != 'rgb' else f'R:{r} G:{g} B:{b}'}")
                except Exception as e:
                    print(f"Error sending command: {e}")

    except Exception as e:
        print(f"Connection error: {e}")
        print("Try running the program again. If the problem persists, make sure the light is in range and powered on.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Unexpected error: {e}")