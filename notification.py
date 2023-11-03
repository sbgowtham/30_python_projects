from plyer import notification

title = "Notification Title"
message = "This is a sample notification."

notification.notify(
    title=title,
    message=message,
    app_name="Python Notification App",
    timeout=10  # Notification will disappear after 10 seconds
)
