import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):

    logging.info('Function triggered to process a message: ', event.get_json())
    #Starter code is wrong
    #logging.info('  EnqueuedTimeUtc =', event.event_time)
    #logging.info('  SequenceNumber =', event.s)
    #logging.info('  Offset =', event.offset)

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })


    logging.info('Python EventGrid trigger processed an event: %s', result)



