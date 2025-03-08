from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

@app.route("/")
def home():
    return jsonify({"message": "Welcome to TommyDevs!"})

@app.route("/calculate_ohms_law", methods=["GET"])
def calculate_ohms_law():
    try:
        voltage = request.args.get("voltage", type=float)
        current = request.args.get("current", type=float)
        resistance = request.args.get("resistance", type=float)

        # Ensure at least two values are provided
        values = [voltage, current, resistance]
        provided_values = sum(v is not None for v in values)

        if provided_values < 2:
            return jsonify({"error": "Please provide at least two values: voltage, current, or resistance."}), 400

        # Solve for the missing value
        if voltage is None:
            voltage = current * resistance
            formula_used = "V = I * R"
        elif current is None:
            if resistance == 0:
                return jsonify({"error": "Resistance cannot be zero when solving for current."}), 400
            current = voltage / resistance
            formula_used = "I = V / R"
        elif resistance is None:
            if current == 0:
                return jsonify({"error": "Current cannot be zero when solving for resistance."}), 400
            resistance = voltage / current
            formula_used = "R = V / I"
        else:
            formula_used = "All values were provided; no calculation needed."

        return jsonify({
            "voltage": voltage,
            "current": current,
            "resistance": resistance,
            "formula_used": formula_used,
            "message": "Calculation successful!"
        })

    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numeric values only."}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Ensure it runs on port 5000