# agentFactory.py
from autogen_agentchat.agents import AssistantAgent
from framework.mcp_config import McpConfig

# This module defines the AgentFactory class, which is responsible for creating different types of agents (DatabaseAgent, APIAgent, ExcelAgent) with their respective configurations and workbenches. 
# The factory uses the MCP configuration to set up the necessary workbenches for each agent, allowing them to perform their specific tasks in the user registration process. 
# Each agent is initialized with a system message that outlines its responsibilities and instructions for interacting with other agents in the workflow.
class AgentFactory:
    
    # The constructor initializes the AgentFactory with a model client and sets up the MCP configuration.
    def __init__(self, model_client):
        self.model_client = model_client
        self.mcp_config = McpConfig()
    
    # This method creates and returns an instance of the DatabaseAgent, which is responsible for retrieving user registration data from a MySQL database. The agent is configured with a system message that outlines its tasks and instructions.
    def create_database_agent(self, system_message):
        database_agent = AssistantAgent( name="DatabaseAgent", model_client=self.model_client,
                                         workbench=self.mcp_config.get_mysql_workbench(),
                                         system_message=system_message )
        return database_agent
    
    # This method creates and returns an instance of the APIAgent, which is responsible for testing API endpoints related to user registration and login. The agent is configured with both REST API and filesystem workbenches, allowing it to interact with APIs and read necessary files. 
    # The system message provides detailed instructions for the agent's tasks.
    def create_api_agent(self,system_message):
        rest_api_workbench = self.mcp_config.get_rest_api_workbench()
        file_system_workbench = self.mcp_config.get_filesystem_workbench()

        api_agent = AssistantAgent(name="APIAgent",model_client=self.model_client,
                                   workbench=[rest_api_workbench, file_system_workbench],

                                   system_message=system_message)
        return api_agent
    
    # This method creates and returns an instance of the ExcelAgent, which is responsible for saving successful registration details to an Excel file. 
    # The agent is configured with an Excel workbench, allowing it to interact with Excel files.
    def create_excel_agent(self, system_message=None):
        excel_workbench = self.mcp_config.get_excel_workbench()

        return AssistantAgent(
            name="ExcelAgent",
            model_client=self.model_client,
            workbench=excel_workbench,
            system_message=system_message
        )


