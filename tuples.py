warehouse_location = (17.3850, 78.4867)
telemetry_record = ("Rover01", 45.2, 102.5)
device_name, speed, heading = telemetry_record
# warehouse_location[0] = 18.9990 (Type error: cannot assign values to tuple)
master_session = warehouse_location + telemetry_record

dashboard = f"""
-----------------------DASHBOARD-----------------------
Confirmed coordinates            : {warehouse_location}
-------------------------------------------------------
UNPACKED DATA:
Device Name : {device_name}
Speed       : {speed}Km/h
Heading     : {heading}°
-------------------------------------------------------
Master Tuple = {master_session}
"""
print(dashboard)