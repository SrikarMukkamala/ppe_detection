import yaml
from ultralytics import YOLO


with open(r"params.yaml") as f:
    params = yaml.safe_load(f)

# load a pre-trained model
pre_trained_model = YOLO(params['model_type'])

# train
model = pre_trained_model.train(
    data=DATA_YAML_PATH,
    imgsz=params['imgsz'],
    batch=params['batch'],
    epochs=params['epochs'],
    optimizer=params['optimizer'],
    lr0=params['lr0'],
    seed=params['seed'],
    pretrained=params['pretrained'],
    name=params['name']
)
