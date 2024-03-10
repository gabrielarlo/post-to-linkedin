# Post to LinkedIn

## Description

This project automates the process of posting content to a LinkedIn company page. It utilizes Python for scripting, the LinkedIn API for posting content, and integrates generative text models (like GPT-3) for content creation. It's designed to help businesses maintain active engagement on LinkedIn with minimal manual effort.

## Getting Started

### Prerequisites

- Python 3.x
- Poetry for Python dependency management
- Access to LinkedIn API and necessary permissions for posting content
- An OpenAI API key if using GPT-3 for content generation

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gabrielarlo/post-to-linkedin.git
   cd post-to-linkedin
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install --no-root
   ```

3. Copy the `.env.example` file to `.env` and fill in your LinkedIn credentials, OpenAI API key, and other environment variables as needed.

### Configuration

1. Edit the `main.py` (or your main script file) to customize the content generation and posting logic.

2. In `ecosystem.config.js`, set the `cron_restart` value to schedule when your script runs (if using PM2 for scheduling).

### Usage

1. To manually post content to LinkedIn using the script:

   ```bash
   poetry run python main.py
   ```

2. To start the PM2 job that schedules your posts:

   ```bash
   pm2 start ecosystem.config.js
   ```

   Ensure PM2 is set to restart on system reboot:

   ```bash
   pm2 save
   ```

## Features

- Automated content generation using AI (e.g., GPT-3).
- Scheduled posting to LinkedIn company pages.
- Easy to customize and extend for different content types and schedules.

## Contributing

We welcome contributions to the Post to LinkedIn project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Your Name - your@email.com
- Project Link: [https://github.com/gabrielarlo/post-to-linkedin.git](https://github.com/gabrielarlo/post-to-linkedin.git)
