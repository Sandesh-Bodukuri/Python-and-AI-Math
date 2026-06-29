# --- The Nested Data Structure ---
# Structure: Dictionary -> List -> Dictionary -> Tuple & Strings
warehouse_data = {
    "warehouse_id": "WH-HYD-01",
    "location": "Hyderabad, India",
    "active_zones": [
        {
            "zone_name": "Cold Storage",
            "manager": "Amit Sharma",
            "telemetry": (12.5, 85.0),  # Tuple: (Temperature Celsius, Humidity %)
            "inventory": [
                {"item_id": "ITEM101", "name": "Vaccines", "qty": 2500},
                {"item_id": "ITEM102", "name": "Enzymes", "qty": 450}
            ]
        },
        {
            "zone_name": "Ambient Electronics",
            "manager": "Neha Reddy",
            "telemetry": (24.0, 45.5),  # Tuple: (Temperature Celsius, Humidity %)
            "inventory": [
                {"item_id": "ITEM201", "name": "Microcontrollers", "qty": 12000},
                {"item_id": "ITEM202", "name": "OLED Screens", "qty": 0}  # Out of stock
            ]
        }
    ]
}

# --- Nested Data Parsing Loop ---

print("=" * 50)
print(f"PARSING REPORT FOR: {warehouse_data['warehouse_id']} ({warehouse_data['location']})")
print("=" * 50)

# 1. Access the list of zones inside the parent dictionary
for zone in warehouse_data["active_zones"]:
    print(f"\n[Zone: {zone['zone_name'].upper()}]")
    print(f"Manager: {zone['manager']}")
    
    # 2. Parse the Tuple (Unpacking immutable metrics)
    temp, humidity = zone["telemetry"]
    print(f"Environment Status -> Temp: {temp}°C | Humidity: {humidity}%")
    
    print("Inventory Details:")
    # 3. Access the nested list of dictionaries inside the zone
    for item in zone["inventory"]:
        item_name = item["name"]
        quantity = item["qty"]
        
        # Add tracking alert logic during parsing
        status = "IN STOCK" if quantity > 0 else "!!! OUT OF STOCK !!!"
        
        print(f"  - {item_name:<18} | Qty: {quantity:<5} | Status: {status}")
        
print("\n" + "=" * 50)