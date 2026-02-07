# NVIDIA API Test Environment

This folder contains a simple Python script to test your NVIDIA API key and explore available models.

## Setup

1.  **Get an API Key:**
    - Go to [NVIDIA API Catalog](https://build.nvidia.com).
    - Login and generate an API key.

2.  **Configure Environment:**
    - Copy `.env.example` to a new file named `.env`:
      ```bash
      cp .env.example .env
      ```
    - Open `.env` and replace the placeholder with your actual API key:
      ```
      NVIDIA_API_KEY=nvapi-your-key-here
      ```

3.  **Install Dependencies:**
    - Create a virtual environment:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      ```
    - Install the required packages:
      ```bash
      pip install openai python-dotenv
      ```

## Usage

Run the test script:

```bash
# Ensure venv is activated
source .venv/bin/activate
python3 test_nvidia_api.py
```

The script will:
1.  List the available models accessible with your key.
2.  Perform a test chat completion with `meta/llama3-70b-instruct`.

## Troubleshooting

-   **Authentication Error:** Double-check your API key in the `.env` file. ensure there are no extra spaces.
-   **Module Not Found:** Make sure you installed the dependencies (`pip install openai python-dotenv`).
