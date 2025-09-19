# CoverLetterWriter Crew

Welcome to the CoverLetterWriter Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities. The multi-agents coverletter writer crew uses your resume (in markdown format), list of projects or portfolio (i.e. github url) and the job posting url to write one page of custom coverletter for that specific position. 

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` and `SERPER_API_KEY` into the `.env` file**

- Modify `src/cover_letter_writer/config/agents.yaml` to define your agents
- Modify `src/cover_letter_writer/config/tasks.yaml` to define your tasks
- Modify `src/cover_letter_writer/crew.py` to add your own logic, tools and specific args
- Modify `src/cover_letter_writer/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the cover-letter-writer Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example will run the create a `tailored_cover_letter.md` file with the output that includes custom cover letter.

## Understanding Your Crew

The cover-letter-writer Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew. Before running the crew for your own usecase, you need to modify the `fake_resume.md` and include your own information. Also, you need to modify the crew input in `src/cover_letter_writer/main.py` and include your desired job posting url, your github url, and short description about yourserlf.

## Support

For support, questions, or feedback regarding the CoverLetterWriter Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
