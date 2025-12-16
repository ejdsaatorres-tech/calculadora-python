# 🧮 Calculadora API - Pipeline de Entrega Continua

Este proyecto implementa una API REST minimalista de una calculadora utilizando **Python** y **Flask**. 

El objetivo principal no es la complejidad de la aplicación, sino la demostración de un **Pipeline de CI/CD robusto**, integrando pruebas automáticas y análisis de seguridad estática según los principios de *Continuous Delivery*.

## 🚀 Tecnologías y Herramientas

*   **Lenguaje:** Python 3.9+
*   **Framework Web:** Flask
*   **Testing (Q1/Q2):** Pytest
*   **Calidad de Código (Q4):** Flake8 (Linter)
*   **Seguridad (Q4):** Snyk (Análisis de vulnerabilidades/SCA)
*   **Contenedorización (CD):** Docker
*   **Orquestación:** GitHub Actions

## ⚙️ Configuración e Instalación Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_CARPETA>
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la aplicación:**
    ```bash
    python app.py
    ```
    La API estará disponible en `http://localhost:5000`.

## 🧪 Ejecución de Pruebas (TDD)

El proyecto sigue una estrategia de pruebas basada en los Cuadrantes del Testing Ágil:

### Pruebas Unitarias e Integración (Q1/Q2)
Para verificar la lógica de la calculadora:
```bash
pytest