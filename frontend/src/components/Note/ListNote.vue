<template lang='html'>
	<div class="container">
		<div class="row">
			<div class="card">
				<div class="card-body">
					<form @submit="onSubmit">
						<vue-form-generator :schema="schema" :model="model" :options="formOptions">
						</vue-form-generator>
						<div class="rows">
							<div class="col text-left">
								<b-button type="submit" variant="primary">Add</b-button>
							</div>
						</div>
					</form>
				</div>
			</div>
			<div class="col text-left">
				<h2>List of Notes</h2>
				<div class="col-md-12">
					<b-table striped hover :items="notes" :fields="fields">
						<template slot="action" slot-scope="data">
							<b-button size="sm" variant="primary" :to="{ name:'EditNote', params: {noteId: data.item.id} }">
								Edit
							</b-button>
							<b-button size="sm" variant="danger" :to="{ name:'DeleteNote', params: {noteId: data.item.id} }">
								Delete
							</b-button>
						</template>
					</b-table>
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
			fields: [
				{ key: 'id', label: "Note's ID" },
				{ key: 'note', label: "Note" },
				{ key: 'date', label: "Date" },
				{ key: 'end_date', label: "End Date" },
				{ key: 'action', label: "" },
			],
			notes: [],
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
						legend: "Add Note",
						fields: [
							{
							    type: "input",
							    inputType: "date",
							    label: "End date",
							    model: "end_date",
							    required: true,
							    placeholder: "Enter the End date",
							    format: 'YYYY-MM-DD',
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
			const path = 'http://127.0.0.1:8000/api/notes/'
			console.log(this.model)
			axios.post(path, this.model).then((response) => {
				swal("Note create sucessfully", "", "success")
				this.getNotes()
			})
			.catch((response) => {
				swal("Sorry, there is a problem with the creation of the element!", "", "error")
			})
		},

		getNotes () {
			const path = 'http://127.0.0.1:8000/api/notes/'
			axios.get(path).then((response => {
				this.notes = response.data
			}))
			.catch((error) => {
				console.log(error)
			})
		}

	},

	created () {
		this.getNotes()
	}
}
</script>

<style lang="css" scoped>
</style>