import { ref } from 'vue'

export const getAllOperadoras = () => {
  const operadoras = ref(null)
  const error = ref(null)

  const load = async () => {
    try {
      await fetch('http://127.0.0.1:5000/get-all-operadoras')
        .then(function (response) {
          return response.json()
        })
        .then(function (json) {
          return (operadoras.value = json.data)
        })
    } catch (error) {
      error.value = error.message
      console.log(error.value)
    }
  }

  console.log('operadoras:::', operadoras)

  return { operadoras, error, load }
}
