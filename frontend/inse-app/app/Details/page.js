'use client';

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useSearchParams } from 'next/navigation';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const Details = () => {
  const searchParams = useSearchParams();
  const id = searchParams.get('id');
  const path = `http://127.0.0.1:8000/schools/${id}/`;

  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get(path)
      .then((response) => {
        setData(response.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [id]); // Adicionando 'id' como dependência para a atualização do useEffect

  const descriptions = {
    nu_ano_saeb: 'Ano de aplicação do Saeb',
    co_uf: 'Código da Unidade da Federação',
    sg_uf: 'Sigla da Unidade da Federação',
    no_uf: 'Nome da Unidade da Federação',
    co_municipio: 'Código do Município',
    no_municipio: 'Nome do Município',
    id_escola: 'Código da Escola no CENSO Escolar',
    no_escola: 'Nome da Escola no CENSO Escolar',
    tp_tipo_rede: 'Dependência Administrativa da Escola',
    tp_localizacao: 'Localização da Escola',
    tp_capital: 'Área da Escola (relacionado ao Município)',
    qtd_alunos_inse: 'Quantidade de Alunos com INSE calculado',
    media_inse: 'Média do Indicador de Nível Socioeconômico dos alunos da escola',
    inse_classificacao: 'Classificação do Indicador de Nível Socioeconômico',
    pc_nivel_1: 'Percentual de alunos da Escola classificados no Nível I',
    pc_nivel_2: 'Percentual de alunos da Escola classificados no Nível II',
    pc_nivel_3: 'Percentual de alunos da Escola classificados no Nível III',
    pc_nivel_4: 'Percentual de alunos da Escola classificados no Nível IV',
    pc_nivel_5: 'Percentual de alunos da Escola classificados no Nível V',
    pc_nivel_6: 'Percentual de alunos da Escola classificados no Nível VI',
    pc_nivel_7: 'Percentual de alunos da Escola classificados no Nível VII',
    pc_nivel_8: 'Percentual de alunos da Escola classificados no Nível VIII',
  };

  const renderRow = (label, value) => (
    <Row key={label} className="mb-2">
      <Col sm={6}>
        <h4>{descriptions[label]}</h4>
      </Col>
      <Col sm={3}>
        <h5>{value}</h5>
      </Col>
    </Row>
  );

  return (
    <div>
      {data ? (
        <Container>
          {Object.keys(data).map((key) => renderRow(key, data[key]))}
        </Container>
      ) : (
        <h1>'Carregando...'</h1>
      )}
    </div>
  );
};

export default Details;
