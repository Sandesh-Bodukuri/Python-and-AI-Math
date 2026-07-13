# 1. Threat Registry (Database of known malicious entities)
THREAT_DB = {
    "malicious_ips": {"192.168.1.99", "10.0.0.66"},
    "banned_countries": {"china", "russia", "north korea"}
}

# 2. Raw Stream of Incoming Server Logs (List of dictionaries)
raw_logs = [
    {"ip": "192.168.1.15", "location": "  india  ", "status": "200 SUCCESS"},
    {"ip": "192.168.1.99", "location": "USA", "status": "403 DENIED"},
    {"ip": "172.16.25.4", "location": "russia ", "status": "200 SUCCESS"},
]

print("================ SECURITY MONITOR ================")

# 3. Processing and Threat Intel Verification Loop
for index, log in enumerate(raw_logs, start=1):
    # Data Sanitization
    ip_addr = log["ip"]
    country = log["location"].strip().lower()
    status_code = log["status"]
    
    # Evaluation Logic using Set Membership (Super fast O(1) checking)
    is_malicious_ip = ip_addr in THREAT_DB["malicious_ips"]
    is_banned_zone = country in THREAT_DB["banned_countries"]
    
    # Determine Threat Severity Flag
    if is_malicious_ip or is_banned_zone:
        flag = "🚨 CRITICAL THREAT DETECTED"
    else:
        flag = "✅ CLEAN TRAFFIC"
        
    # 4. Clean Metric Output Dashboard
    print(f"Log #{index} | Source: {ip_addr} ({country.upper()})")
    print(f"Status : {status_code}")
    print(f"Verdict: {flag}")
    print("-" * 50)

print("==================================================")