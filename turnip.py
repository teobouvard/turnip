import requests
import os
import logging
import smtplib

from email.message import EmailMessage

store = os.environ["HOME"] + "/.config/turnip"
log_file = store + "/log"
db = store + "/ip"

logging.basicConfig(filename=log_file, level=logging.DEBUG)


def get_last_ip():
    if not os.path.isfile(db):
        return None
    else:
        with open(db, "r") as f:
            old_ip = f.read()
            return old_ip


def send_mail(ip_addr):
    msg = EmailMessage()
    msg["Subject"] = "Change of IP address"
    msg["From"] = ""
    msg["To"] = ""
    msg["Content"] = ip_addr

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.send_message(msg)
    server.quit()


def save_current_ip(ip_addr):
    os.makedirs(os.path.dirname(db), exist_ok=True)
    with open(db, "w+") as f:
        f.write(ip_addr)


def main():
    old_ip = get_last_ip()
    res = requests.get("http://ifconfig.me")
    if res.status_code == requests.status_codes.codes["ok"]:
        current_ip = res.text
        if current_ip != old_ip or True:
            logging.info(f"public ip changed from {old_ip} to {current_ip}")
            send_mail(current_ip)
            save_current_ip(current_ip)
        else:
            logging.info("ip address did not change since last time")


if __name__ == "__main__":
    main()
