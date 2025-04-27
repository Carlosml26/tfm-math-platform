from jinja2 import Environment, FileSystemLoader
import os

PROMPTS_DIR = os.path.join(os.path.dirname(__file__))

env = Environment(
    loader=FileSystemLoader(PROMPTS_DIR),
    trim_blocks=True,
    lstrip_blocks=True
)

def render_prompt(template_name: str, context: dict) -> str:
    """
    Renderiza un template Jinja2 ubicado en config/prompts/.
    """
    template = env.get_template(template_name)
    return template.render(**context)
