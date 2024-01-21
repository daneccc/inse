'use client';
import React, { useEffect, Component } from 'react';
import axios from 'axios';
import useState from 'react';
import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import 'bootstrap/dist/css/bootstrap.min.css';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import { data } from './data.js';
import { networkTypeHelper, localeTypeHelper, capitalTypeHelper } from './helpers.js';
import { ufFilters, networkFilters, localeFilters } from './filters.js';
import Link from 'next/link';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedUfs: new Set(),
      selectednetworkType: new Set(),
      selectedLocaleType: new Set(),
      apiData: []
    };
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/schools/')
    .then((response) => {
      this.setState({
        apiData: response.data
      })
    })
    .catch((err) => {
      console.log(err);
    });
  }

  // const selectedUfs = new Set();
  handleUFChanges(value) { 
    if(this.state.selectedUfs.has(value)) {
      this.state.selectedUfs.delete(value)
      return
    }
    this.state.selectedUfs.add(value)
  }

  // const selectednetworkType = new Set();
  handleNetworkChanges(value) { 
    if(this.state.selectednetworkType.has(value)) {
      this.state.selectednetworkType.delete(value)
      return
    }
    this.state.selectednetworkType.add(value)
  }

  // const selectedLocaleType = new Set();
  handleLocaleChanges(value) { 
    if(this.state.selectedLocaleType.has(value)) {
      this.state.selectedLocaleType.delete(value)
      return
    }
    this.state.selectedLocaleType.add(value)
  }

  handleFilterButton = () => {
    let uf_path_value = "" 
    this.state.selectedUfs.forEach((value) => {
      uf_path_value = uf_path_value + "co_uf=" + value + "&"
    })

    let network_path_value = "" 
    this.state.selectednetworkType.forEach((value) => {
      network_path_value = network_path_value + "tp_tipo_rede=" + value + "&"
    })

    let locale_path_value = "" 
    this.state.selectedLocaleType.forEach((value) => {
      locale_path_value = locale_path_value + "tp_localizacao=" + value + "&"
    })
    const path = "http://localhost:8000/schools/filtered/?" + uf_path_value + network_path_value + locale_path_value

    axios.get(path)
    .then((response) => {
      this.setState({
        apiData: response.data
      })
    })
    .catch((err) => {
      console.log(err);
    });
  }

  openSchoolDetails(schoolsID) {
    navigate('/Details', {replace: true});
    console.log(schoolsID)
  }

  render() {
    return (
      <div>
      <Container>
        <h1 className='text-center mt-4'>Tabela Inse</h1>
        <Form>
          <InputGroup className='my-3'>

            {/* onChange for search */}
            <Form.Control
              // onChange={(e) => setSearch(e.target.value)}
              placeholder='Procurar escola por id'
            />
          </InputGroup>
        </Form>
        <Form>
          <InputGroup className='my-3'>

            {/* onChange for search */}
            <Form.Control
              // onChange={(e) => setSearch(e.target.value)}
              placeholder='Procurar município por id'
            />
          </InputGroup>
        </Form>
        <h4 className='text-left mt-4'>Filtrar UF</h4>
        <Row>
          {ufFilters
            .map((uf) => (
              <Col sm={3}>
                <Form.Check 
                type='checkbox'
                id='default-checkbox'
                label={uf.name}
                onChange={() => this.handleUFChanges(uf.id)}
                />
            </Col>
            ))
          }
        </Row>
        <h4 className='text-left mt-4'>Filtrar tipo de rede</h4>
        <Row>
          {networkFilters
            .map((network) => (
              <Col sm={3}>
                <Form.Check 
                type='checkbox'
                id='default-checkbox'
                label={network.name}
                onChange={() => this.handleNetworkChanges(network.id)}
                />
            </Col>
            ))
          }
        </Row>
        <h4 className='text-left mt-4'>Filtrar tipo de localização</h4>
        <Row>
          {localeFilters
            .map((locale) => (
              <Col sm={3}>
                <Form.Check 
                type='checkbox'
                id='default-checkbox'
                label={locale.name}
                onChange={() => this.handleLocaleChanges(locale.id)}
                />
            </Col>
            ))
          }
        </Row>

        <br></br>
        <div className="d-grid gap-2">
          <Button variant="primary" size="lg" onClick = {this.handleFilterButton}>
             Filtrar
          </Button>
        </div>
        <br></br>
        <br></br>

        <Table striped bordered hover>
          <thead>
            <tr>
              <th>UF</th>
              <th>Municipio</th>
              <th>Escola</th>
              <th>Tipo de rede</th>
              <th>Tipo de localização</th>
              <th>Tipo de capital</th>
              <th>Quantidade de alunos</th>
              <th>Media inse</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {this.state.apiData
              .map((item, index) => (
                <tr key={index}>
                  <td>{item.no_uf} ({item.sg_uf})</td>
                  <td>{item.no_municipio}</td>
                  <td>{item.no_escola}</td>
                  <td>{networkTypeHelper(item.tp_tipo_rede)}</td>
                  <td>{localeTypeHelper(item.tp_localizacao)}</td>
                  <td>{capitalTypeHelper(item.tp_capital)}</td>
                  <td>{item.qtd_alunos_inse}</td>
                  <td>{item.media_inse}</td>
                  <td>
                  <Link 
                    href={{
                      pathname: `/Details`,
                      query: {
                        id: item.id_escola
                      }
                    }}
                  >
                    <Button 
                      variant="primary" 
                      size="sm"
                    >
                      Detalhes
                    </Button>
                  </Link>
                  </td>
                </tr>
              ))}
          </tbody>
        </Table>
      </Container>
    </div>
    )
  }
}

export default Home;