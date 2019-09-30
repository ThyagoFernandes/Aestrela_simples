# Aestrela_simples
Este é um solução em python usando A* para um exercício sugerido na disciplina de IA para jogos do curso de BTI da UFRN.
A movimentação neste é apenas horizontalmente e verticalmente (Cima e Baixo).
O ponto de partidade e de chegada é dado Respectivamente por A e B e será utilizado como heurística a distância Manhattan. Este código deve ser executado com a versão python 3.x.

Para executar o código use o seguinte comando:
```python
python Astar.py <Arquivo_do_mapa>
```
Ou caso exista uma versão python 2.x e outra seja 3.x:
```python
python3 Astar.py <Arquivo_do_mapa>
```
O arquivo do mapa deve ser ter apenas os caracteres 0, 1, A e B. Esse caracteres devem ser separados em coluna por espaço e em linha por quebra de linha (\n) e o grid precisa ser n x n.
