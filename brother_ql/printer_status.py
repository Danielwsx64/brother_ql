import logging, time
from brother_ql.backends import backend_factory
from brother_ql.reader import interpret_response
from brother_ql.raster import BrotherQLRaster

logger = logging.getLogger(__name__)

backend = 'linux_kernel'
model = 'QL-810W'
printer_name = 'file:///dev/usb/lp0'

be = backend_factory(backend)
BrotherQLBackend = be['backend_class']

printer = BrotherQLBackend(printer_name)

qlr = BrotherQLRaster(model)
qlr.exception_on_warning = True
# qlr.add_invalidate()
qlr.add_switch_mode()
qlr.add_initialize()
# qlr.add_status_information()

instructions = qlr.data

printer.write(instructions)

start = time.time()

while time.time() - start < 10:
    data = printer.read()
    if not data:
        time.sleep(0.005)
        continue
    try:
        result = interpret_response(data)
    except ValueError:
        logger.error("TIME %.3f - Couln't understand response: %s", time.time()-start, data)
        continue

    print(result)
    break
