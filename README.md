# Basic OPC-UA Server

A pure Python OPC-UA server library implementation using the `asyncua` framework.

## Overview

This project provides a lightweight, fully functional OPC-UA server built with modern Python asynchronous patterns. It initializes a custom address space with a simulated device and writable variables, making it an ideal starting point for building out industrial communication interfaces, testing clients, or simulating machine data.

## Server Details

The script automatically provisions the following OPC-UA structure upon startup:

* **Endpoint:** `opc.tcp://0.0.0.0:4840/freeopcua/server/` (Listens on all network interfaces)
* **Server Name:** Basic OPC UA Server
* **Custom Namespace:** `http://your_domain.com/opcua`
* **Objects & Nodes:**
  * `Device_1` (Parent Object)
    * `Status_Active` (Boolean, Writable, Initial Value: False)
    * `Process_Value` (Float, Writable, Initial Value: 0.0)

## Prerequisites and Versioning# Basic OPC-UA Server

**Author:** Peter Kern, TH Köln

A pure Python OPC-UA server library implementation using the `asyncua` framework.

## Overview

This project provides a lightweight, fully functional OPC-UA server built with modern Python asynchronous patterns. It initializes a custom address space with a simulated device and writable variables, making it an ideal starting point for building out industrial communication interfaces, testing clients, or simulating machine data.

## Server Details

The script automatically provisions the following OPC-UA structure upon startup:

* **Endpoint:** `opc.tcp://0.0.0.0:4840/freeopcua/server/` (Listens on all network interfaces)
* **Server Name:** Basic OPC UA Server
* **Custom Namespace:** `http://your_domain.com/opcua`
* **Objects & Nodes:**
  * `Device_1` (Parent Object)
    * `Status_Active` (Boolean, Writable, Initial Value: False)
    * `Process_Value` (Float, Writable, Initial Value: 0.0)

## Prerequisites and Versioning

**Important:** Modern asynchronous operations require specific environment configurations. As defined in the `pyproject.toml`, you must ensure the following requirements are met:

* **Python >= 3.13:** The `asyncio` module is part of the Python standard library. A Python version of 3.13 or higher is strictly required to ensure compatibility with the underlying asynchronous event loops used by this server.
* **asyncua >= 1.2b2:** The core OPC-UA dependency.

## Installation

It is recommended to install this project in editable mode. This allows you to modify the source code while testing and automatically installs the dependencies listed in the `pyproject.toml`.

Navigate to the root directory of the project (where `pyproject.toml` is located) and run:

```bash
pip install -e .

**Important:** Modern asynchronous operations require specific environment configurations. As defined in the `pyproject.toml`, you must ensure the following requirements are met:

* **Python >= 3.13:** The `asyncio` module is part of the Python standard library. A Python version of 3.13 or higher is strictly required to ensure compatibility with the underlying asynchronous event loops used by this server.
* **asyncua >= 1.2b2:** The core OPC-UA dependency.

## Installation

It is recommended to install this project in editable mode. This allows you to modify the source code while testing and automatically installs the dependencies listed in the `pyproject.toml`.

Navigate to the root directory of the project (where `pyproject.toml` is located) and run:

```bash
pip install -e .