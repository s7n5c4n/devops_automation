#cicd.py
class CICDpipeline:
    def __init__(self, platform: str):
        self.platform = platform

    def generate_pipeline(self, language: str, test_command: str, deploy_command: str):
        if self.platform == "github":
            self._generate_github_workflow(language, test_command, deploy_command)
        elif self.platform == "gitlab":
            self._generate_gitlab_pipeline(language, test_command, deploy_command)

    def _generate_github_workflow(self, language: str, test_command: str, deploy_command: str):
        workflow = f"""
        name: CI/CD Pipeline
        on: [push]
        jobs:
            build:
            runs-on: ubuntu-latest
            steps:
            - uses: actions/checkout@v2
            - name: Set up Python {language}
                uses: actions/setup-python@v2
                with:
                python-version: '{language}'
            - name: Install dependencies
                run: |
                python -m pip install --upgrade pip
                pip install pytest
            - name: Test
                run: |
                {test_command}
            - name: Deploy
                run: |
                {deploy_command}
        """ 
        with open("github_workflow.yml", "w") as f:
            f.write(workflow)

    def _generate_gitlab_pipeline(self, language: str, test_command: str, deploy_command: str):
        pipeline = f"""
        image: python:{language}
        stages:
            - test
            - deploy
        test:
            stage: test
            script:
                - {test_command}
        deploy:
            stage: deploy
            script:
                - {deploy_command}
        """
        with open("gitlab_pipeline.yml", "w") as f:
            f.write(pipeline)
        