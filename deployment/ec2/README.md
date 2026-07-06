# Deploying to a plain EC2 instance (no Docker, no Elastic Beanstalk)

These steps are only for this folder — nothing here is read automatically by
any AWS tool. You SSH in and run them yourself.

1. Launch an Ubuntu (or Amazon Linux) EC2 instance, open port 8000 (or 80 if
   you put nginx in front) in its security group.

2. SSH in, then:

   ```
   sudo apt update && sudo apt install -y python3-venv python3-pip git
   git clone https://github.com/tirth314/ML-projects.git
   cd ML-projects
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirment.txt
   pip install gunicorn
   ```

3. Quick test:

   ```
   gunicorn --bind 0.0.0.0:8000 app:application
   ```

   Visit http://<your-ec2-public-ip>:8000 — if the form loads, it works.
   Ctrl+C to stop it before going to the next step.

4. Run it permanently as a service:

   ```
   sudo cp deployment/ec2/flaskapp.service /etc/systemd/system/flaskapp.service
   sudo systemctl daemon-reload
   sudo systemctl enable flaskapp
   sudo systemctl start flaskapp
   sudo systemctl status flaskapp   # should say "active (running)"
   ```

5. (Optional) Put nginx in front on port 80, proxying to 127.0.0.1:8000, so
   you don't need to expose port 8000 directly or run gunicorn as root.
