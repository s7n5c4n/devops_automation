# infra.py
class TerraformConfig:
    def __init__(self, resource_type: str, resource_name: str, config_params: dict):
        self.resource_type = resource_type
        self.resource_name = resource_name
        self.config_params = config_params

    def generate_config(self):
        config = f"""
        resource "{self.resource_type}" "{self.resource_name}" {{
          {', '.join([f'{key} = "{value}"' for key, value in self.config_params.items()])}
        }}
        """
        with open(f'{self.resource_name}.tf', 'w') as f:
            f.write(config)

class AnsiblePlaybook:
    def __init__(self, host: str, roles: list):
        self.host = host
        self.roles = roles

    def generate_playbook(self):
        playbook = f"""
        - hosts: {self.host}
          roles:
            - {', '.join(self.roles)}
        """
        with open('playbook.yml', 'w') as f:
            f.write(playbook)
