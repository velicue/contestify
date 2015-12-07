from app import app, service
service.emailService()
app.debug = True
app.run()
