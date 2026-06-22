import asyncio
import json
import logging
import sys
from pathlib import Path
from asyncua import Server

# ==========================================
# SWITCH: Set to False to deactivate log output
# ==========================================
ENABLE_LOGGING = True

# Configure logging based on the switch
if ENABLE_LOGGING:
    logging.basicConfig(level=logging.ERROR)
else:
    # Disable all logging below CRITICAL level
    logging.disable(logging.CRITICAL)

_logger = logging.getLogger('asyncua')


async def main():
    # 1. Load Configuration
    try:
        # Safely resolve the path whether running as script or frozen executable
        if getattr(sys, 'frozen', False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).resolve().parent

        config_path = base_dir / "config.json"

        with open(config_path, "r") as f:
            config = json.load(f)

        _logger.info("Successfully loaded config.json")
    except Exception as e:
        _logger.error("Configuration Error: %s", e)
        return

    # 2. Initialize the Server
    server = Server()
    await server.init()

    # Apply the URL from the JSON config, fallback to default if missing
    url = config.get("server_url", "opc.tcp://0.0.0.0:4840/th-koeln/opcua/")
    server.set_endpoint(url)
    server.set_server_name("SimpleOPCUAServer")

    # 3. Setup Namespaces
    uri = "http://th-koeln.de/ait/opcua/simple_server/"
    idx = await server.register_namespace(uri)


    # 4. Populate the Address Space
    device_name = config.get("device_name", "Some_Device")
    my_device = await server.nodes.objects.add_object(idx, device_name)

    node_config = config.get("nodes", {})
    data_types = config.get("data_types", {})



    # Dynamically create nodes from the dictionary
    for node_name, node_id_str in node_config.items():
        # Read intended type from config, default to boolean if missing
        intended_type = data_types.get(node_name, "boolean")

        # Infer data type based on the config file
        if intended_type == "float":
            initial_value = 0.0
        else:
            initial_value = False

        try:
            # Create variable using the explicit string ID from the JSON
            var = await my_device.add_variable(node_id_str, node_name, initial_value)
            await var.set_writable()
            _logger.info("Created node: %s -> %s (Type: %s)", node_name, node_id_str, intended_type)
        except Exception as e:
            _logger.error("Failed to create node %s: %s", node_name, e)

    _logger.info("Starting OPC UA Server at %s", server.endpoint.geturl())

    # 5. Start the server and keep it running
    async with server:
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    # Gracefully handle manual interruptions (like Ctrl+C)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer successfully shut down.")