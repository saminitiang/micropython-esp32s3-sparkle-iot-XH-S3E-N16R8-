# Build Instructions MicroPython ESP32-S3 BLE MIDI

Folder ini berisi:
- src/      : kode MicroPython BLE MIDI + USB MIDI stub
- docs/     : instruksi flash dan build
- .github/  : workflow CI/CD template

Untuk build firmware sendiri:
- Gunakan ESP-IDF 5.x
- Clone MicroPython upstream
- Build target board: esp32s3
- Replace partitions.csv bila diperlukan
