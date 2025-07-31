#!/usr/bin/env python3
import re
import os

def translate_content():
    """
    Traduce el contenido del PDF al español chileno formal
    manteniendo términos técnicos en inglés
    """
    
    # Leer el contenido original
    with open('/home/ubuntu/owasp-agentic-ai-spanish/contenido_completo_original.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Diccionario de traducciones específicas
    translations = {
        # Títulos principales
        "Agentic AI - Threats and Mitigations": "IA Agéntica - Amenazas y Mitigaciones",
        "OWASP Top 10 for LLM Apps & Gen AI": "OWASP Top 10 para Aplicaciones LLM e IA Generativa",
        "Agentic Security Initiative": "Iniciativa de Seguridad Agéntica",
        "Table of Content": "Tabla de Contenidos",
        "Introduction": "Introducción",
        "AI Agents": "Agentes de IA",
        "Agentic AI Reference Architecture": "Arquitectura de Referencia de IA Agéntica",
        "Agentic AI Threat Model": "Modelo de Amenazas de IA Agéntica",
        "Agentic Threats Taxonomy Navigator": "Navegador de Taxonomía de Amenazas Agénticas",
        "Mitigation Strategies": "Estrategias de Mitigación",
        "Example Threat Models": "Modelos de Amenazas de Ejemplo",
        "Acknowledgements": "Reconocimientos",
        "OWASP Top 10 for LLM Project Sponsors": "Patrocinadores del Proyecto OWASP Top 10 para LLM",
        "Project Supporters": "Colaboradores del Proyecto",
        
        # Términos generales
        "License and Usage": "Licencia y Uso",
        "You are free to:": "Usted es libre de:",
        "Share": "Compartir",
        "copy and redistribute the material in any medium or format": "copiar y redistribuir el material en cualquier medio o formato",
        "Adapt": "Adaptar",
        "remix, transform, and build upon the material for any purpose, even commercially": "remezclar, transformar y construir sobre el material para cualquier propósito, incluso comercialmente",
        "Under the following terms:": "Bajo los siguientes términos:",
        "Attribution": "Atribución",
        "You must give appropriate credit": "Debe dar el crédito apropiado",
        "provide a link to the license": "proporcionar un enlace a la licencia",
        "and indicate if changes were made": "e indicar si se realizaron cambios",
        "You may do so in any reasonable manner": "Puede hacerlo de cualquier manera razonable",
        "but not in any way that suggests the licensor endorses you or your use": "pero no de manera que sugiera que el licenciante lo respalda a usted o su uso",
        "Attribution Guidelines": "Directrices de Atribución",
        "must include the project name as well as the name of the asset Referenced": "debe incluir el nombre del proyecto así como el nombre del activo referenciado",
        "ShareAlike": "CompartirIgual",
        "If you remix, transform, or build upon the material": "Si remezcla, transforma o construye sobre el material",
        "you must distribute your contributions under the same license as the original": "debe distribuir sus contribuciones bajo la misma licencia que el original",
        "Link to full license text": "Enlace al texto completo de la licencia",
        
        # Contenido específico
        "Scope and Audience": "Alcance y Audiencia",
        "Core Capabilities": "Capacidades Principales",
        "Agents and LLM Applications": "Agentes y Aplicaciones LLM",
        "Planning & Reasoning": "Planificación y Razonamiento",
        "Memory / Statefulness": "Memoria / Estado",
        "Action and Tool Use": "Acción y Uso de Herramientas",
        "Reflection": "Reflexión",
        "Self-Critic": "Autocrítica",
        "Chain of Thought": "Cadena de Pensamiento",
        "Subgoal Decomposition": "Descomposición de Subobjetivos",
        "Short-term memory": "Memoria a corto plazo",
        "Long-term memory": "Memoria a largo plazo",
        "Single Agent": "Agente Único",
        "Multi-agent system": "Sistema Multi-agente",
        "autonomy": "autonomía",
        
        # Frases comunes
        "The information provided in this document does not, and is not intended to, constitute legal advice": "La información proporcionada en este documento no constituye, ni pretende constituir, asesoramiento legal",
        "All information is for general informational purposes only": "Toda la información es solo para propósitos informativos generales",
        "This document contains links to other third-party websites": "Este documento contiene enlaces a otros sitios web de terceros",
        "Such links are only for convenience": "Tales enlaces son solo por conveniencia",
        "and OWASP does not recommend or endorse the contents of the third-party sites": "y OWASP no recomienda ni respalda el contenido de los sitios de terceros",
        
        # Términos técnicos que se mantienen en inglés pero se explican
        "large language models": "large language models",
        "LLMs": "LLMs",
        "generative AI": "generative AI",
        "Machine Learning": "Machine Learning",
        "ML": "ML",
        "Reinforcement Learning": "Reinforcement Learning",
        "function calling": "function calling",
        "APIs": "APIs",
        "ReAct pattern": "patrón ReAct",
        "LangChain": "LangChain",
        "LangFlow": "LangFlow",
        "AutoGen": "AutoGen",
        "CrewAI": "CrewAI",
    }
    
    # Aplicar traducciones
    translated_content = content
    for english, spanish in translations.items():
        translated_content = translated_content.replace(english, spanish)
    
    # Traducciones más complejas con regex
    # Traducir frases completas manteniendo estructura
    complex_translations = [
        (r"An agent is an intelligent software system designed to perceive its environment, reason about it, make decisions, and take actions to achieve specific objectives autonomously",
         "Un agente es un sistema de software inteligente diseñado para percibir su entorno, razonar sobre él, tomar decisiones y realizar acciones para lograr objetivos específicos de manera autónoma"),
        
        (r"Russell and Norvig define agents in their classic \"Artificial Intelligence: A Modern Approach\" as follows:",
         "Russell y Norvig definen los agentes en su clásico \"Artificial Intelligence: A Modern Approach\" de la siguiente manera:"),
        
        (r"An intelligent agent is \"an agent that acts appropriately for its circumstances and its goals, is flexible to changing environments and goals, learns from experience, and makes appropriate choices given its perceptual and computational limitations.\"",
         "Un agente inteligente es \"un agente que actúa apropiadamente para sus circunstancias y objetivos, es flexible ante entornos y objetivos cambiantes, aprende de la experiencia y toma decisiones apropiadas dadas sus limitaciones perceptuales y computacionales.\""),
        
        (r"AI Agents use Machine Learning \(ML\) for reasoning",
         "Los Agentes de IA utilizan Machine Learning (ML) para el razonamiento"),
        
        (r"traditional ML approaches \(such as Reinforcement Learning\) playing a key role in each development",
         "los enfoques tradicionales de ML (como Reinforcement Learning) juegan un papel clave en cada desarrollo"),
        
        (r"The Open AI Gym \(now Farama Foundation's Gymnasium\), helped drive the first wave of Agentic AI",
         "El Open AI Gym (ahora Gymnasium de Farama Foundation), ayudó a impulsar la primera ola de IA Agéntica"),
        
        (r"However, the advanced capabilities, NLP interface, and scale of LLMs have revolutionized agentic AI and accelerated adoption",
         "Sin embargo, las capacidades avanzadas, la interfaz de NLP y la escala de los LLMs han revolucionado la IA agéntica y acelerado su adopción"),
        
        (r"Well-known vendors and enterprises are embracing LLM agents",
         "Proveedores y empresas reconocidas están adoptando agentes LLM"),
        
        (r"and Gartner forecasts that by 2028 33% of enterprise software applications will utilize agentic AI",
         "y Gartner pronostica que para 2028 el 33% de las aplicaciones de software empresarial utilizarán IA agéntica"),
        
        (r"enabling 15% of day-to-day work decisions to be made autonomously",
         "permitiendo que el 15% de las decisiones laborales del día a día se tomen de manera autónoma"),
    ]
    
    for pattern, replacement in complex_translations:
        translated_content = re.sub(pattern, replacement, translated_content, flags=re.IGNORECASE)
    
    return translated_content

if __name__ == "__main__":
    print("Iniciando traducción del contenido...")
    translated = translate_content()
    
    # Guardar contenido traducido
    output_path = '/home/ubuntu/owasp-agentic-ai-spanish/contenido_traducido.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f"Traducción completada y guardada en: {output_path}")

