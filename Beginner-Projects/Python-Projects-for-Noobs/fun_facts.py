# Import the necessary modules
import requests
from pywebio import start_server
from pywebio.output import put_html, put_text, put_buttons, clear
from pywebio.session import hold

def get_fun_fact():
    """Fetch and display a random fun fact."""
    # Clear the screen
    clear()

    # Display the header
    display_header()

    # URL to fetch the data from
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    try:
        # Use GET request to fetch data
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP errors

        # Parse JSON data
        data = response.json()

        # Extract the 'text' from the JSON data
        useless_fact = data.get('text', 'No fact available at the moment.')

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        useless_fact = f"An error occurred: {e}"

    # Display the fun fact
    put_text(useless_fact, style='color:blue; font-size: 30px')

    # Display the "Click me" button
    put_buttons(
        [{'label': 'Click me', 'value': 'get_fact', 'color': 'success'}],
        onclick=get_fun_fact
    )

def display_header():
    """Display the Fun Fact Generator header."""
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

def fun_fact_app():
    """Main app function for the Fun Fact Generator."""
    # Display the header
    display_header()

    # Display the "Click me" button initially
    put_buttons(
        [{'label': 'Click me', 'value': 'get_fact', 'color': 'success'}],
        onclick=get_fun_fact
    )

    hold()  # Hold the session open

# Driver Function
if __name__ == '__main__':
    # Run the app using pywebio's start_server function
    start_server(fun_fact_app, port=8080)  # Choose any available port, like 8080
