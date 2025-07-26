import random

# Normal ranges for simulation
NORMAL_RANGES = {
    "Heart Rate (bpm)": (60, 100),
    "Oxygen Saturation (%)": (95, 100),
    "Body Temperature (°C)": (36.5, 37.5),
    "Hydration Level (%)": (50, 65)
}

def simulate_vitals():
    vitals = {}
    for vital, (low, high) in NORMAL_RANGES.items():
        value = round(random.uniform(low - 10, high + 10), 1)
        vitals[vital] = value
    return vitals

def check_vitals(vitals):
    print("📡 Simulated Astronaut Health Check:\n")
    all_ok = True
    for vital, value in vitals.items():
        low, high = NORMAL_RANGES[vital]
        status = "✅ Normal" if low <= value <= high else "⚠️ Warning"
        if status != "✅ Normal":
            all_ok = False
        print(f"{vital}: {value} → {status}")
    
    print("\n🚀 Overall Status:", "🟢 Stable" if all_ok else "🟠 Needs Attention")

if __name__ == "__main__":
    vitals = simulate_vitals()
    check_vitals(vitals)
