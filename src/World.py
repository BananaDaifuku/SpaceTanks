class World:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def update(self):
        for entity in self.entities:
            entity.update()

    def render(self):
        for entity in self.entities:
            entity.render()