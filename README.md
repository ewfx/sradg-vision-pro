# 🚀 Project Name

## 📌 Table of Contents
- [🚀 Project Name](#-project-name)
  - [📌 Table of Contents](#-table-of-contents)
  - [🎯 Introduction](#-introduction)
  - [🎥 Demo](#-demo)
  - [💡 Inspiration](#-inspiration)
  - [⚙️ What It Does](#️-what-it-does)
  - [🛠️ How We Built It](#️-how-we-built-it)
  - [🚧 Challenges We Faced](#-challenges-we-faced)
  - [🏃 How to Run](#-how-to-run)
  - [👥 Team](#-team)

---

## 🎯 Introduction
Existing reconciliation tools process huge number of transactions daily and monthly. Business users spend significant time manually identifying data anomalies post-reconciliation for the breaks and fixing them. Process is tedious and error prone.
Our tool:
 Automatically detect data anomalies by comparing real-time data against historical baselines.
 Provides insights into potential root cause of detected anomalies.
 Integrates with existing reconciliation tools to streamline the anomaly identification process.
 Reduce manual effort and minimizes human error in anomaly detection.


## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
This is the day-to-day job of any financial analysis team. Even if our tool reduces their time by 10%, it will be very helpful for the bank.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
We used CrewAI agentic AI framework to create a team of analysts. Each agent has its well-defined task and can communicate with each other to provide accurate reconcilation actions.

## 🚧 Challenges We Faced
Defining personas for AI agents
Ensuring the output of the agent is well-formatted
Implementing guardrails so the agents do not go off-track

## 🏃 How to Run
Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.
1. First, if you haven't already, install uv:
   ```bash
   pip install uv
   ```
2. Navigate to ./code/src/anomally_detection and run the following command to install crewai CLI
   ```sh
   uv tool install crewai
   ```
3. Create a .env file under ./code/src/anomally_detection. It should contain these variables:
   ```sh
   MODEL=gpt-4o-mini
   OPENAI_API_KEY=<your openAI API key>
   ```
4. From the same directory, run
   ```sh
   crewai install
   ```
   to automatically install all requirements

5. Navigate to ./code/src/anomally_detection/inputs
   Add 2 files here:
   historical_data.csv containing the historical data
   current_data.csv constaining the current data
   Please ensure the names of files are accurate

6. Add configuration.
   Navigate to ./code/src/anomally_detection/src/main.py
   Replace the variables in the inputs dict (line#21) to better represent your data

7. Once the installation process is over, (from the same directory) run
   ```sh
   crewai run
   ```
   to run the AI framework. Results will be saved in ./code/src/anomally_detection/outputs


## 👥 Team
- **Vision Pro** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)