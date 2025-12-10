#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # Exit on error

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Node.js and npm..."
# Install Node.js 24.x
curl -fsSL https://deb.nodesource.com/setup_24.x | bash -
apt-get install -y nodejs

echo "Verifying Node.js and npm installation..."
node --version
npm --version

echo "Installing Tailwind CSS dependencies..."
cd theme/static_src
npm install
cd ../..

echo "Building Tailwind CSS..."
python manage.py tailwind build

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running database migrations..."
python manage.py migrate --no-input

echo "Build completed successfully!"
