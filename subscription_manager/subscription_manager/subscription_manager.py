from rxconfig import config
import reflex as rx
import pandas as pd

filename = f"{config.app_name}/{config.app_name}.py"


class SubscriptionFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def index() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.heading("Add New Subscription", size="md"),
                
                rx.text("Start Date:"),
                rx.input(type_="date", id="start_date"),
                
                rx.text("End Date:"),
                rx.input(type_="date", id="end_date"),
                
                rx.text("Subscription Name:"),
                rx.input(type="text", placeholder="Enter the name of the subscription.", id="subscription_name"),
                
                rx.text("Category:"),
                rx.input(type="text", placeholder="Enter a category for this subscription.", id="subscription_category"),
                
                rx.button("Submit", type_="submit"),
            ),
            on_submit=SubscriptionFormState.handle_submit,
        ),
        rx.divider(),
        rx.heading("Current Subscriptions", size="md"),
        rx.text(SubscriptionFormState.form_data.to_string()),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
