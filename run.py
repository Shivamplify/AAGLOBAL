"""Entry point. Run with: python run.py"""
import os
from app import create_app

app = create_app()

def start_scheduler():
    from apscheduler.schedulers.background import BackgroundScheduler
    from app.bot import run_bot_job
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=run_bot_job, trigger="interval", minutes=1)
    scheduler.start()

if __name__ == "__main__":
    if not os.environ.get("WERKZEUG_RUN_MAIN"):  # Prevent running twice in debug mode
        start_scheduler()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=app.config.get("DEBUG", False))
