#!/bin/bash

echo "🚀 GitHub Push Setup"
echo "===================="
echo ""
read -p "Enter your GitHub username: " USERNAME
echo ""

if [ -z "$USERNAME" ]; then
    echo "❌ Username cannot be empty!"
    exit 1
fi

echo "Setting up remote..."
git remote add origin https://github.com/$USERNAME/voice-clone-pdf-reader.git

echo "Switching to main branch..."
git branch -M main

echo ""
echo "✅ Setup complete!"
echo ""
echo "Now run this command to push:"
echo "  git push -u origin main"
echo ""
echo "Note: You may need to create the repository at:"
echo "  https://github.com/new"
echo "  Name: voice-clone-pdf-reader"
echo ""
