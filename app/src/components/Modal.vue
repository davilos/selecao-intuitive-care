<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          <h2 class="modal-title">Filtrar Operadoras</h2>
        </slot>
        <button type="button" class="btn-close" @click="close">×</button>
      </header>

      <section class="modal-body">
        <slot name="body">
          <form @submit.prevent="handleSubmit" class="modal-form">
            <div class="form-group">
              <label for="ans">Registro ANS</label>
              <input type="text" id="ans" placeholder="000000" class="form-input" :maxlength="20" />
            </div>

            <div class="form-group">
              <label for="operadora">Nome da Operadora</label>
              <input
                type="text"
                id="operadora"
                class="form-input"
                :maxlength="200"
                placeholder="SUL AMÉRICA SEGURADORA DE SAÚDE S.A."
              />
            </div>

            <div class="form-group">
              <label for="cnpj">CNPJ</label>
              <input
                type="text"
                id="cnpj"
                placeholder="13339532000109"
                class="form-input"
                :maxlength="14"
              />
            </div>
          </form>
        </slot>
      </section>

      <footer class="modal-footer">
        <slot name="footer">
          <div class="footer-actions">
            <button type="submit" class="btn-filter" @click="handleSubmit">Buscar</button>
          </div>
        </slot>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  methods: {
    close() {
      this.$emit('close')
    },
    handleSubmit() {
      this.$emit('save')
      this.close()
    },
  },
}
</script>

<style>
:root {
  --primary-color: #4361ee;
  --primary-hover: #3748b5;
  --text-color: #2b2d42;
  --border-color: #dee2e6;
  --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal {
  background: white;
  width: 100%;
  max-width: 500px;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  overflow: hidden;
}

.modal-header {
  padding: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-color);
}

.modal-title {
  margin: 0;
  font-size: 1.5rem;
  color: var(--text-color);
  font-weight: 600;
}

.btn-close {
  border: none;
  background: none;
  font-size: 28px;
  color: #6c757d;
  cursor: pointer;
  padding: 8px;
  transition: var(--transition);
}

.btn-close:hover {
  color: var(--primary-color);
  transform: rotate(90deg);
}

.modal-body {
  padding: 24px;
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 500;
  color: var(--text-color);
}

.form-input {
  padding: 12px 16px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  font-size: 1rem;
  transition: var(--transition);
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.1);
}

.modal-footer {
  padding: 24px;
  border-top: 1px solid var(--border-color);
}

.footer-actions {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
}

.btn-filter {
  background-color: var(--primary-color);
  color: #ffffff !important;
  padding: 12px 28px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
}

.btn-filter:hover {
  background-color: var(--primary-hover);
  transform: translateY(-1px);
}
</style>
