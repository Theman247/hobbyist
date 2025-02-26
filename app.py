from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Route to execute Python script
@app.route("/run-script", methods=["GET"])
def run_script():
    try:
        result = subprocess.run(["python", "Fault_Code_Finder.py"], capture_output=True, text=True)
        return jsonify({"message": result.stdout})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)