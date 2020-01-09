import json, logging, time, sys
from brother_ql.backends import backend_factory
from brother_ql.reader import interpret_response
from brother_ql.raster import BrotherQLRaster

logger = logging.getLogger(__name__)

def get_status(backend, model, printer_name):
    be = backend_factory(backend)
    BrotherQLBackend = be['backend_class']
    printer = False

    try:
        printer = BrotherQLBackend(printer_name)
    except:
        print('Error: could not connect to printer ' + printer_name)
        sys.exit(2)

    qlr = BrotherQLRaster(model)
    qlr.exception_on_warning = True
    qlr.add_switch_mode()
    qlr.add_initialize()
    qlr.add_status_information()

    instructions = qlr.data
    printer.write(instructions)

    start = time.time()

    output = False

    while time.time() - start < 3:
        data = printer.read()
        if not data:
            time.sleep(0.005)
            continue
        try:
            result = interpret_response(data)
            output = result
            break

        except ValueError:
            logger.error("TIME %.3f - Couln't understand response: %s", time.time()-start, data)
            continue

    if output:
        print(json.dumps(output, indent=2, sort_keys=True))
    else:
        print('Error: could not fetch printer status')
        sys.exit(2)


# status('linux_kernel', 'QL-810W', 'file:///dev/usb/lp0')
