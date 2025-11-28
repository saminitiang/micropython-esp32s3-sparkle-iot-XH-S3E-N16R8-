class BLEMidi:
    def __init__(self, name='BLE-MIDI'):
        self.name = name
        print('[BLE MIDI] Init device:', name)

    def send_note_on(self, note, velocity):
        print('[BLE] NOTE ON', note, velocity)

    def send_note_off(self, note, velocity):
        print('[BLE] NOTE OFF', note, velocity)

    def send(self, midi_bytes):
        print('[BLE] SEND RAW:', midi_bytes)
