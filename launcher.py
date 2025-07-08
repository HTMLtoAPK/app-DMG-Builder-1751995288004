
import os
import sys
import subprocess

# The user's main script file name, passed from the HTML app state
REAL_SCRIPT = 'app.py'

def main():
    # Path to the bundled executable
    executable_path = os.path.dirname(sys.executable)
    
    # Path to the main user script, which we bundle into Resources
    real_script_path = os.path.join(executable_path, '..', 'Resources', REAL_SCRIPT)
    
    # Path to the SSL certificate file, also in Resources
    cert_path = os.path.join(executable_path, '..', 'Resources', 'cacert.pem')

    # Set the SSL_CERT_FILE environment variable for the subprocess
    env = os.environ.copy()
    if os.path.exists(cert_path):
        env['SSL_CERT_FILE'] = cert_path

    # Run the user's actual script
    subprocess.run([sys.executable, real_script_path], env=env)

if __name__ == '__main__':
    main()
