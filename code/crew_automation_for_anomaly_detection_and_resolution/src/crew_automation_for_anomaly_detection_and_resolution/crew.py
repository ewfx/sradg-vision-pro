from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CSVSearchTool

@CrewBase
class CrewAutomationForAnomalyDetectionAndResolutionCrew():
    """CrewAutomationForAnomalyDetectionAndResolution crew"""

    @agent
    def data_ingestion_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['data_ingestion_specialist'],
            tools=[],
        )

    @agent
    def anomaly_detection_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['anomaly_detection_analyst'],
            tools=[],
        )

    @agent
    def classification_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['classification_expert'],
            tools=[],
        )

    @agent
    def feedback_loop_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['feedback_loop_coordinator'],
            tools=[],
        )

    @agent
    def break_resolution_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['break_resolution_analyst'],
            tools=[],
        )

    @agent
    def operator_automation_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config['operator_automation_coordinator'],
            tools=[],
        )


    @task
    def data_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['data_collection_task'],
            tools=[CSVSearchTool()],
        )

    @task
    def anomaly_detection_task(self) -> Task:
        return Task(
            config=self.tasks_config['anomaly_detection_task'],
            tools=[CSVSearchTool()],
        )

    @task
    def classification_task(self) -> Task:
        return Task(
            config=self.tasks_config['classification_task'],
            tools=[],
        )

    @task
    def feedback_capture_task(self) -> Task:
        return Task(
            config=self.tasks_config['feedback_capture_task'],
            tools=[],
        )

    @task
    def break_resolution_task(self) -> Task:
        return Task(
            config=self.tasks_config['break_resolution_task'],
            tools=[],
        )

    @task
    def workflow_automation_task(self) -> Task:
        return Task(
            config=self.tasks_config['workflow_automation_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the CrewAutomationForAnomalyDetectionAndResolution crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
