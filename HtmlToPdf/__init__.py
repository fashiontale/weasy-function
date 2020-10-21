import logging

import azure.functions as func
import weasyprint


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        html = req_body.get('html')
        doc = weasyprint.HTML(string = html)
        pdfBytes = doc.write_pdf()

        return func.HttpResponse(pdfBytes, mimetype = "application/pdf")

