import boto3
import json
from .teams import TeamManager

print('Loading function')

s3 = boto3.client('s3')


def handler(event, context):
    """
    Handle the API Gateway request.

    :return:
    print("Received event: " + json.dumps(event, indent=2))
    Display the input for debugging.. but not normally
    If no queryParams are passed, then the structure won't exist.

    event data reference: https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html#eventsources-api-gateway-request

    :param event:
    :param context:
    :return:
    """
    print("Entered handler")
    queryParams = event.get('queryStringparameters', {})
    showEvent = queryParams.get('show_input', False)

    eventString = json.dumps(event, indent=2, sort_keys=True)

    print(f'Full event:{eventString}')

    body = event.get('body', '{men:[],women:[]}')
    body = json.loads(body)

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": 'application/json',
        },
        "isBase64Encoded": False,
        "body": body
    }
    # if (event.body == null || event.body == undefined) {
    #
    #     const response = {
    #         statusCode: 402,
    #         body: JSON.stringify({
    #             message: 'POST Must include a valid body',
    #             input: showEvent ? event : ''
    #         })
    #     }
    #     callback(null, response)
    #     return
    # }

    # try {
    #     console.log(`Decoding and parsing the json: ${event.body}`)
    #     const eventBody = convertStrToObj(event.body)
    #     const output = generatePDF(eventBody)
    #
    #     console.log(`Generate completed with output in ${output.filename}`)
    #
    #     const response = {
    #         statusCode: 200,
    #         headers: {
    #             'Content-Type': 'application/pdf',
    #             'Content-Disposition': `attachment; filename="${eventBody.projectname}.pdf"`
    #         },
    #         isBase64Encoded: true,
    #         body: post_process_resource(output.fil.name,
    #             (file) => new Buffer(fs.readFileSync(file)).toString('base64'))
    #     }
    #
    #     console.log('Output file converted to base64 encoded version')
    #     callback(null, response);
    # } catch (err) {
    #     console.log(`Caught an error: ${err}`)
    #     callback(new Error(`Exception while processing: ${err}`));
    # }

    try:
        return response
    except Exception as e:
        print(e)
        raise e
