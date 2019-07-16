<template lang='html'>
	<div class="container">
		<div class="row">
			<div class="col">
				<div class="card">
					<div class="card-body">
						<form @submit="onSubmit">
							<vue-form-generator :schema="schema" :model="model" :options="formOptions">
							</vue-form-generator>
							<div class="rows">
								<div class="col text-left">
									<b-button type="submit" variant="primary">Edit</b-button>
									<b-button type="submit"class="btn-large-space" :to="{ name: 'ListNote' }">Cancel</b-button>
								</div>
							</div>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>


<script>
import validators from 'vue-form-generator'
import axios from 'axios'
import swal from 'sweetalert'
export default {
	data () {
		return {

			noteId: this.$route.params.noteId,

			model: {
				end_date: "2019-01-01",
				note: "",
				tags: "",
				task: "",
				type_field: "",
			},

			schema: {
				groups: [
					{
						legend: "Edit Note",
						fields: [
							{
							    type: "input",
							    inputType: "date",
							    format: 'YYYY-MM-DD',
							    label: "End date",
							    model: "end_date",
							    required: true,
							    placeholder: "Enter the End date",
							    validator: validators.date
							},
							{
								type: "textArea",
								label: "Note",
								model: "note",
								required: true,
								placeholder: "Note",
								rows: 4,
								validator: validators.string
							},
							{
							    type: "select",
							    label: "Task",
							    model: "task",
							    required: true,
							    values: function() {
							      return [
							        { id: "yes", name: "Yes" },
							        { id: "no", name: "No" },
							      ]
							    },
							},
							{
								type: "textArea",
								label: "Tags",
								model: "tags",
								required: true,
								placeholder: "Tags",
								rows: 4,
								validator: validators.string
							},
							{
							    type: "input",
							    inputType: "text",
							    label: "Type",
							    model: "type_field",
							    required: true,
							    placeholder: "Type",
							    validator: validators.string
							},
						]
					},
					],
			},
			formOptions: {
				validateAfterLoad: true,
				validateAfterChanged: true,
				fieldIdPrefix: 'user-'
			}
		}
	},
	methods: {
		onSubmit(evt){
			evt.preventDefault()

			const path = 'http://127.0.0.1:8000/api/notes/' + this.noteId + '/'
			console.log(this.model)
			axios.put(path, this.model).then((response) => {
				swal("Note edit sucessfully", "", "success")
			})
			.catch((response) => {
				swal("Sorry, there is a problem with the element!", "", "error")
			})
		},

		getNote () {
			const path = 'http://127.0.0.1:8000/api/notes/' + this.noteId + '/'
			axios.get(path).then((response) => {
				this.model.end_date = response.data.end_date
				this.model.note = response.data.note
				this.model.tags = response.data.tags
				this.model.task = response.data.task
				this.model.type_field = response.data.type_field
			})
			.catch((response) => {
				swal("Sorry, there is a problem with the element!", "", "error")
			})
		},
	},
	created () {
		this.getNote()
	},
}

</script>
<style lang="css" scoped>
</style>