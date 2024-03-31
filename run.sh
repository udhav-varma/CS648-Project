#!/bin/bash

# Set the maximum number of attempts
MAX_ATTEMPTS=5

# Set the path to your animation rendering command
RENDER_COMMAND="your_rendering_command_here"

# Variable to keep track of the number of attempts
attempt=1

# Loop until the rendering is successful or the maximum number of attempts is reached
while true; do
    echo "Attempt $attempt: Running $RENDER_COMMAND"
    manim-slides render kruskal.py
    exit_code=$?

    # Check if the rendering was successful
    # if [ $exit_code -eq 0 ]; then
    #     echo "Rendering completed successfully!"
    #     break
    # fi

    # Check if the maximum number of attempts has been reached
    if [ $attempt -eq $MAX_ATTEMPTS ]; then
        echo "Maximum number of attempts reached. Rendering failed."
        break
    fi

    # Increment the attempt counter
    ((attempt++))

    # Wait for a short period before retrying (e.g., 5 seconds)
    sleep 5
done