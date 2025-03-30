SELECT 
    o.Razao_Social AS Operadora,
    SUM(d.VL_SALDO_FINAL) AS Total_Despesas
FROM 
    demonstracao_contabeis d
INNER JOIN 
    operadoras o ON d.REG_ANS = o.Registro_ANS
WHERE 
    d.DESCRICAO LIKE '%EVENTOS/%SINISTROS CONHECIDOS%ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.DATA BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    Operadora
ORDER BY 
    Total_Despesas DESC
LIMIT 10;

