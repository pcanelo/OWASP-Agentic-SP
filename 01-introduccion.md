# Introducción

La IA Agéntica representa un avance en los sistemas autónomos, cada vez más habilitados por large language models (LLMs) e IA generativa. Aunque la IA agéntica es anterior a los LLMs modernos, su integración con la IA generativa ha expandido significativamente su escala, capacidades y riesgos asociados. Este documento es el primero de una serie de guías de la Iniciativa de Seguridad Agéntica de OWASP (ASI) para proporcionar una referencia basada en modelos de amenazas de las amenazas agénticas emergentes y discutir mitigaciones.

El documento:
- Define el alcance y la audiencia
- Proporciona una definición de términos agénticos, capacidades y arquitectura
- Discute enfoques de modelado de amenazas y proporciona un modelo de amenazas de referencia que discute nuevas amenazas agénticas y mitigaciones
- Ilustra las amenazas en diferentes configuraciones con modelos de amenazas para cuatro escenarios de ejemplo
- Documenta amenazas con una Taxonomía de Amenazas Agénticas estructurada y detallada
- Detalla mitigaciones y playbooks

## Alcance y Audiencia

Nuestro trabajo se enfoca en agentes basados en large language models (LLMs), ya que estos modelos de propósito general revolucionan las capacidades agénticas y, a diferencia de las generaciones agénticas anteriores, aportan más capacidades y uso generalizado.

Nuestro objetivo es proporcionar una referencia fácil de seguir, práctica y accionable sobre amenazas y mitigaciones de aplicaciones de IA Agéntica. Introducimos algunos conceptos básicos y utilizamos una arquitectura de referencia de IA agéntica, actuando como el lienzo para modelos de amenazas, para explicar y contextualizar las amenazas agénticas. Sin embargo, proporcionar una definición detallada y arquitectura de IA agéntica está más allá del alcance de nuestro trabajo.

Nuestro trabajo se enfoca en amenazas de IA Agéntica y se basa en directrices y estándares existentes, como el OWASP Top 10 para Aplicaciones LLM e IA Generativa, OWASP AI Exchange, OWASP Top 10, y el OWASP Top 10 para APIs para abordar aspectos relacionados inherentes en la construcción de aplicaciones de IA. Cuando es relevante, destacamos el impacto de la IA Agéntica en amenazas y riesgos existentes.

La audiencia objetivo de este documento son constructores y defensores de aplicaciones agénticas, incluyendo desarrolladores, arquitectos, ingenieros de plataforma y QA, y profesionales de seguridad. Este es nuestro primer reporte, y planeamos proporcionar guías adicionales basadas en roles como seguimiento a este documento para audiencias técnicas y de toma de decisiones.

