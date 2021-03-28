import logging
import datetime
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    if req.method == "GET":
        d = datetime.datetime.today().strftime('%Y-%m-%d')
        return func.HttpResponse(f"Todays date is {d}")
    else:
        return func.HttpResponse(
            "Bad request. Only GET allowed.",
            status_code=400
        )
        
