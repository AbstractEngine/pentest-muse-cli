# Pentest Muse

Pentest Muse is an AI assistant tailored for cybersecurity professionals. It can help penetration testers brainstorm ideas, write payloads, analyze code, and perform reconnaissance. It can also take actions, execute command line codes, and iteratively solve complex tasks. 

## Pentest Muse Web App

In addition to this command-line tool, we are excited to introduce the [Pentest Muse Web Application](https://www.pentestmuse.ai)! The web app has access to the latest online information, and would be a good AI assistant for your pentesting job.

## Disclaimer

This tool is intended for legal and ethical use only. It should only be used for authorized security testing and educational purposes. The developers assume no liability and are not responsible for any misuse or damage caused by this program.

## Requirements

- Python 3.12 or later
- Necessary Python packages as listed in `requirements.txt`

## Setup

### Standard Setup

1. Clone the repository:

   ```
   git clone https://github.com/pentestmuse-ai/PentestMuse
   cd PentestMuse
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
   
### Alternative Setup (Package Installation)

Install Pentest Muse as a Python Package:

   ```
   pip install .
   ```
   
## Running the Application
### Chat Mode (Default)

In the chat mode, you can chat with pentest muse and ask it to help you brainstorm ideas, write payloads, and analyze code. Run the application with:

```
python run_app.py
```

or

```
pmuse
```

### Agent Mode (Experimental)

You can also give Pentest Muse more control by asking it to take actions for you with the agent mode. In this mode, Pentest Muse can help you finish a simple task (e.g., 'help me do sql injection test on url xxx'). To start the program with agent model, you can use:

```
python run_app.py agent
```

or

```
pmuse agent
```

## Selection of Language Models
### Managed APIs 
You can use Pentest Muse with our managed APIs after signing up at www.pentestmuse.ai/signup. After creating an account, you can simply start the pentest muse cli, and the program will prompt you to login.

### OpenAI API keys
Alternatively, you can also choose to use your own OpenAI API keys. To do this, you can simply add argument `--openai-api-key=[your openai api key]` when starting the program. 

## Contact

For any feedback or suggestions regarding Pentest Muse, feel free to reach out to us at contact@pentestmuse.ai or [join our discord](https://discord.gg/5cY35u99Nr). Your input is invaluable in helping us improve and evolve.
