import { ref } from 'vue'

export const getAllOperadoras = () => {
  const operadoras = ref(null)
  const error = ref(null)

  const load = async () => {
    try {
      let data = await fetch('https://jsonplaceholder.typicode.com/posts')

      if (!data.ok) {
        throw Error('Não foi possível carregar as operadoras')
      }

      operadoras.value = await data.json()
    } catch (error) {
      error.value = error.message
      console.log(error.value)
    }
  }

  return { operadoras, error, load }
}
