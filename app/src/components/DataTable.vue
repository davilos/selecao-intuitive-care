<template>
  <div v-if="operadoras" class="table-container">
    <v-data-table
      v-model:items-per-page="itemsPerPage"
      :headers="headers"
      :items="data"
      class="elevation-1"
    >
    </v-data-table>
  </div>
</template>

<script>
import { VDataTable } from 'vuetify/components'
import { getAllOperadoras } from '../services/getAllOperadoras'

export default {
  components: {
    VDataTable,
  },
  setup() {
    const { operadoras, error, load } = getAllOperadoras()

    load()

    return {
      operadoras,
      error,
      load,
      itemsPerPage: 10,
      headers: [
        {
          key: 'registro_ans',
          title: 'Registro ANS',
          align: 'start',
          sortable: false,
        },
        {
          key: 'cnpj',
          title: 'CNPJ',
          align: 'start',
          sortable: false,
        },
        {
          key: 'razao_social',
          title: 'Razão Social',
          align: 'start',
          sortable: true,
        },
        {
          key: 'nome_fantasia',
          title: 'Nome Fantasia',
          align: 'start',
          sortable: false,
        },
        {
          key: 'modalidade',
          title: 'Modalidade',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.cep',
          title: 'CEP',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.cidade',
          title: 'Cidade',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.uf',
          title: 'UF',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.bairro',
          title: 'Bairro',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.logradouro',
          title: 'Logradouro',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.numero',
          title: 'Número',
          align: 'start',
          sortable: false,
        },
        {
          key: 'endereco.complemento',
          title: 'Complemento',
          align: 'start',
          sortable: false,
        },
        {
          key: 'contato.telefone',
          title: 'Telefone',
          align: 'start',
          sortable: false,
        },
        {
          key: 'contato.fax',
          title: 'Fax',
          align: 'start',
          sortable: false,
        },
        {
          key: 'contato.email',
          title: 'Email',
          align: 'start',
          sortable: false,
        },
        {
          key: 'responsavel.nome',
          title: 'Responsável',
          align: 'start',
          sortable: false,
        },
        {
          key: 'responsavel.cargo',
          title: 'Cargo do Responsável',
          align: 'start',
          sortable: false,
        },
        {
          key: 'regiao_comercializacao',
          title: 'Região de Comercialização',
          align: 'start',
          sortable: false,
        },
        {
          key: 'data_registro',
          title: 'Data Registro',
          align: 'start',
          sortable: false,
        },
      ],
      data: operadoras,
    }
  },
}
</script>

<style scoped>
:root {
  --table-bg: #ffffff;
  --header-bg: linear-gradient(145deg, #f8f9fa 0%, #e9ecef 100%);
  --header-color: #2b2d42;
  --row-hover: #f1faee;
  --border-color: #dee2e6;
  --accent-color: #4361ee;
}

.table-container {
  padding: 2rem;
  background: #f8f9fa;
  min-height: 100vh;
}

.custom-data-table {
  width: 100%;
  max-width: 1600px;
  margin: 0 auto;
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 10px 15px -3px rgba(0, 0, 0, 0.03),
    0 4px 6px -4px rgba(0, 0, 0, 0.03);
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease;
}

.custom-data-table:hover {
  transform: translateY(-2px);
}

:deep(.v-data-table-header) {
  background: var(--header-bg);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

:deep(.v-data-table-header__content) {
  color: var(--header-color) !important;
  font-weight: 700;
  font-size: 0.95rem;
  letter-spacing: 0.25px;
  padding: 20px 32px;
}

:deep(.v-data-table__tr) {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
}

:deep(.v-data-table__tr:hover) {
  background: var(--row-hover) !important;
  transform: translateY(-2px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  z-index: 1;
}

:deep(td) {
  padding: 18px 32px !important;
  font-size: 0.95rem;
  color: #495057 !important;
  border-bottom: 1px solid var(--border-color) !important;
  vertical-align: middle;
}

:deep(th),
:deep(td) {
  min-width: 220px;
}

:deep(th:first-child),
:deep(td:first-child) {
  min-width: 160px;
  max-width: 200px;
}

:deep(.v-data-table-footer) {
  border-top: 1px solid var(--border-color);
  background: var(--header-bg);
  padding: 20px 32px;
}

:deep(.v-data-table__td:not(:last-child)) {
  border-right: 1px solid var(--border-color);
}

:deep(.v-data-table__tr:nth-child(even)) {
  background-color: #fcfcfc;
}

:deep(.v-data-table__td:last-child) {
  border-radius: 0 8px 8px 0;
}

.loading-message {
  padding: 2rem;
  text-align: center;
  color: #6c757d;
  font-size: 1.1rem;
}

.table-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1.5rem;
  max-width: 1600px;
  margin: 0 auto 2rem;
  padding: 0 32px;
  width: 100%;
}
</style>
