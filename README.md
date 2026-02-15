# Log Analysis Lab – Detecção de Força Bruta

## Objetivo
Demonstrar a análise de logs de autenticação para identificar tentativas suspeitas
de login com falha.

## Cenário
Um analista de segurança revisa registros de login para detectar possíveis ataques
de força bruta a partir de padrões repetidos de falha.

## Análise Automatizada
Foi desenvolvido um script em Python para identificar e contar tentativas de login
com falha por usuário e endereço IP. Eventos com três ou mais falhas consecutivas
foram classificados como risco elevado, indicando possível ataque de força bruta.

## Método
Os registros de autenticação foram processados automaticamente pelo script,
que leu os logs, identificou falhas de login e agrupou ocorrências por usuário
e endereço IP.

## Resultados
Foram identificadas quatro tentativas de login com falha para o usuário "admin",
originadas do mesmo endereço IP externo, indicando risco elevado.

## Conclusão
A análise de logs permite a detecção precoce de acessos não autorizados, contribuindo
para a proteção da confidencialidade e integridade dos sistemas.
