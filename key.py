from roboflow import Roboflow
rf = Roboflow(api_key="VMtwHVIntP4wLdXKXoFs")
project = rf.workspace("louie-fsst3").project("asl-3lsdf-6qkxy")
version = project.version(2)
dataset = version.download("yolov8")
                