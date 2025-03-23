from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CSVSearchTool

@CrewBase
class AgentCreationForCrewAutomationCrew():
    """AgentCreationForCrewAutomation crew"""

    @agent
    def data_ingestor(self) -> Agent:
        return Agent(
            config=self.agents_config['data_ingestor'],
            tools=[CSVSearchTool()],
        )

    @agent
    def anomaly_detector(self) -> Agent:
        return Agent(
            config=self.agents_config['anomaly_detector'],
            tools=[],
        )

    @agent
    def reconciliation_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['reconciliation_expert'],
            tools=[CSVSearchTool()],
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            tools=[],
        )


    @task
    def preprocess_financial_data(self) -> Task:
        return Task(
            config=self.tasks_config['preprocess_financial_data'],
            tools=[CSVSearchTool()],
        )

    @task
    def organize_transactions_data(self) -> Task:
        return Task(
            config=self.tasks_config['organize_transactions_data'],
            tools=[],
        )

    @task
    def analyze_data_for_anomalies(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_data_for_anomalies'],
            tools=[],
        )

    @task
    def validate_anomalies_against_criteria(self) -> Task:
        return Task(
            config=self.tasks_config['validate_anomalies_against_criteria'],
            tools=[],
        )

    @task
    def cross_check_anomalies_with_records(self) -> Task:
        return Task(
            config=self.tasks_config['cross_check_anomalies_with_records'],
            tools=[CSVSearchTool()],
        )

    @task
    def generate_comprehensive_report(self) -> Task:
        return Task(
            config=self.tasks_config['generate_comprehensive_report'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AgentCreationForCrewAutomation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
