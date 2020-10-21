# weasy-function
HTML-to-PDF API powered by Weasyprint and Azure Functions

Host your own HTML-To-PDF API.

##Requirements
- Azure subscription
- VS Code
- Azure Function Tools
- Azure Function extension for VS Code
- ...?

##Setup
- Clone this repo
- Open in VS Code
- In the Azure Function Sidebar, click "Deploy"

Probably you'll want to choose "Function" as way of authentication. In that case you need an app key (available in Azure Portal) to make requests.
Beware that in case of public clients (like clients running in a browser), you might have different needs.

##Usage
Send a POST request to /api/HtmlToPdf?code=[your App key for that function] with body:
```
{
   html: "<!doctype html><html>...</html>"
}
```
