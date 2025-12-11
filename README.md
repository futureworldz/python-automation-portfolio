# Python Automation Portfolio
**Author:** Santosh Venkata | **Role:** Solutions Engineer

## Overview
This repository contains a collection of Python scripts designed to automate common integration engineering tasks, including API health monitoring, data logging, and logic processing.

## Tools
* **Language:** Python 3.x
* **Libraries:** `requests`, `datetime`, `random`, `time`
* **Concepts:** REST API polling, JSON parsing, CSV logging, Error Handling

## Script Descriptions

### 1. API Health Monitor (`api_monitor.py`)
* **Function:** A script that continuously polls a target API endpoint to check for "200 OK" status codes.
* **Features:**
  * Uses `try/except` blocks to handle network failures without crashing.
  * Timestamps every check for audit logs.
  * Simulates an "Alert" system when downtime is detected.

### 2. FX Data Logger (`Loggerscript.py`)
* **Function:** Connects to a live Financial API to track USD/GBP exchange rates.
* **Features:**
  * Parses nested JSON data to extract real-time rates.
  * Appends data to a CSV file (`fx_data.csv`) for historical analysis.
  * Runs on an automated loop with `time.sleep()`.

### 3. Logic Engine (`guessing_game.py`)
* **Function:** An interactive program demonstrating state management and loops.
* **Features:**
  * Implements `while` loops for continuous user input.
  * Uses conditional logic (`if/else`) to guide user decisions.
  * Manages "Game State" (counting attempts and enforcing limits).
