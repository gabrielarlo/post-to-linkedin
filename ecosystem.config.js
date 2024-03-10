module.exports = {
    apps : [{
      name: 'linkedin-post',
      script: 'poetry run python main.py',
      cron_restart: '0 8 * * 1-5', // This cron job runs at 8:00 AM on every weekday (Monday to Friday)
      autorestart: false, // Prevents the script from restarting outside the scheduled time
      watch: false
    }]
  };
  