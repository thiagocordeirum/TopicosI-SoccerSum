# Projeto Prático 2: Detecção e Segmentação em Partidas de Futebol com YOLOv26

Este repositório contém a implementação do **Projeto Prático 2 (YOLO26) da disciplina Tópicos para Computação 1 (2026.1)**, ministrada pela **Profa. Dra. Elloá B. Guedes** na **Escola Superior de Tecnologia (EST/UEA)**.

---

## 📁 Estrutura do Projeto

```
├── Eliteserien/
│   ├── 2021/
│   ├── 2022/
│   └── 2023/
├── NotebookAP2_TEC1.ipynb
├── .venv/
└── README.md
```

- **Eliteserien/** → Dataset contendo frames e anotações de detecção e segmentação (2021-2023)
- **NotebookAP2_TEC1.ipynb** → Notebook contendo toda a implementação do treinamento e avaliação do modelo YOLOv8
- **.venv/** → Ambiente virtual Python com as dependências do projeto
- **README.md** → Documentação do projeto

---

## ⚙️ Descrição da Atividade

A atividade consiste na utilização da arquitetura **YOLOv8** para resolver problemas de **detecção de objetos e segmentação de instâncias** em partidas de futebol profissional.

O experimento utiliza o **Eliteserien Dataset**, que contém imagens de partidas da liga principal da Noruega. O dataset é composto por 750 amostras balanceadas, focando em classes fundamentais para a análise de jogo:

- **Ball** (Bola)
- **Player** (Jogador)
- **Referee** (Árbitro)
- **Goalkeeper** (Goleiro)

O objetivo principal é treinar um modelo robusto capaz de identificar e segmentar esses elementos, avaliando seu desempenho em cenários reais de transmissão esportiva.

---

## 🔎 Etapas do Processamento

### 🔸 Preparação do Dataset

As imagens e anotações são organizadas seguindo o padrão esperado pelo framework **Ultralytics**. O dataset original foi particionado para garantir um equilíbrio entre as classes e os anos das partidas (2021, 2022 e 2023).

As transformações aplicadas incluem:
- Redimensionamento para **640x640** pixels
- Normalização de cores
- Organização em formato YOLO para detecção e segmentação

---

### 🔸 Divisão dos Dados

O dataset de 750 amostras foi dividido da seguinte forma:

- **Treinamento (70%)** – 525 imagens utilizadas para o ajuste dos pesos do modelo.
- **Validação (10%)** – 75 imagens utilizadas para monitoramento e ajuste de hiperparâmetros.
- **Teste (20%)** – 150 imagens utilizadas para a avaliação final da capacidade de generalização.

---

### 🔸 Arquitetura da Rede Neural

Foi utilizada a arquitetura **YOLOv8 (You Only Look Once)**, especificamente as versões:
- **YOLOv8n (nano)**: Para detecção de caixas delimitadoras (bounding boxes).
- **YOLOv8n-seg**: Para segmentação de instâncias.

O YOLOv8 é conhecido por sua alta eficiência e precisão em tempo real, sendo o estado da arte para tarefas de visão computacional em dispositivos com recursos limitados.

---

### 🔸 Treinamento do Modelo

O treinamento foi configurado com os seguintes parâmetros:

- **Epochs**: 100
- **Batch size**: 16
- **Image size**: 640
- **Otimizador**: Automático (SGD/AdamW)

Durante o processo, foram registradas métricas de perda (loss) para coordenadas de caixa, classificação e máquinas de segmentação.

---

### 🔸 Monitoramento do Treinamento

O progresso foi monitorado através de gráficos gerados pelo framework:
- Evolução da **Loss de Treinamento e Validação**
- Curvas de **Precisão e Recall**
- Gráficos de **mAP (mean Average Precision)**

Essas métricas permitem identificar se o modelo está convergindo corretamente ou se há sinais de overfitting.

---

### 🔸 Avaliação do Modelo

Após o treinamento, os melhores pesos foram avaliados no conjunto de teste (150 imagens). As principais métricas de avaliação foram:

- **Box mAP@50**: Precisão média para detecção com IoU de 0.5.
- **Box mAP@50-95**: Média da precisão em diferentes limiares de IoU.
- **Mask mAP@50/50-95**: Métricas equivalentes para a tarefa de segmentação.

---

### 🔸 Análise de Predições

Para validação qualitativa, o modelo foi testado em frames aleatórios do conjunto de teste, exibindo:
- Caixas delimitadoras com as classes e scores de confiança.
- Máscaras de segmentação sobrepostas aos jogadores e bola.

Essa análise visual confirma a eficácia do modelo em lidar com oclusões e diferentes ângulos de câmera típicos de transmisões de futebol.

---

## 🧰 Tecnologias Utilizadas

- **Python**
- **Ultralytics (YOLOv26)** – Framework principal para visão computacional
- **OpenCV** – Processamento de imagens e vídeos
- **Matplotlib** – Visualização de resultados e gráficos
- **Pandas** – Manipulação de dados de anotação
- **PyTorch** – Engine de backend para processamento em GPU/CPU

---

## 👥 Autores

| [<img src="https://github.com/thiagocordeirum.png?size=100" width=100><br><sub>Thiago Cordeiro</sub>](https://github.com/thiagocordeirum) | [<img src="https://github.com/beatrizguedes03.png?size=100" width=100><br><sub>Beatriz Guedes</sub>](https://github.com/beatrizguedes03) | [<img src="https://github.com/yagofeitoza19.png?size=100" width=100><br><sub>Yago Feitoza</sub>](https://github.com/yagofeitoza19) | [<img src="https://github.com/ordozgoite.png?size=100" width=100><br><sub>Victor Ordozgoite</sub>](https://github.com/ordozgoite) | [<img src="https://github.com/ItaloFonseca.png?size=100" width=100><br><sub>Italo Fonseca</sub>](https://github.com/ItaloFonseca)
|:---:|:---:|:---:|:---:|:---:|

---

## 👩‍🏫 Orientação

- Orientador(a): **Profa. Dra. Elloá B. Guedes**
- Instituição: **Escola Superior de Tecnologia – Universidade do Estado do Amazonas (EST/UEA)**
- Data: **Junho de 2026**
