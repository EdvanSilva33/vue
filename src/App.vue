<script setup>
import { reactive } from 'vue';
const estado = reactive({
  filtro: 'todas',
  tarefaTemp: ' ',
  tarefas: [
    {
      titulo: 'Estudar ES6',
      finalizada: false,

    },
    {
      titulo:'Estudar SaSS',
      finalizada: false,


    },
    {
      titulo: 'Ir pra a Academia',
      finalizada:false,
    },

    {
      titulo: 'Estudar a VueJs',
      finalizada:false,
    }
  ]

})

const getTarefasPendentes = () =>{
  return estado.tarefas.filter(tarefa => !tarefa.finalizada)
  
}

const getTarefasFinalizadas = () =>{
  return estado.tarefas.filter(tarefa => tarefa.finalizada)
  
}

const getTarefasFiltradas = () =>{
const {filtro} = estado;

switch (filtro){
  case 'pendentes':
    return getTarefasPendentes();
  case 'finalizadas':
    return getTarefasFinalizadas();
  default:
    return estado.tarefas;
}

}

const cadastraTarefa = ()=>{
const tarefaNova = {
  titulo: estado.tarefaTemp,
  finalizada: false,
}
estado.tarefas.push(tarefaNova);
estado.tarefaTemp = '';
}
</script>

<template>
<div class="container">
  <header class="p-5 mb4 mt4 bg-light rounded-3">
    <h1>Minhas tarefas</h1>
    <p>
      Voce possui {{ getTarefasPendentes().length }} tarefas pendente!
    </p>
  </header>

  <form @submit.prevent="cadastraTarefa">
     <div class="row">
      <div class="col">
        <input :value = "estado.tarefaTemp"  @change="evento => estado.tarefaTemp = evento.target.value" type="text" placeholder="Digite aqui a descriçõa de tarefa " required class="form-control">

      </div>
<div class="col-md-2">
  <button type="submit" class="btn btn-primary">Cadastrar</button>
</div>
<div class="col-md-2">
  <select @change="evento => estado.filtro = evento.target.value" class="form-control">
    <option value="todas">Todas tarefas</option>
    <option value="pendentes">pendentes</option>

    <option value="finalizadas">finalizadas tarefas</option>
  </select>
</div>
     </div>
  </form>

<ul class="list-gruop mt-4">
  <li class="list-group-item" v-for="tarefa in getTarefasFiltradas() ">
    <input @change="evento => tarefa.finalizada = evento.target.checked" :checked="tarefa.finalizada" :id="tarefa.titulo" type="checkbox" >

    <label :for="tarefa.titulo" :class=" {done: tarefa.finalizada}" class="ms-3">
      {{ tarefa.titulo}}

    </label>
  </li>
</ul>
</div>
</template>

<style scoped>
.done{
  text-decoration: line-through red;
}

</style>
