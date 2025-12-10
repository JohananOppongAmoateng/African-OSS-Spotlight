#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies for Tailwind
cd theme/static_src
npm install
cd ../..

# Build Tailwind CSS
python manage.py tailwind build

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate --no-input
