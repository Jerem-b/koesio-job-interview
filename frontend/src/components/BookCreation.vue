<template>
    <v-container>
        <v-form @submit.prevent="createBook">
            <v-text-field v-model="book.name" label="Book name"/>
            <v-select
                v-model="book.author_id" 
                :items="authors"
                item-text="name"
                item-value="id"
                label="Select Author"
                required/>
            <v-text-field v-model="book.type" label="Book type"/>
            <v-btn class="mt-2" color="primary" type="submit" block>Create Book</v-btn>
        </v-form>
    </v-container>
</template>

<script>
export default {
    data() {
        return {
            book: {
                name: '',
                author_id: null,
                is_available: true,
                type: '',
            },
            authors: [],
        };
    },
    created() {
        this.fetchAuthors();
    },
    methods: {
        async fetchAuthors() {
            try {
                const response = await fetch('http://localhost:4000/authors');
                const data = await response.json();
                this.authors = data.authors.map(author => ({
                    id: author.id,
                    name: author.name,
                }));
            } catch (error) {
                console.error('Error fetching authors:', error);
            }
        },
        async createBook() {
            try {
                const response = await fetch('http://localhost:4000/books', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.book),
                });

                if (response.ok) {
                    this.book = {
                        name: '',
                        author_id: null,
                        type: '',
                    };
                } else {
                    console.error('Error creating book');
                }
            } catch (error) {
                console.error('Error creating book:', error);
            }
        },
    },
};
</script>