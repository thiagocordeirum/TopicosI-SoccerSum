# Projeto Prático 2: Detecção em Partidas de Futebol com YOLOv26

Este repositório apresenta a implementação do **Projeto Prático 2** da disciplina **Tópicos para Computação 1 (2026.1)**, orientado pela **Profa. Dra. Elloá B. Guedes** no **Centro de Tecnologia (EST/UEA)**.

O objetivo do projeto é aplicar a arquitetura **YOLOv26** para detecção de objetos e segmentação de instâncias em imagens de partidas de futebol, utilizando o dataset **Eliteserien**.

---

## 📁 Estrutura do Repositório

```text
TopicosI-SoccerSum/
│
├── data/
│   ├── Eliteserien/                 # Dataset bruto 
│   ├── Eliteserien_partitioned/     # Dataset estruturado
│   │   ├── images/                  # Frames da partida (.jpg) [train, val, test]
│   │   └── labels/                  # Anotações em formato YOLO (.txt) [train, val, test]
│   └── dataset.yaml                 # Configuração do mapeamento de dados e classes do YOLO
│
├── src/
│   ├── __init__.py
│   ├── data_preparation.py          # Script de extração, split e validação dos dados
│   ├── train.py                     # Script para disparar o treinamento da rede neural
│   └── predict.py                   # Script para inferência e teste qualitativo com pesos .pt
│
├── .gitignore                       
├── NotebookAP2_TEC1.ipynb           # Notebook de desenvolvimento e prototipagem
└── README.md                        # Documentação do repositório

```

---

## Objetivo do Projeto

Detectar e segmentar objetos em imagens de futebol usando aprendizado de máquina. O modelo identifica as classes principais presentes nos jogos da liga norueguesa **Eliteserien**.

### Classes do dataset

- `0: Player`
- `1: Goalkeeper`
- `2: Referee`
- `3: Ball`
- `4: Logo`
- `5: Penalty mark`
- `6: Corner flag post`
- `7: Goal net`

---

## Fluxo de Trabalho

### 1. Preparação dos Dados

O script `src/data_preparation.py` cria a partição do dataset em formato YOLO:

- `train` → imagens de treino
- `val` → imagens de validação
- `test` → imagens de teste

Ele percorre os diretórios de `Eliteserien/` e copia imagens e anotações de detecção para a estrutura esperada pelo Ultralytics.

### 2. Configuração do Dataset

O arquivo `data/dataset.yaml` define o caminho base e as pastas de cada split:

- `train: images/train`
- `val: images/val`
- `test: images/test`

Assim, o modelo usa os dados particionados corretamente durante o treinamento.

### 3. Treinamento do Modelo

O script `src/train.py` carrega pesos iniciais a partir de arquivos em `models/` e executa o treinamento com:

- `epochs = 100`
- `imgsz = 640`
- `batch = 8`
- `lr0 = 0.001`
- `patience = 20`
- `freeze = 10`

O treinamento é realizado usando a biblioteca **Ultralytics YOLO** e salva resultados em `runs/`.

---

## Tecnologias e Bibliotecas

- Python 3
- Ultralytics YOLO (YOLOv26)
- PyTorch
- OpenCV
- Matplotlib
- Pandas

---

## Como Executar

### Preparar o dataset

```bash
python src/data_preparation.py
```

### Treinar o modelo

```bash
python src/train.py
```

> Certifique-se de que o ambiente virtual está ativo e que a biblioteca Ultralytics está instalada.

---

## Resultados Esperados

O projeto realiza:

- partição do dataset em treino, validação e teste
- treinamento de modelos YOLO com pesos iniciais
- avaliação da performance em diferentes métricas de detecção e segmentação
- análise qualitativa de predições em frames de futebol

---

## Observações

- O dataset original está em `Eliteserien/` com imagens e anotações separadas por ano.
- A estrutura final usada pelo treino é gerada em `data/Eliteserien_partitioned`.
- Os pesos de modelo usados no treino estão em `models/`.

---

## Autores

| [<img src="https://github.com/thiagocordeirum.png?size=100" width=100><br><sub>Thiago Cordeiro</sub>](https://github.com/thiagocordeirum) | [<img src="https://github.com/beatrizguedes03.png?size=100" width=100><br><sub>Beatriz Guedes</sub>](https://github.com/beatrizguedes03) | [<img src="https://github.com/yagofeitoza19.png?size=100" width=100><br><sub>Yago Feitoza</sub>](https://github.com/yagofeitoza19) | [<img src="https://github.com/ordozgoite.png?size=100" width=100><br><sub>Victor Ordozgoite</sub>](https://github.com/ordozgoite) | [<img src="https://github.com/ItaloFonseca.png?size=100" width=100><br><sub>Italo Fonseca</sub>](https://github.com/ItaloFonseca)
|:---:|:---:|:---:|:---:|:---:|

---

## Orientação

- **Profa. Dra. Elloá B. Guedes**
- **Escola Superior de Tecnologia – Universidade do Estado do Amazonas (EST/UEA)**
- **Junho de 2026**
