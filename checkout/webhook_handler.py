from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handles Stripe webhooks
    From Boutique Ado project
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles a generic/unknown/unexpected webhook event
        From Boutique Ado project
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)