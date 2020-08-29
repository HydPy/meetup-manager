from abc import ABC


class BaseIntegrationClient(ABC):
    """
    Interface for Integration clients.
    This abstract class should be subclassed to create integration specific
    clients. The clients can choose to use an existing platform sdk / implement
    rest integration using `requests`.

    `create_event`
        Method used to create an event.

    `update_event`
        Method used to update an event (comment/post update).

    `notify_attendees`
        Method used to share an update
        with attendees(email notification/messaging).
    """

    api_endpoint = "https://api.example.com"
    content_type = "application/json"
    client = None

    class Meta:
        abstract = True

    def create_event(self, *args, **kwargs):
        raise NotImplementedError("Must be implemented in a subclass.")

    def update_event(self, *args, **kwargs):
        raise NotImplementedError("Must be implemented in a subclass.")

    def notify_attendees(self, *args, **kwargs):
        raise NotImplementedError("Must be implemented in a subclass.")

    def notify_speaker(self, *args, **kwargs):
        raise NotImplementedError("Must be implemented in a subclass.")
