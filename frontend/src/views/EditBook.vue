<template>
    <v-container>
        <v-form @submit.prevent="updateBook">
            <v-text-field v-model="book.name" label="Book name" />
            <v-select v-model="book.author_id" :items="authors" item-text="name" item-value="id" label="Select Author"
                required />
            <v-text-field v-model="book.type" label="Book type" />
            <v-checkbox v-model="book.is_available" label="Book is available"></v-checkbox>
            <v-btn class="mt-2" color="primary" type="submit" block>Update Book</v-btn>
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
        this.fetchBook();
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
        async fetchBook() {
            const bookId = this.$route.params.id;
            try {
                const response = await fetch(`http://localhost:4000/books/${bookId}`);
                const data = await response.json();
                this.book = data.book;
            } catch (error) {
                console.error('Error fetching book:', error);
            }
        },
        async updateBook() {
            const bookId = this.$route.params.id;
            try {
                const response = await fetch(`http://localhost:4000/books/${bookId}`, {
                    method: 'PATCH',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.book),
                });

                if (response.ok) {
                    this.$router.push('/books');
                } else {
                    console.error('Failed to update book');
                }
            } catch (error) {
                console.error('Error updating book:', error);
            }
        },
    },
};
</script>