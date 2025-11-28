import time
from ble_midi import BLEMidi
from usb_midi import USBMidiHost

ble = BLEMidi(name='ESP32S3-BLE-MIDI')
usb = USBMidiHost()

print('BLE MIDI + USB MIDI bridge started')

while True:
    msg = usb.poll()
    if msg:
        ble.send(msg)
    time.sleep(0.01)
