from app import app, service
app.debug = True
service.emailService()
app.run()