# 🎮 PingPong - Refatoração + SOLID

Este projeto é uma refatoração do clássico jogo **Pong**, desenvolvida em **Python** com foco na aplicação dos princípios **SOLID** e boas práticas de engenharia de software.

O objetivo principal é transformar um código monolítico e acoplado em uma arquitetura **modular, extensível e de fácil manutenção**.

---

## 📁 Estrutura do Projeto

A aplicação foi organizada em módulos coesos, cada um com responsabilidades bem definidas:

```
.
├── main.py
└── src/
    ├── constants.py
    ├── entities.py
    ├── renderer.py
    └── game.py
```

### 🔹 `main.py`

- Ponto de entrada da aplicação.
- Responsável apenas por inicializar e iniciar o jogo.
- Mantém o desacoplamento da lógica principal.

---

### 🔹 `src/constants.py`

- Centraliza **todas as constantes globais** do sistema:
  - Cores
  - Dimensões da tela
  - Velocidades

- Evita “números mágicos” espalhados pelo código.
- Facilita ajustes e manutenção.

---

### 🔹 `src/entities.py`

- Contém as entidades principais do jogo:
  - `Paddle` (Raquete)
  - `Ball` (Bola)

- Cada classe encapsula:
  - Estado (posição, velocidade)
  - Comportamento (movimento, colisão)

✔ Responsabilidade clara: **modelar os objetos do jogo**

---

### 🔹 `src/renderer.py`

- Responsável exclusivamente pela **renderização gráfica**.
- Desenha:
  - Objetos
  - Tela
  - Elementos visuais

✔ Separação total entre lógica e apresentação.

---

### 🔹 `src/game.py`

- Controla o **loop principal do jogo**:
  - Eventos
  - Atualização de estado
  - Integração entre entidades e renderização

✔ Atua como o “orquestrador” do sistema.

---

## 🧠 Princípios de Engenharia Aplicados

### ✅ 1. Single Responsibility Principle (SRP)

Cada módulo/classe tem **uma única responsabilidade bem definida**:

- `Ball` → lógica da bola
- `Paddle` → lógica da raquete
- `Renderer` → desenho na tela
- `Game` → fluxo do jogo

---

### ✅ 2. Open/Closed Principle (OCP)

O sistema está **aberto para extensão, mas fechado para modificação**:

- Novas entidades podem ser adicionadas sem alterar o core
- Exemplo: adicionar IA, power-ups ou múltiplas bolas

---

### ✅ 3. Encapsulamento

- Estados internos protegidos dentro das classes
- Redução de dependências externas
- Eliminação de variáveis globais desnecessárias

---

### ✅ 4. Modularidade

- Código dividido em partes independentes
- Facilita:
  - Testes
  - Manutenção
  - Reutilização

---

### ✅ 5. Baixo Acoplamento

- Módulos se comunicam de forma controlada
- Mudanças em um módulo não quebram os outros

---

### ✅ 6. Alta Coesão

- Cada módulo faz **bem uma única coisa**
- Código mais legível e previsível

---

## ⚙️ Como Executar

### 1. Instale as dependências

```bash
pip install pygame
```

---

### 2. Execute o projeto

```bash
python main.py
```

---

## 🚀 Benefícios da Refatoração

- ✔ Código mais limpo e organizado
- ✔ Facilidade para adicionar novas funcionalidades
- ✔ Melhor legibilidade
- ✔ Redução de bugs
- ✔ Arquitetura escalável
