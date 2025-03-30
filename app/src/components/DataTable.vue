<template>
  <div v-if="operadoras">
    <v-data-table
      v-model:items-per-page="itemsPerPage"
      :headers="headers"
      :items="data"
      item-value="userID"
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
      itemsPerPage: 20,
      headers: [
        {
          key: 'userID',
          title: 'User Id',
          align: 'start',
          sortable: false,
        },
        {
          key: 'title',
          title: 'Title',
          align: 'start',
        },
        {
          key: 'body',
          title: 'Body',
          align: 'start',
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
  --header-bg: #f8f9fa;
  --header-color: #2c3e50;
  --row-hover: #f4f4f4;
  --border-color: #eceef1;
}

.v-data-table {
  width: 100%;
  max-width: 1200px;
  margin: 2rem auto;
  border-radius: 12px;
  overflow: hidden;
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.02),
    0 1px 2px rgba(0, 0, 0, 0.14);
  background: var(--table-bg);
}

:deep(.v-data-table-header) {
  background: var(--header-bg);
  position: sticky;
  top: 0;
  z-index: 2;
}

:deep(.v-data-table-header__content) {
  color: var(--header-color) !important;
  font-weight: 600;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 16px 24px;
}

:deep(.v-data-table__tr) {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

:deep(.v-data-table__tr:hover) {
  background: var(--row-hover) !important;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

:deep(td) {
  padding: 14px 24px !important;
  font-size: 0.925rem;
  color: #4a5568 !important;
  border-bottom: 1px solid var(--border-color) !important;
  white-space: nowrap;
}

:deep(th),
:deep(td) {
  min-width: 180px;
}

:deep(th:first-child),
:deep(td:first-child) {
  min-width: 120px;
  max-width: 160px;
}

:deep(.v-data-table-footer) {
  border-top: 1px solid var(--border-color);
  background: var(--header-bg);
  padding: 16px 24px;
}

@media (max-width: 768px) {
  .v-data-table {
    margin: 1rem;
    border-radius: 8px;
    overflow-x: auto;
  }

  :deep(table) {
    min-width: 600px;
  }

  :deep(th),
  :deep(td) {
    padding: 12px 16px !important;
    font-size: 0.875rem;
  }
}

.loading-message {
  padding: 2rem;
  text-align: center;
  color: #718096;
}
</style>
