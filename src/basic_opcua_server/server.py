import asyncio
import logging
from asyncua import Server

# Enable basic logging to see server status and connection attempts
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')


async def main():
    # 1. Initialize the Server
    server = Server()
    await server.init()

    # Set the endpoint URL where clients will connect
    # 0.0.0.0 is the default interface, but it can be changed to 127.0.0.1 to restrict access to the local machine.
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_server_name("Basic OPC UA Server")

    # 2. Setup a custom namespace
    # Namespaces prevent collisions between node IDs from different systems
    uri = "http://your_domain.com/opcua"
    idx = await server.register_namespace(uri)

    # 3. Populate the Address Space
    # Create a parent object to organize our variables
    my_device = await server.nodes.objects.add_object(idx, "Device_1")

    # Add the variables (Boolean and Floating Point)
    # The data type is automatically inferred from the initial value (False -> Boolean, 0.0 -> Float/Double)
    bool_var = await my_device.add_variable(idx, "Status_Active", False)
    float_var = await my_device.add_variable(idx, "Process_Value", 0.0)

    # 4. Make variables writable
    # By default, variables are read-only. This allows clients to change the values.
    await bool_var.set_writable()
    await float_var.set_writable()

    _logger.info("Starting OPC UA Server at %s", server.endpoint.geturl())
    _logger.info("Namespace ID: %s", idx)

    # 5. Start the server and keep it running
    # The 'async with' context manager automatically handles starting and stopping the server
    async with server:
        while True:
            # The server runs in the background; this loop keeps the main script alive
            await asyncio.sleep(1)


if __name__ == "__main__":
    # Gracefully handle manual interruptions (like Ctrl+C)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer successfully shut down.")