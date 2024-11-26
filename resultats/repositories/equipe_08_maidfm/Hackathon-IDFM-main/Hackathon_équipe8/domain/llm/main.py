from Hackathon_équipe8.domain.llm.llm_management import LLMConfiguration
from Hackathon_équipe8.config.prompts import prompt_test

llm_config = LLMConfiguration()

input = "I am a human"
response = llm_config.invoke(prompt_test.format(input = input))

print(f'response: {response.choices[0].message.content}')

print(f'Impact energy: {response.impacts.energy.value.max} kWh')
print(f'Impact co2: {response.impacts.usage.gwp.value.max} CO2eq')
