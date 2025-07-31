# OWASP Agentic AI - Threats and Mitigations
## Version 1.0 - February 2025

### Table of Content
- Introduction
- AI Agents
- Agentic AI Reference Architecture
- Agentic AI Threat Model
- Agentic Threats Taxonomy Navigator
- Mitigation Strategies
- Example Threat Models
- Acknowledgements
- OWASP Top 10 for LLM Project Sponsors
- Project Supporters

---

## Introduction

Agentic AI represents an advancement in autonomous systems, increasingly enabled by large language models (LLMs) and generative AI. While agentic AI predates modern LLMs, their integration with generative AI has significantly expanded their scale, capabilities, and associated risks. This document is the first in a series of guides from the OWASP Agentic Security Initiative (ASI) to provide a threat-model-based reference of emerging agentic threats and discuss mitigations.

The document:
• Defines the scope and audience
• Provides a definition of agentic terms, capabilities, and architecture
• Discusses threat modelling approaches and provides a reference threat model discussing new agentic threats and mitigations
• Illustrates the threats in different settings with threat models for four example scenarios
• Documents threats with a structured and detailed Agentic Threat Taxonomy
• Details mitigations and playbooks

### Scope and Audience

Our work focuses on agents based on large language models (LLMs), as these general-purpose models revolutionize agentic capabilities and, unlike previous agentic generations, bring more capabilities and widespread use.

We aim to provide an easy-to-follow, practical, and actionable reference to threats and mitigations of Agentic AI applications. We introduce some basic concepts and use a reference architecture of agentic AI, acting as the canvas for threat models, to explain and contextualize agentic threats. However, providing a detailed definition and architecture of agentic AI is beyond the scope of our work.

Our work focuses on Agentic AI threats and relies on existing guidelines and standards, such as the OWASP Top 10 for LLM Applications and Generative AI, OWASP AI Exchange, OWASP Top 10, and the OWASP Top 10 for APIs to address related aspects inherent in building AI applications. When relevant, we highlight Agentic AI's impact on existing threats and risks.

The intended audience of this document are builders and defenders of agentic applications, including developers, architects, platform and QA engineers, and security professionals. This is our first report, and we plan to provide additional role-based guides as follow-ups to this document for technical and decision-making audiences.


