from cubes.server import slicer
from cubes import Workspace

# Load model
model_path = "model.json"
model = Workspace(config=model_path).model

# Create slicer server
server = slicer.Slicer()

# Register model with the server
server.register_model("my_cube", model)

# Create and register a data store
store_path = "data.csv"
store = slicer.create_store("csv", store_path)
server.register_store("my_store", store)

# Link model and data store
server.link_store("my_cube", "my_store")

# Start the server
server.run()