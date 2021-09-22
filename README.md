## COMPANY AND PRODUCTS PROJECT

### **criação da estrutura inicial do projeto**

- criar o ambiente virtual

```
python3 -m venv .venv

```
- ativar o ambiente

```
source .venv/bin/activate
```
- instalar gerenciador de dependencias
```
pip install pip-tools
```
- criar o arquivos para compilação das dependencias
```
touch requirements.in requirements-dev.in
echo 'django' > requirements.in
echo '-r requirements.in' > requirements-dev.in
```
- incluir dependencias de desenvolvimento em requirements-dev.in
```
pytest
flake8
black
```
- compilar as dependencias
```
pip-compile requirements.in --generate-hashes
pip-compile requirements-dev.in --generate-hashes
```
- instalar dependencias
```
pip install -r requirements-dev.txt
```
