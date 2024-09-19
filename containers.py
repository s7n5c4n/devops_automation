#containers.py
import docker

class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()

    def create_container(self, image_name: str, container_name: str):
        container = self.client.containers.run(image_name, name = container_name, detach=True)
        return container
    
    def stop_container(self, container_name: str):
        container = self.client.containers.get(container_name)
        container.stop()
        container.remove()