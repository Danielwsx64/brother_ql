import logging, time, sys
from brother_ql.backends import backend_factory
from brother_ql.reader import interpret_response

logger = logging.getLogger(__name__)

def r_print(instructions, printer_identifier, backend_identifier):
    be = backend_factory(backend_identifier)
    BrotherQLBackend = be['backend_class']
    printer = None

    try:
        printer = BrotherQLBackend(printer_identifier)
    except:
        print('Error: could not connect to printer ' + printer_identifier)
        sys.exit(2)

    start = time.time()
    printer.write(instructions)

    while time.time() - start < 10:
        data = printer.read()
        if not data:
            time.sleep(0.005)
            continue
        try:
            result = interpret_response(data)

            if(result['status_type'] == 'Printing completed'):
                print('Job successfully printed')
                sys.exit(0)

            elif(result['status_type'] == 'Error occurred'):
                print('Error: an error occurred while printing')
                sys.exit(2)

            continue

        except ValueError:
            logger.error("TIME %.3f - Couln't understand response: %s", time.time()-start, data)
            continue

    print('Error: Couldt get success message from printer')
    sys.exit(2)
