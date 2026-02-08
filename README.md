# Summary
This framework orchestrates a 3-agent AutoGen pipeline via MCP to automate the user lifecycle, from SQL data extraction to RESTful registration and login authentication. By eliminating manual data entry through autonomous hand-offs between specialized agents.

## Core Workflow
- **DatabaseAgent:** Extracts raw user "seed" data from MySQL.

- **APIAgent:** Transforms data (unique timestamps) and executes RESTful Registration/Login flows.

- **ExcelAgent:** Closes the loop by generating an automated Audit Report of the test results.

## Technical Stack
- **Framework:** AutoGen (Multi-Agent Orchestration)

- **Protocol:** MCP (Model Context Protocol) for Database & Filesystem access

- **Language:** Python (Asyncio)

- **Integrations:** MySQL, REST APIs, Microsoft Excel
