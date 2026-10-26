# parking-management-system
A menu-driven Python Parking Management System for vehicle entry, exit, slot allocation, automatic fee calculation and revenue reports.
A menu-driven Python application that automates the working of a parking lot: vehicle entry, slot allocation, exit processing, automatic fee calculation and revenue reporting.

Mini Project for Python Programming, BCA (Section 24BCA1/B), Chandigarh University.

Problem Statement

Manual parking lots depend on paper tickets and hand calculation. This causes:

No live view of free and occupied slots
Fee calculation errors and disputes with drivers
Lost or reused tickets and unrecorded cash (revenue leakage)
No records for reports or decisions

This project replaces the manual process with a simple software system that records every vehicle, tracks every slot and calculates every fee by fixed rules.

Objectives
Automate vehicle entry and exit
Allocate slots separately for cars and bikes
Show real-time slot availability
Calculate parking fees automatically
Keep a permanent log of completed parkings
Generate a revenue report
Features
Vehicle entry: records the plate number and vehicle type, and assigns the first free slot
Duplicate check: a vehicle that is already parked cannot be entered again
Full-lot handling: shows a message when no slot of that type is free
Vehicle exit: finds the vehicle, calculates the duration and fee, and frees the slot
Slot status: shows free and occupied slots for each vehicle type
Revenue report: shows vehicles served and total revenue, overall and by vehicle type
History log: every completed parking is saved to parking_log.csv
Input handling: plate numbers are converted to upper case and extra spaces are removed
Parking Rules
Vehicle type	Slots	Rate per hour
Car	5	Rs 20
Bike	5	Rs 10
Fee = number of hours x hourly rate
Part hours are rounded up to the next full hour
The minimum charge is 1 hour
Tools and Technologies Used

Programming language

Python 3

Python standard library modules (no external libraries needed)

csv - writes and reads the parking history log
math - rounds the parking duration up to the next hour (ceil)
os - checks whether the log file already exists
datetime - records entry and exit time and finds the duration

Programming concepts applied

Object-oriented programming (a ParkingLot class with methods)
Dictionaries to store slots and vehicle records
File handling with CSV
Conditional statements and loops
Menu-driven command-line interface
Input validation

Development tools

Visual Studio Code - code editor
Python extension for VS Code
Git - version control
GitHub - hosting the repository

Storage

CSV file (parking_log.csv) for completed parking records

Interface

Command-line (terminal) menu
System Design

The program is built around a single class, ParkingLot.

Method	Purpose
park(plate, type)	Validates the type, rejects duplicates, assigns the first free slot, stores the entry time
exit(plate)	Finds the vehicle, calculates duration and fee, frees the slot, writes the record to the log
status()	Displays free and occupied slots for each vehicle type
report()	Reads the log and totals vehicles served and revenue by type
find_vehicle(plate)	Searches all slots for a plate number

Working flow

Entry: the operator enters the plate number and vehicle type. The system validates them and assigns a free slot.
Occupancy: the system keeps track of which slots are taken and which are free.
Exit: the system calculates the duration and fee, frees the slot and saves the record.
Report: totals are calculated from the saved records.
Project Structure
parking-management-system/
|-- parking_system.py     # main program
|-- parking_log.csv       # created automatically when a vehicle exits
|-- screenshots/          # output screenshots
|-- README.md
How to Run

Requirements: Python 3.8 or later. No libraries need to be installed.

Clone the repository or download it as a ZIP:
   git clone https://github.com/JayantaRaj34/parking-management-system.git
Open the folder in VS Code (or any terminal).
Run the program:
   python parking_system.py

On Mac or Linux, use python3 parking_system.py.

Menu Options
=== PARKING MANAGEMENT SYSTEM ===
1. Park vehicle
2. Exit vehicle
3. Slot status
4. Revenue report
5. Quit
