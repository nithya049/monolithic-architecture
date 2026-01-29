from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = lambda self:0

    @task
    def view_events(self):
        self.client.get("/events?user=locust_user")
