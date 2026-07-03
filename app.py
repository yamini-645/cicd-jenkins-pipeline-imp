from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 CI/CD Pipeline Automation using Jenkins</h1>

    <p><b>🟢 Application Status:</b> Running Successfully</p>

    <p>
    This project demonstrates an end-to-end CI/CD pipeline that automatically builds, pushes, and deploys a Dockerized Flask application using Jenkins Pipeline.
    </p>

    <h3>Pipeline Highlights</h3>

    <ul>
        <li>✅ Source Code: GitHub</li>
        <li>✅ CI Tool: Jenkins Pipeline</li>
        <li>✅ Containerization: Docker</li>
        <li>✅ Image Registry: Docker Hub</li>
        <li>✅ Deployment: Automated using <code>deploy.sh</code></li>
    </ul>

    <p><b>📦 Version:</b> v2.0</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)