<template lang='html'>
	<div class="container">
		<div class="row">
			<div class="col">
				<h3>Do you want to delete this note?</h3>
				<hr>
				<p>NoteId : {{ this.element.id }}</p>
				<p>Note text : {{ this.element.note }}</p>
			</div>
		</div>
		<div class="rows">
			<div class="col text-left">
					<b-button v-on:click="deleteNote" variant="danger">Delete</b-button>
					<b-button type="submit" class="btn-large-space" :to="{ name: 'ListNote' }">Cancel</b-button>
			</div>
		</div>
	</div>
</template>


<script>
import axios from 'axios'
import swal from 'sweetalert'
export default {
 data () {
 	return{

 		noteId: this.$route.params.noteId,

 		element:{
 			id: '',
 			note: '',
 		}
 	}
 },
 methods: {
		getNote () {
			const path = 'http://127.0.0.1:8000/api/notes/' + this.noteId + '/'
			axios.get(path).then((response) => {
				this.element.id = response.data.id
				this.element.note = response.data.note
			})
			.catch((response) => {
				swal("Sorry, there is a problem with the element!", "", "error")
			})
		},
		deleteNote () {
			const path = 'http://127.0.0.1:8000/api/notes/' + this.noteId + '/'
			axios.delete(path).then((response) => {
				location.href = '/'
			}).catch((error) => {
				swal("The note could not be deleted", "", "error")
			})
		}
 },
 created () {
	this.getNote()
 }
}
</script>
<style lang="css" scoped>
</style>