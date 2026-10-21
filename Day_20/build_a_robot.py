def build_robot(*parts, **features):
    print("Robot parts:")
    for part in parts:
        print(f"- {part}")
    print("Features: ")
    for key, value in features.items():
        print(f"{key}: {value}")
    print(f"Part count: {len(parts)}")
    print(f"Feature count: {len(features)}")

build_robot("Wheels", "Claw", "Camera", name="Bolt", colour="Blue")