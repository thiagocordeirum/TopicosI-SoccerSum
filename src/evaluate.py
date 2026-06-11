from pathlib import Path
import torch
from ultralytics import YOLO

# --- Configuração de Caminhos ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_CONFIG = BASE_DIR / "data" / "dataset.yaml"
RUNS_DIR = BASE_DIR / "runs/detect/runs"

# --- Modelos Treinados (Apontando para os pesos gerados após o treino) ---
# O YOLO salva os resultados em: runs/nome_do_experimento/weights/best.pt
MODELS_TO_EVALUATE = [
    {
        "name": "yolo26n",
        "weights": RUNS_DIR / "yolo26n" / "weights" / "best.pt"
    },
    {
        "name": "yolo26s",
        "weights": RUNS_DIR / "yolo26s" / "weights" / "best.pt"
    }
]

# --- Hiperparâmetros de Avaliação ---
IMAGE_SIZE = 640
BATCH_SIZE = 8  
DEVICE = 0
WORKERS = 2

def evaluate_model(model_info: dict) -> None:
    """
    Evaluate a trained YOLO model on the test dataset split.
    """
    model_path = model_info["weights"]
    experiment_name = f"val_{model_info['name']}"

    if not model_path.exists():
        print(f"Erro: Os pesos do modelo não foram encontrados em: {model_path}")
        print("Certifique-se de rodar o treino antes de executar a avaliação.")
        return

    # Carrega o modelo com os melhores pesos obtidos no treino
    model = YOLO(str(model_path))

    print(f"\n[EVAL] Avaliando {model_info['name']} no conjunto de TESTE...")
    
    # Executa a validação forçando o split de teste
    metrics = model.val(
        data=str(DATASET_CONFIG),
        split="test",          # <-- Força o uso do split de teste do dataset.yaml
        imgsz=IMAGE_SIZE,
        batch=BATCH_SIZE,
        device=DEVICE,
        workers=WORKERS,
        project=str(RUNS_DIR / "val"), # Salva isolado dentro de runs/val/
        name=experiment_name
    )

    # Exibe um sumário rápido das métricas de detecção no terminal
    print(f"\n=== Resultados Finais de Teste ({model_info['name']}) ===")
    print(f"Box mAP@50:    {metrics.box.map50:.4f}")
    print(f"Box mAP@50-95: {metrics.box.map:.4f}")


def evaluate() -> None:
    print(f"Torch: {torch.__version__}")
    print(f"CUDA Available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    for model_info in MODELS_TO_EVALUATE:
        print(f"\nEvaluating weights from {model_info['name']}")
        print("-" * 50)

        evaluate_model(model_info)


if __name__ == "__main__":
    evaluate()