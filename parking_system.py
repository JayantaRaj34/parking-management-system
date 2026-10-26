
import csv
import math
import os
from datetime import datetime

LOG_FILE = "parking_log.csv"
RATES = {"car": 20, "bike": 10}          # Rs per hour
CAPACITY = {"car": 5, "bike": 5}         # slots per vehicle type
FMT = "%Y-%m-%d %H:%M:%S"


class ParkingLot:
    def __init__(self):
        # slot -> record, per vehicle type
        self.slots = {v: {i: None for i in range(1, n + 1)}
                      for v, n in CAPACITY.items()}
        self.revenue = 0

    def find_vehicle(self, plate):
        for vtype, slots in self.slots.items():
            for no, rec in slots.items():
                if rec and rec["plate"] == plate:
                    return vtype, no
        return None

    def park(self, plate, vtype):
        plate = plate.upper().strip()
        if vtype not in RATES:
            return "Invalid vehicle type (use car/bike)."
        if self.find_vehicle(plate):
            return f"{plate} is already parked."
        for no, rec in self.slots[vtype].items():
            if rec is None:
                self.slots[vtype][no] = {"plate": plate,
                                         "in": datetime.now()}
                return f"{plate} parked at {vtype.upper()} slot {no}."
        return f"No {vtype} slots free."

    def exit(self, plate, out_time=None):
        plate = plate.upper().strip()
        found = self.find_vehicle(plate)
        if not found:
            return "Vehicle not found."
        vtype, no = found
        rec = self.slots[vtype][no]
        out_time = out_time or datetime.now()
        hours = max(1, math.ceil((out_time - rec["in"]).total_seconds() / 3600))
        fee = hours * RATES[vtype]
        self.slots[vtype][no] = None
        self.revenue += fee
        self._log(plate, vtype, no, rec["in"], out_time, fee)
        return (f"{plate} exited. Duration: {hours} hr(s). "
                f"Fee: Rs {fee}")

    def _log(self, plate, vtype, slot, t_in, t_out, fee):
        new = not os.path.exists(LOG_FILE)
        with open(LOG_FILE, "a", newline="") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["plate", "type", "slot", "in", "out", "fee"])
            w.writerow([plate, vtype, slot, t_in.strftime(FMT),
                        t_out.strftime(FMT), fee])

    def status(self):
        lines = []
        for vtype, slots in self.slots.items():
            free = sum(1 for r in slots.values() if r is None)
            lines.append(f"{vtype.upper()}: {free}/{len(slots)} free")
            for no, rec in slots.items():
                state = rec["plate"] if rec else "-"
                lines.append(f"   Slot {no}: {state}")
        return "\n".join(lines)

    def report(self):
        if not os.path.exists(LOG_FILE):
            return "No completed parkings yet."
        with open(LOG_FILE) as f:
            rows = list(csv.DictReader(f))
        total = sum(int(r["fee"]) for r in rows)
        by_type = {}
        for r in rows:
            by_type[r["type"]] = by_type.get(r["type"], 0) + int(r["fee"])
        out = [f"Vehicles served: {len(rows)}", f"Total revenue: Rs {total}"]
        out += [f"  {k}: Rs {v}" for k, v in by_type.items()]
        return "\n".join(out)


def main():
    lot = ParkingLot()
    menu = ("\n=== PARKING MANAGEMENT SYSTEM ===\n"
            "1. Park vehicle\n2. Exit vehicle\n"
            "3. Slot status\n4. Revenue report\n5. Quit")
    while True:
        print(menu)
        ch = input("Choice: ").strip()
        if ch == "1":
            print(lot.park(input("Plate no: "),
                           input("Type (car/bike): ").lower().strip()))
        elif ch == "2":
            print(lot.exit(input("Plate no: ")))
        elif ch == "3":
            print(lot.status())
        elif ch == "4":
            print(lot.report())
        elif ch == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
