from pathlib import Path

import torch
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_CONFIG = BASE_DIR / "data" / "dataset.yaml"
MODELS_DIR = BASE_DIR / "models"
RUNS_DIR = BASE_DIR / "runs"

MODELS = [
    MODELS_DIR / "yolo26n.pt",
    MODELS_DIR / "yolo26s.pt"
]

EPOCHS = 100
IMAGE_SIZE = 640
BATCH_SIZE = 8
LEARNING_RATE = 0.001
PATIENCE = 20
FREEZE = 10

DEVICE = 0
WORKERS = 2

PROJECT_NAME = "runs"

def train_model(model_path: Path) -> None:
    """
    Train a single YOLO model.
    """

    experiment_name = Path(model_path).stem

    model = YOLO(str(model_path))

    model.train(
        data=str(DATASET_CONFIG),
        epochs=EPOCHS,
        imgsz=IMAGE_SIZE,
        batch=BATCH_SIZE,
        lr0=LEARNING_RATE,
        patience=PATIENCE,
        freeze=FREEZE,
        device=DEVICE,
        workers=WORKERS,
        project=str(RUNS_DIR),
        name=experiment_name
    )


def train() -> None:

    print(f"Torch: {torch.__version__}")
    print(f"CUDA Available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    for model_name in MODELS:

        print(f"\nTraining {model_name}")
        print("-" * 50)

        train_model(model_name)


if __name__ == "__main__":
    train()