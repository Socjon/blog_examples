
import dash
import dash_html_components as html

app = dash.Dash()

html_content_of_app = html.H1("Hello World")

app.layout = html_content_of_app

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)

