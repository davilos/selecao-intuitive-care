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
      itemsPerPage: 10,
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
