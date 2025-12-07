# AI-Powered Agentic Workflow for Project Management

In this repo, you will find all the files about a developed AI-Powered Agentic Workflow for Project Management

The developed system showcases a mature and technically robust approach to multi-agent orchestration, workflow automation, and LLM-driven project planning. At its core is a well-architected agentic_workflow.py module that coordinates agents, structures their interactions, and ensures seamless execution from initial planning to final evaluation.

The workflow demonstrates true end-to-end capability: it autonomously generates action plans, transforms them into structured user stories and feature sets, decomposes them into implementation tasks, and then evaluates the results with clear, auditable logic. The outputs follow strict formatting and structural standards, making them easy to review, trace, and integrate into downstream processes.

The codebase reflects strong engineering discipline, with clean modular boundaries, well-defined agent responsibilities, and thoughtful orchestration flows. It adheres to best practices in prompt engineering, API interaction, and data modeling, resulting in a system that is both reliable and extensible. Overall, the work represents a professional-grade implementation of an agentic workflow framework, balancing clarity, automation, and technical precision.

**What Has Been Built: A Reusable Agentic Toolkit**

A modular Python package (workflow_agents) has been developed, featuring seven specialized AI agent classes that form the foundation of more advanced workflows:

- DirectPromptAgent
- AugmentedPromptAgent
- KnowledgeAugmentedPromptAgent
- RAGKnowledgePromptAgent
- EvaluationAgent
- RoutingAgent
- ActionPlanningAgent

Each agent is individually tested, with dedicated test scripts and accompanying run outputs that validate functionality and reliability. Together, they constitute a robust toolkit for constructing flexible, intelligent multi-agent systems.

**2. A General-Purpose Agentic Project Management Workflow**

A central orchestration script, agentic_workflow.py, implements the end-to-end workflow for technical project management. Using a combination of planning, routing, knowledge-augmented generation, and evaluation, the system transforms a high-level product concept and an associated product specification into:

- Structured user stories
- Detailed product features
- Fully defined engineering tasks

**The workflow executes as follows:**

- Accepts a TPM-style prompt and the Email Router product specification
- Uses an Action Planning Agent to break down the objective into logical sub-tasks
- Applies a Routing Agent to assign each sub-task to the most suitable agent group
- Simulates a Product Manager team that generates and validates user stories
- Simulates a Program Manager team that defines and evaluates product features
- Simulates a Development Engineer team that produces evaluated engineering tasks
- Outputs a complete, well-structured project plan for the Email Router, demonstrating the workflow’s reliability, scalability, and clarity.

**Deliverables Produced**

Phase 1

- Fully implemented reusable agent library (workflow_agents/base_agents.py)
- Seven test scripts validating each agent
- Executed test outputs (screenshots or text logs)

**Phase 2**

- Completed agentic_workflow.py script implementing the full project management workflow for the Email Router pilot


