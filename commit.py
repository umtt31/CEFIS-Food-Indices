import subprocess
from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d")
commit_message = f"Commit for {current_date}"

subprocess.run(["git", "add", "*"])
subprocess.run(["git", "commit", "-m", commit_message])