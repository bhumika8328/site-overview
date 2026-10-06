# =====================================================================
# SitePulse Backend Server (Python 3.14 Compatible)
# Serves frontend static files and provides live POST /api/send-email
# endpoint to send real emails to recipient inboxes via SMTP.
# =====================================================================
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PORT = 8080

class SitePulseHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/send-email':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
                manager_name = data.get('managerName', 'Project Manager')
                manager_email = data.get('managerEmail', '').strip()
                priority = data.get('priority', 'Normal')
                remarks = data.get('remarks', '')
                rec_title = data.get('recTitle', 'Project Recommendation Action Plan')
                
                smtp_server = data.get('smtpServer') or os.environ.get('SMTP_SERVER', '')
                smtp_port = int(data.get('smtpPort') or os.environ.get('SMTP_PORT', 587))
                smtp_user = data.get('smtpUser') or os.environ.get('SMTP_USER', '')
                smtp_pass = data.get('smtpPass') or os.environ.get('SMTP_PASS', '')

                email_sent = False
                message_status = ""

                html_body = f"""
                <!DOCTYPE html>
                <html>
                <body style="font-family: Arial, sans-serif; color: #1e293b; background-color: #f8fafc; padding: 20px; margin: 0;">
                  <div style="max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; border-bottom: 2px solid #3b82f6; padding-bottom: 12px;">
                      <h2 style="color: #1e293b; margin: 0; font-size: 20px;">SitePulse — Project Directive Notification</h2>
                    </div>
                    <p style="font-size: 15px; line-height: 1.5;">Hello <b>{manager_name}</b>,</p>
                    <p style="font-size: 14px; line-height: 1.5; color: #475569;">The following schedule recovery action plan has been assigned and dispatched to you from the SitePulse Infrastructure Intelligence Layer:</p>
                    
                    <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 18px; margin: 20px 0; border-radius: 6px;">
                      <div style="font-size: 11px; text-transform: uppercase; color: #2563eb; font-weight: bold; letter-spacing: 0.08em; margin-bottom: 6px;">PRIORITY: {priority}</div>
                      <h3 style="margin: 0 0 10px 0; color: #0f172a; font-size: 17px;">{rec_title}</h3>
                      {f'<div style="font-size: 13.5px; color: #334155; background: #ffffff; padding: 10px 12px; border-radius: 4px; border: 1px solid #dbeafe; margin-top: 10px;"><b>Directive Remarks:</b> {remarks}</div>' if remarks else ''}
                    </div>

                    <p style="font-size: 13px; color: #64748b; line-height: 1.5;">This notification is linked to active project assessment records and verified against baseline schedule activities in the digital twin layer.</p>
                    <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;" />
                    <p style="font-size: 11px; color: #94a3b8; text-align: center; margin: 0;">SIH26122 · SitePulse Infrastructure Intelligence Platform</p>
                  </div>
                </body>
                </html>
                """

                if smtp_server and smtp_user and smtp_pass:
                    msg = MIMEMultipart("alternative")
                    msg["Subject"] = f"[{priority}] SitePulse Action Plan: {rec_title}"
                    msg["From"] = f"SitePulse <{smtp_user}>"
                    msg["To"] = manager_email
                    msg.attach(MIMEText(html_body, "html"))

                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(smtp_user, smtp_pass)
                        server.sendmail(smtp_user, manager_email, msg.as_string())
                    email_sent = True
                    message_status = f"Real email sent via SMTP server ({smtp_server}) to {manager_email}!"
                else:
                    log_entry = f"\n=== EMAIL DISPATCH LOG ===\nTo: {manager_name} <{manager_email}>\nPriority: {priority}\nTitle: {rec_title}\nRemarks: {remarks}\n===========================\n"
                    with open("sent_emails_log.txt", "a", encoding="utf-8") as f:
                        f.write(log_entry)
                    message_status = f"Action plan prepared for {manager_email}. Enter your SMTP password in the modal to deliver directly to your inbox."

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = {
                    "success": True,
                    "emailSent": email_sent,
                    "recipient": manager_email,
                    "message": message_status
                }
                self.wfile.write(json.dumps(response).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        elif self.path == '/api/assessments':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"reportId": "REP-2026-0812", "eventId": "EVT-9042", "status": "saved"}).encode('utf-8'))
        else:
            super().do_POST()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', PORT), SitePulseHandler)
    print(f"SitePulse server running at http://localhost:{PORT}")
    server.serve_forever()
