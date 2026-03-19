# CyberAI-Sentinel: AI-Powered SOC Monitoring 🚀

CyberAI-Sentinel is an intelligent Security Operations Center (SOC) tool designed to monitor logs in real-time, detect threats using both rule-based and AI-driven methods, and provide automated responses and alerts.

## 🌟 Key Features

- **Real-Time Log Monitoring**: Automatically watches log files (e.g., `sample.log`) for changes using high-performance file system observers.
- **Rule-Based Threat Detection**: Identifies common attack patterns like brute-force login attempts using optimized regular expressions.
- **AI-Powered Anomaly Detection**: Leverages Machine Learning (`IsolationForest`) to detect sophisticated behavioral anomalies that static rules might miss.
- **Automated Response**:
  - **Instant Alerts**: Sends real-time notifications via Telegram.
  - **Active Blocking**: Automatically blocks malicious IPs using `iptables` (Linux) or simulated blocking (Windows).
- **Backend API**: A robust FastAPI-powered backend for manual analysis triggers and system status monitoring.

## 🛠️ Tech Stack

- **Core Logic**: Python 3.x
- **Web Framework**: FastAPI, Uvicorn
- **Monitoring**: Watchdog
- **Machine Learning**: Scikit-learn, Pandas
- **Alerts**: Telegram Bot API
- **Environment**: Dotenv for secure configuration

## 📂 Project Structure

```text
SOC Project/
├── app/
│   ├── main.py              # FastAPI Entry Point
│   ├── log_watcher.py       # Real-time log observer logic
│   ├── log_analyzer.py      # Pattern-based threat analysis
│   ├── anomaly_detector.py  # Machine Learning (IsolationForest)
│   ├── features.py          # Feature extraction for ML
│   ├── alerts.py            # Telegram notification system
│   └── auto_response.py     # Automated IP blocking logic
├── .env                     # Configuration (Tokens, IDs)
├── requirements.txt         # Project dependencies
├── sample.log               # Target log file for monitoring
└── README.md                # Project documentation
```

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- A Telegram Bot (for alerts)

### 2. Installation

Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the root directory:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
CHAT_ID=your_chat_id_here
```

### 4. Running the Application

Start the FastAPI server (which also launches the real-time log watcher):
```bash
uvicorn app.main:app --reload
```

- **API Interface**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Manual Analysis**: [http://127.0.0.1:8000/analyze](http://127.0.0.1:8000/analyze)

## 🔍 How it Works

1. **Log Watcher**: The system starts a background thread that monitors `sample.log`.
2. **Analysis**: When a change is detected, `log_analyzer` scans for brute-force patterns.
3. **ML Anomaly**: `anomaly_detector` extracts features like attempt frequency and timing to flag outliers.
4. **Action**: If a threat is confirmed, an alert is sent to Telegram, and the IP is immediately blocked.

---
*Built with ❤️ for Security Professionals.*
