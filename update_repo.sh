#!/bin/bash

cd /home/ubuntu/chess_data/chess-data-pipeline

# Check for updates
git fetch origin main

# Compare the current branch with the remote branch
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse @{u})

if [ $LOCAL != $REMOTE ]; then
    git pull origin main
fi

