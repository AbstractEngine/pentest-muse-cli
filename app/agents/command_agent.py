import subprocess
import shlex
import os
import json

class CommandAgent:
    def __init__(self, data_dir="./pentest_data/", task_id=None):
        self.data_dir = data_dir
        self.task_id = task_id
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def get_history_file_path(self):
        return os.path.join(self.data_dir, f"history_{self.task_id}.json")

    def load_history(self):
        history_file = self.get_history_file_path()
        if not os.path.exists(history_file):
            return []

        with open(history_file, "r") as file:
            return json.load(file)

    def save_history(self, history):
        history_file = self.get_history_file_path()
        with open(history_file, "w") as file:
            json.dump(history, file, indent=4)

    def save_result(self, r):
        history = self.load_history()
        # reduce the length of error and output to 1000 characters
        if len(r['error']) > 1000:
            r['error'] = r['error'][:500] + " ... " + r['error'][-500:]
        # if len(r['output']) > 1000:
        #     r['output'] = r['output'][:500] + " ... " + r['output'][-500:]
        # turn the result into a string
        r = json.dumps(r)
        history.append({"role": "system", "content": r})
        self.save_history(history)

    def execute_action(self, command):
        """
        Execute a command in the terminal and return the output.
        """
        # Save the command in the history
        history = self.load_history()
        history.append({"role": "user", "content": command})
        self.save_history(history)

        # Execute the command
        try:
            # Safely split the command into a sequence of arguments
            args = shlex.split(command)

            # Execute the command with a timeout of 60 seconds
            result = subprocess.run(args, capture_output=True, text=True, check=True, timeout=60)

            return {
                "output": result.stdout,
                "error": ""
            }
        except subprocess.TimeoutExpired:
            # Handle the timeout case
            return {
                "output": "",
                "error": "Command timed out after 60 seconds"
            }
        except subprocess.CalledProcessError as e:            
            return {
                "output": e.stdout,
                "error": e.stderr
            }
        except Exception as e:
            return {
                "output": "",
                "error": str(e)
            }
